from random import randint

list=[]
for steps in range(1000):
    list.append(randint(1,1000000))

print(list)
random_i=randint(0,999)
print()
print("Chiqish: ", end=" ")
for index in range(random_i+1,1000):
    if list[index]==2:
        print(list[index], end=" ")
    for value in range(2,list[index]):
        if list[index]%value==0:
            break
        else:
            if value==list[index]-1:
                print(list[index], end=" ")