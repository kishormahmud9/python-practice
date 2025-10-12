a = int(input())
reve = 0
while a>0:
    last_digit = a%10
    reve = reve * 10 + last_digit
    a //= 10
print(reve)