import statistics
import listNumbers
my_list = listNumbers.readListFromKeyboard()

result = statistics.mean(i for i in my_list if i % 2 == 0)
print(result)
