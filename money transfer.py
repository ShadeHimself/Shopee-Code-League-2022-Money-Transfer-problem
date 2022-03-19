

bank={}
data=input('?')
data=list(data.split())
N=data[0]
T=data[1]
for i in N:
    obj=input('Input username and balance')
    list1=list(obj.split())
    bank.update({list1[0]:list1[1]})

for i in T:
    trans=input('What is the transaction?')
    trans=list(trans.split())
    user1=trans(0)      
    user2=trans(1)
    amt=trans(2)
    newAmt=bank.get(user1)-amt
    bank[user1]=newAmt          #update transactor balance
    newAmt=bank.get(user2)+amt
    bank[user2]=newAmt          #update receiver balance

for key, value in bank:
    print(key + value)


# 3 4
# amir 10
# brenda 10
# charlie 10
# amir brenda 5
# brenda charlie 5
# charlie amir 20
# charlie amir 7