#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import datetime
import os
import json
import re

def main():
  con = MySQLdb.connect(
  host="localhost",
  user="root",
  passwd="root",
  db="ecommerce")

  #con.set_character_set('utf8')

  c = con.cursor()

  # sample code
  # c.execute("""INSERT INTO categories (category_id, category_name) VALUES (%s, %s)""", ("1", "cong nghe",))
  # con.commit()

  # note that category_id, image_id, discount_id is 1

  # c.execute("""SELECT spam, eggs, sausage FROM breakfast
  #         WHERE price < %s""", (max_price,))

  now = datetime.datetime.now()

  # the place store filter json file
  READ_DIR = '../data/' + str(now.year) + '/' + str(now.month) + '/' + str(now.day) + '/json/'

  i = 2
  for filename in os.listdir(READ_DIR):
    with open(READ_DIR + filename) as fp:
      data = json.load(fp)
      # print(data)

      true_price = re.findall(r'\d+', data["true_price"])
      true_price = ''.join(true_price)
      c.execute("""
      INSERT INTO products 
      (product_id, product_name, product_price, product_quantity, 
      category_id, product_description, product_brand, image_id, discount_id) 
      VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
      """, (i, data["name"].encode('utf-8'), true_price, 1, 
      1, data["description"].encode('utf-8'), data["store"].encode('utf-8'), 1, 1))
      con.commit()

      i+=1

  if con: con.close()

if __name__ == "__main__":
  main()


