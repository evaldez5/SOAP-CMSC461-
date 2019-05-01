'''This file is used to be the driver for SOAP database
'''
import json
import pymysql

# Connection generator in one place for easy adjustment later
def getConn():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='team4our++',
                           db='SOAP',
                           autocommit=True)

connection = getConn()
cursor = connection.cursor()
inputCommand = ""

while inputCommand != "quit":
    inputCommand = input("What is next command? ")
    cursor.execute(inputCommand)
