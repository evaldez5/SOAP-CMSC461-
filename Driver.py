'''This file is used to be the driver for SOAP database
'''
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
    try:
        inputCommand = input("What is next command? ")
        if inputCommand != "quit":
            if inputCommand.split(' ', 1)[0] == "load":
                '''load format: load fileName into tableName'''
                fileName = inputCommand.split(' ', 1)[1]
                tableName = inputCommand.split(' ', 1)[3]
                #todo load from a csv file
            elif inputCommand.split(' ', 1)[0] == "select":
                cursor.execute(inputCommand)
                rows_s = str(cursor.fetchall())
                #todo format data and print out
            else:
                cursor.execute(inputCommand)
    except:
        print("Wrong SQL Syntax, try again")
        connection.rollback()


cursor.close()
connection.close()

