# binggodeals: a product-crawling project
For educational purpose.

## Introduction
The project will crawl data from e-commerce website and apply ML to determine which products are similar to each other.

## Post-introduction
The project is divided into 4 sub-project.
1. **Fixed_rawl_url project (1)**: This project will crawl all products in specific categories on two sites <https://tiki.vn/> and <https://www.adayroi.com/>, then it will divide the product into brand-based folder (for example: it will have folder samsung, sony, apple, asus,...).

Each of the brand it will contain the pre-defined .txt file, which include those pre-defined term for matching products. 2 sub-folder (2 crawled sites) and 1 folder contain matching information if found.

2. **Parse_url_to_html project (2)**: This project will read the crawled.txt file and store crawled .html product files into /data folder according to time.
3. **Filter_data_from_file project (2)**: This project will read those .html file from sub-project above and, filter informative data and store as .json file
4. **Save_db project (4)**: This project will read those .json files from above and save to [influxdb](https://www.influxdata.com/)

Note: Naming convention is not set yet

## How to run it
### Project 1:
```
python3 main.py
```

for example:
```
python3 main.py
```

### Project 2:
```
python3 main.py
```

for example:
```
python3 main.py
```

### Project 3:
```
python3 main.py
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
