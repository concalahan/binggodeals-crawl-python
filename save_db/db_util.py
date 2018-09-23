import MySQLdb
import datetime
import os
import json

def main():
  my_db = MySQLdb.connect(
  host="localhost",
  user="root",
  passwd="root",
  db="ecommerce")

  c=my_db.cursor()
  
  # sample code
  c.execute("""INSERT INTO categories (category_id, category_name) VALUES (%s, %s)""", ("1", "cong nghe",))
  my_db.commit()

  # note that category_id, image_id, discount_id is 1

  # c.execute("""SELECT spam, eggs, sausage FROM breakfast
  #         WHERE price < %s""", (max_price,))

  now = datetime.datetime.now()

  # the place store filter json file
  READ_DIR = '../data/' + str(now.year) + '/' + str(now.month) + '/' + str(now.day) + '/json/'

  for filename in os.listdir(READ_DIR):
    with open(READ_DIR + filename) as fp:
      data = json.load(fp)
      print(data)

      c.execute("""
      INSERT INTO products (product_name, product_description) VALUES (%s, %s)
      """, ("1", "cong nghe",))
      my_db.commit()

if __name__ == "__main__":
  main()


