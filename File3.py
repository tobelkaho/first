import csv
import random

print("У вас уже есть аккаунт?")
authOrRegistr = input("1 - да. 2 - нет.")
if authOrRegistr == "1":
    login = input("Логин:")
    password = input("Пароль:")
    allUsers = []
    with open("main.csv","r", encoding="utf-8") as f:
        reader = csv.reader(f)
        allUsers = list(reader)
    for user in allUsers:
        print(user[1])
        if user[0] == login:
            if user[1] == password:
                print(user)

if authOrRegistr == "2":
    login = input("Логин:")
    password = input("Пароль:")
    name = input("Имя:")
    surname = input("Фамилия:")
    patronymic = input("Отчество")
    seriaPassport = str(input("Серия паспорта:"))
    nomerPassport = str(input("Номер паспорта:"))
    dateBirth = str(input("Дата рождения"))
    BankAccount = "S-" + str(random.randint(800000000000,999999999999))
    SumCredit = input("Сумма кредита:")
    SrokCredita = input("Срок кредита(в месяцах):")
    nomerBankAccount = str(random.randint(800000000000,999999999999))
    dataBankAccount = "07/98"
    CVCBankAccount = str(random.randint(100,999))
    CreditCard = str(random.randint(800000000000,999999999999))
    with open("main.csv","a", encoding="utf-8",newline="\n") as f:
        newUser = [login, password, name, surname, patronymic, seriaPassport, nomerPassport, dateBirth, BankAccount, nomerBankAccount, dataBankAccount, CVCBankAccount, CreditCard, SumCredit, SrokCredita]
        writer = csv.writer(f)
        writer.writerow(newUser)