import listNumbers
my_list = listNumbers.readListFromKeyboard()

i=0

v = [my_list[i+1]-my_list[i] for i in range(len(my_list)-1)]

print(max(v))

    
