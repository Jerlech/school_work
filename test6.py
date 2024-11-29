import mysql.connector as mc

con=mc.connect(host='localhost', user='root', passwd='root', database='JEREMY_PYTHON')

if con.is_connected():
    print('Successfully connected to MySQL.')
    print('Welcome to employee data entry')

data=con.cursor()

ans='yY'

while ans in 'yY':
    empno=int(input('Enter employee no: '))
    name=input('Enter name: ')
    dept=input('Enter department: ')
    sal=int(input('Enter salary: '))

    query="insert into emp values({0},'{1}','{2}',{3})".format(empno, name, dept, sal)

    data.execute(query)

    con.commit()
    print("## Record Saved..... ##")

    ans=input('Add more? (y,n): ')








