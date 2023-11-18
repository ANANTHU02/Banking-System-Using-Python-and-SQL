import mysql.connector
mydb = mysql.connector.connect(host = 'localhost', user = 'root', password ='Cananthu77@', database ='bank')

def Open_Account():
    n = input("Eneter the name: ")
    acc = input("Enter the account number")
    dob = input("Enter the date of birth: ")
    add = input("Enter the address: ")
    ph = int(input("Enter the phone number: "))
    ob = int(input("Enter the opening balance: "))
    data1 = (n, acc, dob, add, ph, ob)
    data2 = (n, acc, ob)
    sql1 = ('insert into ACCOUNT values(%s,%s,%s,%s,%s,%s)')
    sql2 = ('insert into AMOUNT values(%s,%s,%s)')
    x = mydb.cursor()
    x.execute(sql1, data1)
    x.execute(sql2, data2)
    mydb.commit()
    print("Data Entered Successfully")
    main()

'''def Deposit():
    acc = input("Enter the account number: ")
    amnt = int(input("Enter the amount for deposit: "))
    a = 'select BALANCE from amount where ACC_NO=%s'
    data =(acc,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0]+amnt
    sql = ('update amount set balance where ACC_NO=%s')
    d = (t, acc)
    x.execute(sql,d)
    mydb.commit()
    main()'''


def Deposit():
    acc = input("Enter the account number: ")
    amnt = int(input("Enter the amount for deposit: "))

    a = 'SELECT balance FROM amount WHERE ACC_NO=%s'
    data = (acc,)

    x = mydb.cursor()
    x.execute(a, data)

    result = x.fetchone()

    if result is not None:
        current_balance = result[0]
        new_balance = current_balance + amnt

        sql = 'UPDATE amount SET balance = %s WHERE ACC_NO = %s'
        d = (new_balance, acc)

        x.execute(sql, d)
        mydb.commit()
        print("Amount deposited successfully. New balance:", new_balance)
    else:
        print("Account not found.")

    main()


def Withdraw():
    acc = input("Enter the account number: ")
    amnt = int(input("Enter the amount for withdraw: "))
    a = 'select balance from amount where ACC_NO=%s'
    data = (acc,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    t = result[0] - amnt
    sql = ('update amount set balance where ACC_NO=%s')
    d = (t, acc)
    x.execute(sql, d)
    mydb.commit()
    main()


def Balance():
    acc = input("Enter the account number: ")
    a = 'select * from AMOUNT where ACC_NO=%s'
    data = (acc,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    print("Balance for account: ",acc," is ",result[-1])
    main()


'''def Cust_Details():
    acc = input("Enter the account number: ")
    a = 'select * from ACCOUNT where ACC_N0=%s'
    data = (acc,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()
    for i in result:
        print(i)
    main()'''


def Cust_Details():
    acc = input("Enter the account number: ")
    a = 'SELECT * FROM ACCOUNT WHERE ACC_NO=%s'
    data = (acc,)
    x = mydb.cursor()
    x.execute(a, data)
    result = x.fetchone()

    if result:
        for i in result:
            print(i)
    else:
        print("Account not found.")

    main()


def main():
    print('''
               BANK OF INDIA
            1. OPEN AN ACCOUNT
            2. DEPOSIT AMOUNT
            3. WITHDRAW AMOUNT
            4. BALANCE ENQUIRY
            5. CUSTOMER DETAILS''')
    choice = int(input("Enter the choice: "))

    if choice == 1:
        Open_Account()
    elif choice == 2:
        Deposit()
    elif choice == 3:
        Withdraw()
    elif choice == 4:
        Balance()
    elif choice == 5:
        Cust_Details()
    else:
        print("INVALID CHOICE")
main()
