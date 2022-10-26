from random import randint
#zadanie 1
a = randint(0,100)
b = randint(0,100)
c = randint(0,100)
print(f"({a} + {b} + {c})/3 = {(a+b+c)/3:.2f}")

#zadanie 2
a = randint(0,100)
b = randint(0,100)
print(f'{a}//{b}={a//b}, {a}%{b}={a % b}')

#zadanie 3
#f = float(input('input a floating point number: '))
#print(f'1){round(f,2)} 2){round(f)} 3){f:=011}')

#zadanie 4 + 5
x = int(input('input a whole number: '))
y = 0
if(x < 2**31 and x > -2**31):
    IsNeg = False
    if(x<0):
        IsNeg = True
        x = -x
    for i in range(len(str(x))):
        y = y * 10 + int(x) % 10
        x = int(x) // 10
    if(IsNeg):
        y *= -1
print(y)