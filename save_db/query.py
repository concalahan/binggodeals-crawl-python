from influxdb import InfluxDBClient

# documentation
# https://influxdb-python.readthedocs.io/en/latest/api-documentation.html#influxdbclient
# https://influxdb-python.readthedocs.io/en/latest/examples.html

client = InfluxDBClient(host='103.216.112.226', port=8086, database='mydb')
dbs = client.get_list_database()
print("The database name is: " + str(dbs))

query = "select * from products where product_url='https://tiki.vn/may-tinh-bang-xiaomi-mipad-4-phien-ban-sim-4g-wifi-64gb-4gb-vang-hong-cuong-luc-hang-nhap-khau-p3834035.html';"
result = client.query(query)
print(result)