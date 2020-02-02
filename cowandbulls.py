import random

def digit_num():
    number = random.randint(1000,9999)
    return number

def cowsandbulls(number):
    number1 = list(str(number))
    number2 = list(str(digit_num()))
    cow = 0
    bull = 0
    while number1 != number2:
        for i in range(0,4):
            if number1[i] == number2[i]:
                cow += 1
            else:
                for j in range(0,4):
                    if number1[i] == number2[j]:
                        bull += 1
        print("cow: %s" % cow)
        print("bull: %s" % bull)
        cow = 0
        bull = 0
        number1 = input("")
        if number1 == 'exit':
            exit()
        number1 = list(number1)
        if len(number1) != 4:
            while len(number1) != 4:
                number1 = input("Only 4 digit caracters: ")
                if number1 == 'exit':
                    exit()
                number1 = list(str(number1))            
    if number1 == number2:
        return("Congratulation!")
    else:
        return("Error! Sorry, try again.")

number = input("Type a 4 Digit Number: ")
while len(number) != 4:
    number = input("Only 4 digit caracters:")
    if number == 'exit':
        exit()
print(cowsandbulls(number))