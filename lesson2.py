

# a=10
# b=a**3
# print(b)

# a=[1,2,3,4,5]
# for b in a:
#     if b%2==1:
#         print(b)


arr=[]
import random
while True:
    a=int(input('Enter a number: '))
    if a==0:
       arr.append(random.randint(1,100))
    elif a==1:
        print(arr)
    elif a==2:
        break
