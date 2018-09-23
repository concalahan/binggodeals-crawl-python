from influxdb import InfluxDBClient
from influxdb import SeriesHelper

def main():
    # query remote database
    client = InfluxDBClient(
        host='103.216.112.226', 
        port=8086, 
        username='admin', 
        password='nvu123456')

    dbs = client.get_list_database()
    print("The database name is: " + str(dbs))

    query = "SELECT COUNT(*) FROM /.*/"
    result = client.query(query)
    print(result)

if __name__== "__main__":
    main()