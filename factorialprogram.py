num = int(input("Enter a num to check factorial:"))
# inotialize the factorial value to be 1

factorial = 1
# num+1 represent here to print until the given input

for i in range(1, num + 1):
    factorial = factorial * i
print("the factorial value of", num, 'is', factorial)
