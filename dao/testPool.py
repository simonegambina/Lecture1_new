import time

import mysql.connector

tic = time.time()

for i in range(100):
    cnx = mysql.connector.connect(user="root",
                                  password="Golden2026!",
                                  host="127.0.0.1",
                                  database="sw_gestionale")
    cursor = cnx.cursor()
    query = "select * from prodotti"
    cursor.execute(query)
    out = cursor.fetchall()
    cursor.close()
    cnx.close()
toc = time.time()

print(f"Tempo con connect:{toc-tic}")

tic = time.time()
cnxPool = mysql.connector.pooling.MySQLConnectionPool(host="127.0.0.1",
                                                      user="root",
                                                      password="Golden2026!",
                                                      database="sw_gestionale",
                                                      pool_size=3,
                                                      pool_name="mypool")

for i in range(100):
    cnx = cnxPool.get_connection()
    cursor = cnx.cursor()
    query = "select * from prodotti"
    cursor.execute(query)
    out1 = cursor.fetchall()
    cursor.close
    cnx.close()
toc = time.time()
print(f"Tempo di esecuzione con pooling:{toc-tic}")