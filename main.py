import psycopg2

conn = psycopg2.connect(
	host="localhost",
	port="5432",
	dbname="testdb",
	user='test',
	password='1234'
)

cursor = conn.cursor()

cursor.execute("""
	CREATE TABLE IF NOT EXISTS test_table(
		id SERIAL PRIMARY KEY,
		name VARCHAR(50)
		);
""")

# cursor.execute("INSERT INTO test_table (name) VALUES (%s)", ("Test Name",))
cursor.execute("UPDATE test_table SET name='change name' WHERE id=4;")
conn.commit()


cursor.execute('SELECT * FROM test_table ORDER BY id;')
rows = cursor.fetchall()

for row in rows:
	print(row)

cursor.close()
conn.close()

