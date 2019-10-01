import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='vladimir', password='12345',
                              host='127.0.0.1',
                              database='publications')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
    cursor = cnx.cursor() 
    cursor.execute("DESCRIBE classics") 
    print(cursor.fetchall()) 
cnx.close()