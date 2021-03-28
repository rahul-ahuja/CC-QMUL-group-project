import psycopg2

conn = psycopg2.connect('host=127.0.0.1 dbname=stocks user=dba password=dba_pswd')

cur = conn.cursor()

conn.set_session(autocommit=True)

try:
	cur.execute('''CREATE SCHEMA stocks''')
except:
	print('Schema already created')
#create users table

cur.execute('''DROP TABLE IF EXISTS stocks.users''')
cur.execute('''DROP TABLE IF EXISTS stocks.sales''')

cur.execute('''CREATE TABLE stocks.users (id SERIAL PRIMARY KEY, 
	username TEXT NOT NULL, 
	hash TEXT NOT NULL)''')

#create sales table
cur.execute('''CREATE TABLE sales (id SERIAL INTEGER PRIMARY KEY, 
	symbol TEXT NOT NULL, 
	price FLOAT NOT NULL,  
	user_name TEXT NOT NULL, 
	share_name TEXT, 
	PRIMARY KEY(id))''')


#cur.execute('''REVOKE SELECT, INSERT ON TABLE users FROM readwrite3''')

try:
	cur.execute('''CREATE ROLE readwrite4''')
except:
	print('Role already created')

cur.execute('''GRANT CONNECT ON DATABASE stocks TO readwrite4''')
cur.execute('''GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA stocks TO readwrite4''')
cur.execute('''GRANT USAGE ON ALL SEQUENCES IN SCHEMA stocks TO readwrite4''')


try:
	cur.execute("CREATE USER developer4 WITH PASSWORD 'dev_pswd'")
except:
	print('User already created')

cur.execute('''GRANT readwrite4 TO developer4''')
conn.close()