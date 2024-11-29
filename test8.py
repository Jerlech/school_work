import mysql.connector as mc

con=mc.connect(host='localhost', user='root', passwd='root', database='JEREMY_PYTHON')

if con.is_connected():
    print('Successfully connected to MySQL.')

data=con.cursor()

def issue_book():
    while True:                     
        stid=int(input('Enter student ID: '))
        q1="select name from students where regno={0}".format(stid)
        data.execute(q1)
        r=data.fetchone()

        if r is None:
            print('No record existing....')
            print('Re-enter student ID...')
            continue

        else:
            print(r)
            print()
            break

    while True:
        bk=input('Enter Book Name: ')
        q2="select * from books where bkname='{0}' ".format(bk)
        data.execute(q2)
        r1=data.fetchone()

        if r1 is None:
            print('Book not available....')
            print('Re-enter Book name...')
            continue

        else:
            print(r1)
            print()
            break

    while True:
        paid=input('Did the student pay?(y/n): ')
        if paid in 'Yy':
            q3="update rental set paid={0} where reg"
    

issue_book()