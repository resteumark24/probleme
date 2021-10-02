import statistics
import listNumbers
my_list = listNumbers.readListFromKeyboard()

result = statistics.mean(i for i in my_list)
print(result)
