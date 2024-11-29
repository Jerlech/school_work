import csv
import tabulate
import os


def create():
    with open('inventory.csv', mode='a', newline='') as csf:
        mywriter=csv.writer(csf, delimiter=',')
        ans='y'
        while ans.lower()=='y':
            product=input('Enter Product Name: ')
            quantity=int(input('Enter Quantity in stock: '))
            price=int(input('Enter Price(per unit): '))
            mywriter.writerow([product, quantity, price])
            print('Data Saved...')
            ans=input('Do you want to add more?(y/n) ')

def display():
    headers=['Product Name', 'Quantity', 'Price']
    dat=[]
    with open('inventory.csv') as csf:
        myreader=csv.reader(csf, delimiter=',')
        for i in myreader:
            dat.append(i)

        tab=tabulate.tabulate(dat, headers, tablefmt='fancy_outline', stralign="center")
        print(tab)


def search():
    headers=['Product Name', 'Quantity', 'Price']
    datmain=[]
    dat=[]
    with open('inventory.csv') as csf:
        myreader=csv.reader(csf, delimiter=',')

        
        records=list(myreader)
        ans='y'
        while ans.lower()=='y':
            found=False
            print(records)
            sear=input('Enter Product Name to Search: ')
            for i in records:
                #print(i)
                
                if len(i)!=0:
                    #print(i)
                    
                    if i[0]==sear:
                        #print(i)
                        
                        dat.extend([i[0], i[1], i[2]])
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
    with open('inventory.csv', 'r') as csf:
        myreader=csv.reader(csf, delimiter=',')
        records=list(myreader)
        print(records)
        modi=input('Enter Product Name to be modified: ')
        for i in records:
            if len(i)!=0:
                if i[0]==modi:
                    while True:
                        print('''What do you want to modify?
                            1. Quantity
                            2. Price
                            3. Exit''')
                        ch=int(input('Enter you choice: '))
                        if ch==1:
                            quan=int(input('Enter new Quantity: '))
                            i[1]=quan

                        elif ch==2:
                            price=input('Enter New Price: ')
                            i[2]=price

                        elif ch==3:
                            print('Exiting modify mode....')
                            break

                        else:
                            print('Invalid Choice')

        

    with open('inventory2.csv', mode='a', newline='') as csf1:
        mywriter=csv.writer(csf1, delimiter=',')
        for i in records:
            mywriter.writerow(i)
        print('Data Saved...')


    os.remove('inventory.csv')
    os.rename('inventory2.csv', 'inventory.csv')





def delete():
    with open('inventory.csv', 'r') as csf:
        myreader=csv.reader(csf, delimiter=',')
        records=list(myreader)
        print(records)
        dele=input('Enter Product name to be deleted: ')
        found=False
        for i in records:
            if len(i)!=0:
                if i[0]==dele:
                    records.remove(i)
                    found=True

        if not found:
            print('Employee not found...')




    with open('inventory2.csv', mode='a', newline='') as csf1:
        mywriter=csv.writer(csf1, delimiter=',')
        for i in records:
            mywriter.writerow(i)


    os.remove('inventory.csv')
    os.rename('inventory2.csv', 'inventory.csv')






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


        