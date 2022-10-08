from posixpath import join
import random

genarate = input("DO you want to generate a unhackeble password (YES/NO) :")

if genarate == "YES":
   upper_case = 'ASDFGHJKLZXCVBNMQWERTYUIOP'
   lower_case = 'asdfghjklzxcvbnmqwertyuiop'
   number  = '1234567890'
   symbol_s = "{}[]*/()$%^&*@m#!"
   all =  upper_case + lower_case + number + symbol_s
   leanght = 9
   password = ''.join(random.sample(all, leanght))
   print("your PASSWORD  is: " + password)
   
   
elif genarate == "NO":
    print("YOU DONT WANT TO GET A STRONGE  PASSWORD")
else:
    print("YOU DONT WANT TO GET A unhackble  PASSWORD")
    

   
   
   









    








