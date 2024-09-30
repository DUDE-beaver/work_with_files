from random import randint

list=[]
for steps in range(100):
    list.append(randint(100,1000))

print(list)
random_i=randint(0,99)
print()
print("Chiqish: ", end=" ")
for index in range(random_i+1,100):
    if list[index]%2==0:
        print(list[index], end=" ")