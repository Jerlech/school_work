import mysql.connector as mc

mycon=mc.connect(host='localhost', user='root', passwd='root', database='JEREMY_PYTHON')

if mycon.is_connected():
    print('Successfully connected to MySQL.')

cursor=mycon.cursor()
cursor.execute('select * from student')
print(cursor)

data=cursor.fetchall()
for row in data:
    print(row)
    for d in row:
        print(d)

    print()

print(cursor.rowcount)