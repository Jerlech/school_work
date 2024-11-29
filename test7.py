import mysql.connector as mc

con=mc.connect(host='localhost', user='root', passwd='root', database='JEREMY_PYTHON')

if con.is_connected():
    print('Successfully connected to MySQL.')

data=con.cursor()

while True:
    print("""\nEmployee List
          1. Add data
          2. Display the records
          3. Search employees
          4. Modify details
          5. Delete a record
          6. Exit\n""")
    
    choice=int(input('Enter your choice: '))


    if choice==1:
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


    elif choice==2:
        data.execute('select * from emp')
        records=data.fetchall()
        for i in records:
            for j in i:
                print(j, end=',')
            print()
        print()
        print(f'Total records collected: {data.rowcount}')


    elif choice==3:
        while True:
            print("""Which of the following ways do you want to serach with?
                1. Employee Number
                2. Employee Name
                3. Department""")
            
            choice1=int(input('Enter your choice: '))
            if choice1==1:
                sear1=int(input('Enter Emp no: '))
                query1="select * from emp where empno={0}".format(sear1)
                data.execute(query1)
                records=data.fetchone()

                if records is None:
                    print('No record existing....')
                    break

                else:
                    print(records)
                    print()
                    print(f'Total records collected: {data.rowcount}')
                    break

            elif choice1==2:
                sear2=input('Enter Emp Name: ')

                query2="select * from emp where name='{0}'".format(sear2)
                data.execute(query2)
                records1=data.fetchall()

                if records1 is None:
                    print('No record existing......')
                    break
                else:
                    print(records1)
                    print()
                    print(f'Total records collected: {data.rowcount}')
                    break

            elif choice1==3:
                sear3=input('Enter Dept: ')

                query3="select * from emp where dept='{0}';".format(sear3)
                data.execute(query3)
                records2=data.fetchall()

                if records2 is None:
                    print('No record existing......')
                    break
                else:
                    print(records2)
                    print()
                    print(f'Total records collected: {data.rowcount}')
                    break



    elif choice==4:
        while True:
            print("""Which of the following ways do you want to modify with?
                1. Employee Number
                2. Employee Name
                3. Department
                4. Salary""")
            

            choice2=int(input('Enter your choice: '))
            
            if choice2==1:
                sea11=int(input('Enter Emp no to be modified: '))
                sea12=int(input('Enter new Emp no: '))
                qu1="update emp set empno={0} where empno={1}".format(sea12, sea11)
                data.execute(qu1)
                con.commit()
                print('Emp no updated successfully...')
                break

            elif choice2==2:
                sea21=input('Enter Emp no to be modified: ')
                sea22=input('Enter new Emp name: ')
                qu2="update emp set name='{0}' where empno='{1}'".format(sea22, sea21)
                data.execute(qu2)
                con.commit()
                print('Emp name updated successfully...')
                break

            elif choice2==3:
                sea31=int(input('Enter emp no of the person to modify dept: '))
                sea32=input('Enter new dept: ')
                qu3="update emp set dept='{0}' where empno={1}".format(sea32, sea31)
                data.execute(qu3)
                con.commit()
                print('Department updated successfully...')
                break

            elif choice2==4:
                sea41=int(input('Enter Emp no to be modified: '))
                sea42=int(input('Enter new Salary: '))
                qu4="update emp set salary={0} where empno={1}".format(sea42, sea41)
                data.execute(qu4)
                con.commit()
                print('Salary updated successfully...')
                break

            else:
                print('Invalid choice...')
                break

    elif choice==5:
        de=int(input('Enter emp no to be deleted: '))
        q1="delete from emp where empno={0}".format(de)
        data.execute(q1)
        con.commit()
        print(f'Deleted Emp no: {de} successfully...')
        break

    elif choice==6:
        print('Exiting the program....')
        break

    else:
        print('Invalid choice...')
        break





