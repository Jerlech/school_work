import pickle
import os

def create():
    emp=[]
    with open('emp.dat', 'ab') as f:
        ans='y'
        while ans.lower()=='y':
            eno=int(input('Enter emp no: '))
            name=input('Enter emp name: ')
            salary=int(input('Enter salary: '))
            emp.append([eno, name, salary])
            ans=input('Add Morerecord? ')
        pickle.dump(emp,f)


def display():
    emp=[]
    with open('emp.dat', 'rb') as f:
        ans='y'
        while True:
            try:
                emp=pickle.load(f)
            except EOFError:
                break
        for e in emp:
            print(e)


def search():
    emp=[]
    with open('emp.dat', 'rb') as f:
        ans='y'
        print('**********************EMPLOYEE SEARCH FORM**************************')
        en=int(input('Enter Employee Number to Search: '))
        found=False
        while True:
            try:
                emp=pickle.load(f)
            except EOFError:
                break
        print('%10s'%'Emp No','%20s'%'Emp Name', '%10s'%'Emp Salary')
        print('******************************************************')
        for e in emp:
            if e[0]==en:
                print('%10s'%e[0], '%20s'%e[1], '%10s'%e[2])
                found=True
                break

        if found==False:
            print('## Sorry Employee Number Not Found ##')

def update():
    emp=[]
    with open('emp.dat', 'rb') as f:
        emp=pickle.load(f)
        print('## Employee Records ##')
        print(emp)
        print('----------------------------------------------------------------')

    with open('emp.dat', 'wb') as f:
        found=False
        en=int(input('Enter employee number to update: '))
        for i in range(len(emp)):
            if emp[i][0]==en:
                s1=int(input('Enter New Salary: '))
                emp[i][2]==s1
                found=True
                print('## Record Updated ##')
        
        if not found:
            print('## No such employee number ##')
        pickle.dump(emp,f)

    with open('emp.dat', 'rb') as f:
        emp=pickle.load(f)
        print('## employee records after update ##')
        print(emp)
        print('--------------------------------------------------------')



def delete():
    emp=[]
    with open('emp.dat', 'rb') as f:
        emp=pickle.load(f)
        
        print('## Employee Records ##')
        print(emp)
        print('------------------------------------------------------')

    with open('emp.dat', 'wb') as f:
        found=False
        en=int(input('Enter Employee Number to Delete: '))
        emp2=[]
        for i in range(len(emp)):
            if emp[i][0]!=en:
                emp2.append(emp[i])

        pickle.dump(emp2,f)

    with open('emp.dat', 'rb') as f:
        emp=pickle.load(f)
        print('## Employee Records After Delete ##')
        print(emp)
        print('------------------------------------------------------')





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


