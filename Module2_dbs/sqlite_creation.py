import sqlite3

# create a simple SQLite database and a table
sqlite3.connect('example.db')


# connect to the database
conn = sqlite3.connect('example.db')

# create a cursor object which allows us to execute SQL commands
cursor = conn.cursor()

# create a X with raw sql commands
cursor.execute('''INSERT IN YOUR SQL CODE HERE''')

# commit the changes
conn.commit()

# close the connection
conn.close()