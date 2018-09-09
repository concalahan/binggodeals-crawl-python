from influxdb import InfluxDBClient

# documentation
# https://influxdb-python.readthedocs.io/en/latest/api-documentation.html#influxdbclient
# https://influxdb-python.readthedocs.io/en/latest/examples.html

client = InfluxDBClient(host='127.0.0.1', port=8086, database='mydb')
dbs = client.get_list_database()
print("The database name is: " + str(dbs))

query = "select * from products where product_url='https://tiki.vn/dien-thoai-nokia-1-hang-chinh-hang-p1666629.html?src=recently-viewed';"
result = client.query(query)
print(result)