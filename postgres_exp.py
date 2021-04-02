import psycopg2

#making connection to the stocks database
conn = psycopg2.connect('host=127.0.0.1 dbname=stocks user=developer4 password=dev_pswd')
cur = conn.cursor()
conn.set_session(autocommit=True)

#developer does not have privilege to drop any table from the schema
cur.execute('''DROP TABLE IF EXISTS stocks.users''')

cur.execute('''SELECT * FROM stocks.users''')
print(cur.fetchall())
