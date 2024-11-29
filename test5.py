import mysql.connector as mc

con=mc.connect(host='localhost', user='root', passwd='root', database='JEREMY_PYTHON')

if con.is_connected():
    print('Successfully connected to MySQL.')

data=con.cursor()
data.execute('select * from emp')

records=data.fetchall()
for i in records:
    for j in i:
        print(j, end=',')
    print()

print(data.rowcount)