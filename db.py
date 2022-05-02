from sqlite3 import connect

# create database and cursor connection
DBCON = connect('mystreamlitdb.db')
CUR = DBCON.cursor()

# create the data table
CUR.execute('CREATE TABLE datatable (pkey INTEGER, userinput TEXT)')

# insert some data
CUR.execute('INSERT INTO datatable (pkey, userinput) VALUES (1,NULL)')
CUR.execute('INSERT INTO datatable (pkey, userinput) VALUES (2,NULL)')
CUR.execute('INSERT INTO datatable (pkey, userinput) VALUES (3,NULL)')
CUR.execute('INSERT INTO datatable (pkey, userinput) VALUES (4,NULL)')
CUR.execute('INSERT INTO datatable (pkey, userinput) VALUES (5,NULL)')

# commit above to database
DBCON.commit()
