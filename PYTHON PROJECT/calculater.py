from ast import operator


first_number = int(input("ENTER THE FIRST NUMBER "))
second_number = int(input("ENTER THE SECOND NUMBER "))
operators =  input("enter the operator (+,-,/,*) :")

first_number = int(first_number)
second_number = int(second_number)

if operators == "+" :
    print(first_number + second_number)
elif operators == "-" :
    print(first_number - second_number)
elif operators == "*" :
    print(first_number * second_number)
elif operators == "/" :
    print(first_number / second_number)
else :
    print("Invalid operators")
    


