print('Програма розраховує скільки треба замовити столі для кожної з трьох груп')
while True:
    a=int(input('Введіть кількість дітей у першій групі\n'))
    if a<=0:
        print('Дітей не може бути меньше за 0')
    else:
        break
while True:
    b=int(input('Введіть кількість дітей у другій групі\n'))
    if b<=0:
         print('Дітей не може бути меньше за 0')
    else:
        break
while True:
    c=int(input('Введіть кількість дітей у третій групі\n'))
    if c<=0:
        print('Дітей не може бути меньше за 0')
    else:
        break
print('Необхідно парт для першої групи:',a//2+a%2)
print('Необхідно парт для другої групи:',b//2+b%2)
print('Необхідно парт для третьої групи:',c//2+c%2)
print('Необхідно парт для всіх груп:',(a//2+a%2)+(b//2+b%2)+(c//2+c%2))