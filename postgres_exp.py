import psycopg2

conn = psycopg2.connect('host=127.0.0.1 dbname=stocks user=developer4 password=dev_pswd')

cur = conn.cursor()

conn.set_session(autocommit=True)


#cur.execute('''DROP TABLE IF EXISTS users''')
#cur.execute('''INSERT INTO stocks.users (username, hash) VALUES (%s, %s)''', ('exp', 'pswd'))
cur.execute('''SELECT * FROM stocks.users''')
print(cur.fetchall())