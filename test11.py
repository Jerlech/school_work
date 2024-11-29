import csv
import tabulate
import os

def create():
    with open('samp1.csv', mode='a', newline='') as csf:
        mywriter=csv.writer(csf, delimiter=',')
        ans='y'
        while ans.lower()=='y':
            eno=int(input('Enter Employee Number: '))
            ename=input('Enter Employee Name: ')
            salary=int(input('Enter Salary: '))
            mywriter.writerow([eno, ename, salary])
            print('Data Saved...')
            ans=input('Do you want to add more?(y/n) ')

def display():
    headers=['Employee Number', 'Employee Name', 'Salary']
    dat=[]
    with open('samp1.csv') as csf:
        myreader=csv.reader(csf, delimiter=',')
        for i in myreader:
            dat.append(i)

        tab=tabulate.tabulate(dat, headers, tablefmt='fancy_outline', stralign="center")
        print(tab)


def search():
    headers=['Employee Name', 'Salary']
    datmain=[]
    dat=[]
    with open('samp1.csv') as csf:
        myreader=csv.reader(csf, delimiter=',')

        
        records=list(myreader)
        ans='y'
        while ans.lower()=='y':
            found=False
            print(records)
            sear=int(input('Enter Employee Number to Search: '))
            for i in records:
                #print(i)
                
                if len(i)!=0:
                    #print(i)
                    
                    if int(i[0])==sear:
                        #print(i)
                        
                        dat.extend([i[1], i[2]])
                        datmain.append(dat)
                        found=True
                        break
            
            if not found:
                print("Employee not Found...")
            else:
                tab=tabulate.tabulate(datmain, headers, tablefmt='fancy_outline', stralign="center")
                print(tab)
               
            
            ans=input('Do you want to search more?(y/n)')
            dat.clear()
            datmain.clear()


def update():
    with open('samp1.csv', 'r') as csf:
        myreader=csv.reader(csf, delimiter=',')
        records=list(myreader)
        print(records)
        modi=int(input('Enter Employee Number to be modified: '))
        for i in records:
            if len(i)!=0:
                if int(i[0])==modi:
                    while True:
                        print('''What do you want to modify?
                            1. Employee Number
                            2. Employee Name
                            3. Salary
                            4. Exit''')
                        ch=int(input('Enter you choice: '))
                        if ch==1:
                            emp_no=int(input('Enter new Employee Number: '))
                            i[0]=emp_no

                        elif ch==2:
                            emp_name=input('Enter new Employee Name: ')
                            i[1]=emp_name

                        elif ch==3:
                            salary=input('Enter new Salary: ')
                            i[2]=salary

                        elif ch==4:
                            print('Exiting modify mode....')
                            break

                        else:
                            print('Invalid Choice')

        

    with open('samp2.csv', mode='a', newline='') as csf1:
        mywriter=csv.writer(csf1, delimiter=',')
        for i in records:
            mywriter.writerow(i)
        print('Data Saved...')


    os.remove('samp1.csv')
    os.rename('samp2.csv', 'samp1.csv')





def delete():
    with open('samp1.csv', 'r') as csf:
        myreader=csv.reader(csf, delimiter=',')
        records=list(myreader)
        print(records)
        dele=int(input('Enter Employee number to be deleted: '))
        found=False
        for i in records:
            if len(i)!=0:
                if int(i[0])==dele:
                    records.remove(i)
                    found=True

        if not found:
            print('Employee not found...')




    with open('samp2.csv', mode='a', newline='') as csf1:
        mywriter=csv.writer(csf1, delimiter=',')
        for i in records:
            mywriter.writerow(i)


    os.remove('samp1.csv')
    os.rename('samp2.csv', 'samp1.csv')






while True:
    print("""Menu Driven
          1. Create
          2. Display
          3. Search
          4. Update
          5. Delete
          6. Exit""")
    

    choice=int(input('Enter your choice: '))

    if choice==1:
        create()

    elif choice==2:
        display()

    elif choice==3:
        search()

    elif choice==4:
        update()

    elif choice==5:
        delete()

    elif choice==6:
        print('Exiting the program....')
        break

    else:
        print('Invalid choice...')
        print('Re-enter your choice')




