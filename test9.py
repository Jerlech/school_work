import os

def create():
    size=20
    with open('names.dat', 'ab+') as f:
        ans='y'
        while ans.lower()=='y':
            n1=input('Enter Name: ')
            l1=len(n1)
            n1=n1+(size-l1)*' '
            n1=n1.encode()
            f.write(n1)
            ans=input('Add More?')


def display():
    size=20
    num=int(input('Enter Record Number: '))
    with open('names.dat', 'rb') as f:
        f.seek(size*(num-1))
        str=f.read(size)
        if len(str)==0:
            print('Incorrect Position')
        else:
            print(str.decode())

def search():
    sizeofrec=20
    size=os.path.getsize('names.dat')
    print(f'Size of file: {size}')

    numrec=int(size/sizeofrec)
    print(f'Number of Records: {numrec}')

    with open('names.dat', 'rb') as f:
        n=input('Enter Name to Search: ')
        n=n.encode()
        pos=0
        found=False
        for i in range(numrec):
            f.seek(pos)
            str=f.read(20)
            if n in str:
                print('Found at Record # ', (i+1))
                found=True
            pos+=sizeofrec
        
        if not found:
            print('Name not Found')

def update():
    sizeofrec=20
    size=os.path.getsize('names.dat')
    print(f'Size of file: {size}')

    numrec=int(size/sizeofrec)
    print(f'Number of Records: {numrec}')

    with open('names.dat', 'r+b') as f:
        oldname=input('Enter name: ')
        oldname=oldname.encode()

        newname=input('Enter new name: ')
        ln=len(newname)
        newname=newname+(20-ln)*' '
        newname=newname.encode()

        pos=0
        found=False
        for i in range(numrec):
            f.seek(pos)
            str=f.read(20)
            if oldname in str:
                print('Updated record No. ', (i+1))
                found=True
                f.seek(-20,1)
                f.write(newname)
            pos+=sizeofrec
        
        if not found:
            print('Name not found')



def delete():
    sizeofrec=20
    size=os.path.getsize('names.dat')
    print(f'Size of file: {size}')

    numrec=int(size/sizeofrec)
    print(f'Number of records: {numrec}')

    f1=open('names.dat', 'rb')
    f2=open('names2.dat', 'wb')

    nm=input('Enter Name to be deleted: ')
    l=len(nm)
    nm=nm+(sizeofrec-l)*' '
    nm=nm.encode()

    pos=0
    found=False
    for i in range(numrec):
        str=f1.read(sizeofrec)
        if str!=nm:
            f2.write(str)
    
    print('Record Deleted')
    f1.close()
    f2.close()
    os.remove('names.dat')
    os.rename('names2.dat', 'names.dat')





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

    

    

