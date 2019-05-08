'''This file is used to be the driver for SOAP database
'''
import pymysql
import csv
# Connection generator in one place for easy adjustment later
def getConn():
	return pymysql.connect(host='localhost',
						   user='root',
						   password='',
						   db='SOAP',
						   autocommit=True)
						   
'''prints formatted table, given a cursor object ready to be fetchall()'d'''
def tableify(cursor):
	try:
		rows = cursor.fetchall()
	except:
		return
	#print column titles
	col_names = [i[0] for i in cursor.description]
	print("| ",end='')
	for j in col_names:
		print(j,end=' | ')
	print()#newline
	print("------------------------------------")
	#print the actual data
	for x in rows:
		print("| ",end='')
		for y in x:
			print(y,end=' | ')
		print();
		
'''loads data from csv and inserts it into database'''		
def csvLoad(connection, fileName, tableName):
	connection = connection.cursor()
	try:
		with open(fileName,'r',newline='') as f:
			myReader = csv.reader(f)
			for data in myReader:
				for x in data:
					inputCommand = "insert into "+tableName+" values(" +', '.join("'" + item + "'" for item in data)+");"
				print(inputCommand)
				try:
					cursor.execute(inputCommand)
				except:
					print("Something went wrong")
					connection.rollback()
	except:
		print("No such file or directory:",fileName)
connection = getConn()
cursor = connection.cursor()
inputCommand = ""
print("note: syntax for csv loading is load fileName into tableName")
while inputCommand != "quit":
		inputCommand = input(">> ")	
		if inputCommand != "quit":
			if (inputCommand.split(' ', 1)[0] == "load") and (inputCommand.split(' ', 3)[2] == "into"):
				'''load format: load fileName into tableName'''
				fileName = inputCommand.split(' ', 2)[1]
				tableName = inputCommand.split(' ', 4)[3]
				csvLoad(connection, fileName, tableName)
			elif inputCommand.split(' ', 1)[0] == "select":
				try:
					cursor.execute(inputCommand)
				except:
					print("Invalid Syntax, try again")
					connection.rollback()
				tableify(cursor)
			else:
				try:
					cursor.execute(inputCommand)
				except:
					print("Invalid Syntax, try again")
					connection.rollback()


cursor.close()
connection.close()

