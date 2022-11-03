import string
#zadanie 1
x = int(input('input a whole number: '))
if(x % 3 == 0):
    print('Fizz',end=' ')
if(x % 5 == 0):
    print('Buzz')

#zadanie 2
x = int(input('input a whole number: '))
if(x > 20 and x % 2 == 0):
    print('Otlichno')
elif(x <= 20 and x >= 6 and x % 2 == 0):
    print('Tak sebe')
elif(x >= 2 and x <= 5 and x % 2 == 0):
    print('Ne ploho')
elif(x % 2 == 1):
    print('Ploho')

#zadanie 3
x = int(input('input a whole number from 1 to 9: '))
for i in range(x):
    print(i+1,end='')

#zadanie 4
x = input('\ninput a sentence: ')
for i in x:
    if(i in string.ascii_uppercase):
        print(i,end='')

#zadanie 5
x = input('\ninput a sentence: ')
x = x.split(' ')
WordsInARow = 0
IsWord = True
ThreeInARow = False
for i in x:
    for j in i:
        if(j in string.digits):
            IsWord = False
            break
    if IsWord:
        WordsInARow = WordsInARow + 1
    if WordsInARow == 3:
        ThreeInARow = True
print(ThreeInARow)

#zadanie 6
x = ["left","right","left","stop","bright","alright","enough","jokes"]
output = ""
for i in x:
    if "right" in i:
        i = i.replace("right","left")
    output = output + i + ','
print(output)