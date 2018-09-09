# -*- coding: utf-8 -*-

# Why we use influxdb:
# Measurements are like buckets.
# Tags are indexed values.
# Fields are the actual data.
# Data is written into InfluxDB via line protocol

from influxdb import InfluxDBClient
from influxdb import SeriesHelper
import datetime
import os
import json

now = datetime.datetime.now()

# the place store filter json file
READ_DIR = '../data/' + str(now.year) + '/' + str(now.month) + '/' + str(now.day) + '/json/'

# InfluxDB connections settings
host = 'localhost'
port = 8086
user = 'root'
password = 'nvu123456'
dbname = 'mydb'

myclient = InfluxDBClient(host, port, user, password, dbname)

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

for filename in os.listdir(READ_DIR):
    with open(READ_DIR + filename) as fp:
        data = json.load(fp)
        # points will be written on the wire via MySeriesHelper.Meta.client.
        # the product URL will be the key -> for faster index and search

        print("Process " + str(data['url']))

        MySeriesHelper(
            product_url=data['url'], 
            time=data['created'], 
            origin_price=data['origin_price'], 
            true_price=data['true_price'])

        # To manually submit data points which are not yet written, call commit:
        MySeriesHelper.commit()

# To inspect the JSON which will be written, call _json_body_():
# MySeriesHelper._json_body_()