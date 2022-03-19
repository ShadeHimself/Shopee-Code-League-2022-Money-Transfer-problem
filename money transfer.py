
bank={}
data=input('?')
data=list(data.split())
N=int(data[0])
T=int(data[1])
for i in range(N):
    obj=input('Input username and balance')
    list1=list(obj.split())
    bank.update({list1[0]:list1[1]})

for i in range(T):
    trans=input('What is the transaction?')
    trans1=list(trans.split())
    user1=trans1[0]      
    user2=trans1[1]
    amt=trans1[2]
    if int(bank.get(user1))>=int(amt):
        newAmt=int(bank.get(user1))-int(amt)
        bank[user1]=str(newAmt)          #update transactor balance
        newAmt=int(bank.get(user2))+int(amt)
        bank[user2]=str(newAmt)         #update receiver balance

for key, value in bank.items():
    print(key + value)


# 3 4
# amir 10
# brenda 10
# charlie 10
# amir brenda 5
# brenda charlie 5
# charlie amir 20
# charlie amir 7