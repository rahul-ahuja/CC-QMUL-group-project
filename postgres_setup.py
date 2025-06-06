import psycopg2

#making connection to the postgres database called stocks as an owner- Database Admin
conn = psycopg2.connect('host=172.17.0.2 dbname=stocks user=dba password=dba_pswd')
cur = conn.cursor()
conn.set_session(autocommit=True)

#creating the schema of the database called stocks
try:
        cur.execute('''CREATE SCHEMA stocks''')
except:
        print('Schema already created')

#making user the table with same does not exists
cur.execute('''DROP TABLE IF EXISTS stocks.users''')
cur.execute('''DROP TABLE IF EXISTS stocks.sales''')

#creating users tables in the schema
cur.execute('''CREATE TABLE stocks.users (id SERIAL PRIMARY KEY,
        username TEXT NOT NULL,
        hash TEXT NOT NULL)''')

#create sales table
cur.execute('''CREATE TABLE stocks.sales (id SERIAL PRIMARY KEY,
        symbol TEXT NOT NULL,
        price FLOAT NOT NULL,
        user_name TEXT NOT NULL,
        share_name TEXT)''')


#cur.execute('''REVOKE SELECT, INSERT ON TABLE users FROM readwrite3''')
#creating a role for role-based policy
try:
        cur.execute('''CREATE ROLE readwrite4''')
except:
        print('Role already created')

#granting the role with certain privileges

cur.execute('''GRANT CONNECT ON DATABASE stocks TO readwrite4''')
cur.execute('''GRANT SELECT, INSERT, UPDATE ON TABLE stocks.users TO readwrite4''')
cur.execute('''GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE stocks.sales TO readwrite4''')
cur.execute('''GRANT USAGE ON ALL SEQUENCES IN SCHEMA stocks TO readwrite4''')
cur.execute('''GRANT USAGE ON SCHEMA stocks TO readwrite4''')

#assigning the role to the user called developer4 who will work on the main application
try:
        cur.execute("CREATE USER developer4 WITH PASSWORD 'dev_pswd'")
except:
        print('User already created')

cur.execute('''GRANT readwrite4 TO developer4''')
conn.close() #closing the database connection
