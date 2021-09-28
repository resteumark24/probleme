# sa se gaseasca maximul din lista

l=[]
num = int(input("How many numbers: "))
for i in range(num):
   number = int(input("Enter number: "))
   l.append(number)
print("Cel mai mare numar este:", max(l))

