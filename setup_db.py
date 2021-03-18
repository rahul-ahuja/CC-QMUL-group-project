import sqlite3

conn = sqlite3.connect('stocks.db')
cur = conn.cursor()


cur.execute('''DROP TABLE IF EXISTS users''')
cur.execute('''DROP TABLE IF EXISTS purchases''')
cur.execute('''DROP TABLE IF EXISTS sales''')

#create users table
cur.execute('''CREATE TABLE users (id INTEGER, 
	username TEXT NOT NULL, 
	hash TEXT NOT NULL, 
	PRIMARY KEY(id))''')


#create purchases table
#cur.execute('''CREATE TABLE purchases (id INTEGER, 
#	symbol TEXT NOT NULL, 
#	price FLOAT NOT NULL, 
#	quantity INTEGER, 
#	user_id INTEGER, 
#	share_name TEXT, 
#	PRIMARY KEY(id))''')


#create sales table
cur.execute('''CREATE TABLE sales (id INTEGER, 
	symbol TEXT NOT NULL, 
	price FLOAT NOT NULL,  
	user_name TEXT NOT NULL, 
	share_name TEXT, 
	PRIMARY KEY(id))''')

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()