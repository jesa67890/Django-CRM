# Install Mysql on your computer
# https"//dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = '192.168.50.32',
    user = 'remoteroot',
    passwd = 'password'

)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE jesadb2")

print("All Done!")