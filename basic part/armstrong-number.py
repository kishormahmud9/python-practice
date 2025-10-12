# method 1 
# a = int(input("enter to check armstrong number: "))
# num_length = len(str(a))
# temp = a
# sum = 0

# while temp>0:
#     last_digit = temp%10
#     sum = sum + last_digit ** num_length
#     temp //= 10
# if sum == a:
#     print("this is armstrong number")
# else:
#     print("this is not armstrong number")


# method 2 
a = input()
num_len = len(a)
sum = 0
for i in a:
    sum += int(i) ** num_len
if int(a) == sum:
    print("armstrong")
else:
    print("not armstrong")