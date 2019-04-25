import sqlite3 as lite
import sys

con = None

try:
	con = lite.connect('UMBC.db')
	cur = con.cursor()
	myStmt="go"
	while myStmt != "quit":
		print(chr(27) + "[2J")
		sys.stderr.write("\x1b[2J\x1b[H")
		myStmt = raw_input('Enter SQL Statement :')
		if myStmt != "quit":
			cur.execute(myStmt)
			data = cur.fetchall()
			print("The results are:")
			for rec in data:
				for field in rec:
					print(str(field)+'\t'),#maybe bad formatting
				print('')
			myWait = raw_input('Press enter to continue')
	con.commit()
	con.close()
except lite.Error, e:
	print("Error %s" % e.args[0])
	sys.exit(1)