count=0
sum_digits=0
list=[]
while num>0:
    list.append(num%10)
    num//=10
    count+=1

list.reverse()
for index in range(count):
    if list[index]==0:
        list[index]=7
    elif list[index]==1:
        list[index]=8
    elif list[index]==2:
        list[index]=9
    elif list[index]==3:
        list[index]=0
    elif list[index]==4:
        list[index]=1
    elif list[index]==5:
        list[index]=2
    elif list[index]==6:
        list[index]=3
    elif list[index]==7:
        list[index]=4
    elif list[index]==8:
        list[index]=5
    elif list[index]==9:
        list[index]=6

size=count
print()
for index in range(size):
    count-=1
    sum_digits+=list[index]*(10**count)
            
print(f"Chiqish: {sum_digits}")