#print(f"Hello {input('Input FIO: ')}, you just delved into python! Great start!")#zadanie 1 xD

from math import floor
from turtle import title


thickness = 5
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness - 1) + c + (c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

#zadanie 3
#print(f"{input('input string: ')}".title())

#zadanie 4
#print('{0:,}'.format(float('{0:.2f}'.format(float(input('Input a value: '))))))

#zadanie 5
H = int(input('input a whole number: '))
W = 3 * H
c = ".|."
for i in range(floor(H/2)):
    print('-'*floor((W - 3*(2*i+1))/2) + c + c * i * 2 + '-'*floor((W - 3*(2*i+1))/2))

print('-'*floor((W - 7)/2)+ 'WELCOME'+'-'*floor((W - 7)/2))

for i in range(floor(H/2)):
    print('-'*floor((W - 3*(2*(floor(H/2) - i)-1))/2) + c * ((floor(H/2) - i) * 2 - 1) + '-'*floor((W - 3*(2*(floor(H/2) - i)-1))/2))

#zadanie 6
value = input('input a value: ')
product = 1
for i in range(len(value)):
    if(int(value[i]) != 0):
        product *= int(value[i])
print(product)