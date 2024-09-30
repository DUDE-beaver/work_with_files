from random import randint

size=int(input("Hajmini kiriting: "))

list=[]
pos_list=[]
neg_list=[]
for steps in range(size):
    list.append(randint(-50,51))

print()
print(f"Kirish: {list}")    
for value in list:
    if value>0:
        pos_list.append(str(value))
        pos_list.append(" ")
    elif value<0:
        neg_list.append(str(value))
        neg_list.append(" ")
    
with open("musbat.txt", "w") as file:
    file.writelines(pos_list)
    
with open("manfiy.txt", "w") as file:
    file.writelines(neg_list)