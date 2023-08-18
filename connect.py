import pyodbc
conn=pyodbc.connect(r"Driver={​​​​​​​​Microsoft Access Driver (*.mdb, *.accdb)}​​​​​​​​;DBQ=C:\Users\cuc\Documents\icq\Database2.accdb;")
cursor=conn.cursor()
cursor.execute("SELECT * FROM personas")
for row in cursor.fetchall():
    print(row)

