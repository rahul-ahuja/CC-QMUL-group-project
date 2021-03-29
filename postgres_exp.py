import psycopg2

conn = psycopg2.connect('host=127.0.0.1 dbname=stocks user=developer4 password=dev_pswd')

cur = conn.cursor()

conn.set_session(autocommit=True)


cur.execute('''DROP TABLE IF EXISTS stocks.users''')

cur.execute('''SELECT * FROM stocks.sales''')
print(cur.fetchall())
