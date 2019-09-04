import sqlite3

connect = sqlite3.connect('quotes.db')
cursor = connect.cursor()

# cursor.execute("""create table quotes_tb (
# title text,
# author text,
# tag text
# )""")
cursor.execute("""insert into quotes_tb values ('test','test2', 'test3')""")
connect.commit()
connect.close()
# https://sqliteonline.com/index.html