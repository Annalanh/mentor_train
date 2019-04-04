import math
from random import *
#Python training practice

#Variable
#Write a program that calculates the area of a circle. The circle radius is entered by users
radius = input("Please enter your name: ")
radius = float(radius)
area = str(radius*3.14)
print("Area: "+area)

#Loop

#print 5 - n
end_number = int(input("Please enter the end number: "))
def from_5_to_n(n):
    for i in range(5,n + 1):
        print((i))
from_5_to_n(end_number)

#print 20-10
for i in range(20,9,-1):
    print(i)

#print n-m. n, m is entered by user
n = int(input("Please enter n: "))
m = int(input("Please enter m: "))
for i in range(n, m - 1, -1):
    print(i)

# Fun quiz with four answers. User must choose 1 - 4
right = False
while(right == False):
    print("How many legs does a spider have?\n1. None\n2. 4 legs\n3. 8 legs\n4. 12 legs")
    choice = int(input())
    if(choice != 1 and choice != 2 and choice != 3 and choice != 4):
        print("Your answer:"+str(choice))
        print("The answer must be 1, 2, 3, or 4, enter again:")
    elif choice == 3:
        print("Your answer:"+str(choice))
        print("Right")
        right = True
    else:
        print("Your answer:"+str(choice))
        print("Wrong, the answer is 3: 4 legs")
        right = True

#Conditional

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

delta = b*b - 4*a*c

if delta < 0:
    print("Phuong trinh vo nghiem")
elif delta == 0:
    res1 = float(-(b)/(2*a))
    print("Phuong trinh co 1 nghiem kep: "+ str(res1))
else:
    print("Phuong trinh co 2 nghiem:")
    res2 = float(-b + math.sqrt(delta)/(2*a))
    res3 = float(-b - math.sqrt(delta)/(2*a))
    print("x1 = "+str(res2))
    print("x2 = "+str(res3))

#List

#shuffle a word
word = input("Enter a word: ")
letter_list = list(word)
shuffle(letter_list)
print(letter_list)

#pick a random word in a list. Shuffle its letter.
guess_word_list = ["thao", "quan", "khanh", "my", "trang", "phuong"]

random_word = guess_word_list[randint(0,len(guess_word_list) - 1)]

random_word_letters = list(random_word)
shuffle(random_word_letters)
shuffled_word = "".join(random_word_letters)
print(shuffled_word)

ur_guess_word = input("Please enter your guess word: ")
if (ur_guess_word == random_word):
    print("Right")
else:
    print("Wrong")

#Dictionary



    