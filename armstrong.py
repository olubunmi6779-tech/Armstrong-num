num = int(input("Enter a number of your choice: "))

temp = num
sum = 0
n = len(str(num))

while temp > 0:
    digit = temp % 10
    sum = sum + digit ** n
    temp = temp // 10

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")