import pandas 
from pandas.io import sql
import pymysql
retaildb_con_i = pymysql.connect(host='XXXX', port=XXXX, user='XXXX', password='XXXX', database='XXXX')
sql_q="select order_item_id,order_item_order_id,order_item_product_id,order_item_quantity,order_item_subtotal,order_item_product_price from order_items;"
pandas.read_sql(sql_q, conn)
conn.close()
