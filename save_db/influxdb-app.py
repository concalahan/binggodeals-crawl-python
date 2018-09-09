# -*- coding: utf-8 -*-

# Why we use influxdb:
# Measurements are like buckets.
# Tags are indexed values.
# Fields are the actual data.
# Data is written into InfluxDB via line protocol

from influxdb import InfluxDBClient
from influxdb import SeriesHelper
import datetime

# InfluxDB connections settings
host = 'localhost'
port = 8086
user = 'root'
password = 'nvu123456'
dbname = 'mydb'

myclient = InfluxDBClient(host, port, user, password, dbname)

now = datetime.datetime.now()

# Uncomment the following code if the database is not yet created
myclient.create_database(dbname)
myclient.create_retention_policy('awesome_policy', '3d', 3, default=True)


class MySeriesHelper(SeriesHelper):
    """Instantiate SeriesHelper to write points to the backend."""

    class Meta:
        """Meta class stores time series helper configuration."""

        # The client should be an instance of InfluxDBClient.
        client = myclient

        # The series name must be a string. Add dependent fields/tags
        # in curly brackets.
        series_name = 'products'

        # Defines all the fields in this time series.
        fields = ['time', 'origin_price', 'true_price']

        # Defines all the tags for the series.
        tags = ['product_url']

        # Defines the number of data points to store prior to writing
        # on the wire.
        bulk_size = 5

        # autocommit must be set to True when using bulk_size
        autocommit = True


# The following will create *five* (immutable) data points.
# Since bulk_size is set to 5, upon the fifth construction call, *all* data
# points will be written on the wire via MySeriesHelper.Meta.client.
MySeriesHelper(product_url='https://tiki.vn/dien-thoai-nokia-1-hang-chinh-hang-p1666629.html?src=recently-viewed', time=now, origin_price=1331, true_price=1330)

# To manually submit data points which are not yet written, call commit:
MySeriesHelper.commit()

# To inspect the JSON which will be written, call _json_body_():
MySeriesHelper._json_body_()