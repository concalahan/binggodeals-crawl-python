# binggodeals: a product-crawling project
For educational purpose.

## Introduction
The project will crawl data from e-commerce website and apply ML to determine which products are similar to each other.

## Post-introduction
The project is divided into 4 sub-project.
1. **Crawl_url project (1)**: This project will crawl all products in specific categories on two sites <https://tiki.vn/> and <https://www.adayroi.com/> and store it in a file, which named crawled.txt
2. **Parse_url_to_html project (2)**: This project will read the crawled.txt file and store crawled .html product files into /data folder
3. **Filter_data_from_file project (2)**: This project will read those .html file from sub-project above and, filter informative data and store as .json file
4. **Save_db project (4)**: This project will read those .json files from above and save to [influxdb](https://www.influxdata.com/)

Note: Naming convention is not set yet

## How to run it
### Project 1:
```
python3 main.py HOMEPAGE CATEGORY_URL
```

for example:
```
python3 main.py tiki.vn https://tiki.vn/dien-thoai-may-tinh-bang/c1789
```

### Project 2:
```
python3 main.py HOMEPAGE
```

for example:
```
python3 main.py tiki.vn
```

### Project 3:
```
python3 main.py HOMEPAGE
```

for example:
```
python3 main.py tiki.vn
```

### Project 4:
#### Influx DB basic syntax

**Start the Database**
```
systemctl start influxdb
```

**Start shell**
```
influx
```

**Use the database**
```
use mydb
```

**Show list database**
```
show databases
```

**Get list column**
```
select * from /.*/ limit 1
```

**Get field**
```
show field keys
```

**Select all row**
```
select * from /.*/
```