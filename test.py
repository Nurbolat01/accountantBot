import sqlite3

try:
	conn = sqlite3.connect("accountant.db")
	cursor = conn.cursor()
	#connecting to db

	# always nessasary
	conn.commit()
except sqlite3.Error as error:
	print("Error", error)

finally:
	if(conn):
		conn.close()