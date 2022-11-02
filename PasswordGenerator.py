from sys import exit
import random

def pwdGenerater(lengthy, up, low, special, numbers):
   answer = ""
   listy = []
   if(up):
     listy.append("up") 
   if(low):
     listy.append("low")
   if(special):
     listy.append("special")
   if(numbers):
     listy.append("numbers")
      
   for i in range(0,int(lengthy)):
      randNum = random.randint(0, len(listy)-1)
      
      if(listy[randNum] == 'up'):
         answer += chr(random.randint(65, 90))
      elif(listy[randNum] == 'low'):
         answer += chr(random.randint(97, 122))
      elif(listy[randNum] == 'special'):
         spec = [chr(random.randint(33,47)), chr(random.randint(58,64)), chr(random.randint(91,96)), chr(random.randint(123,126))]
         answer += spec[random.randint(0,3)]
      elif(listy[randNum] == 'numbers'):
         answer += str(random.randint(0,9))
      else:
         answer+= 'no parameters were input'
         break
   return (answer)
#end of pwdGenerater/////////////////////////////////////////

print('Please list your requirements for the password: ')
requirements = input()
pwdLength = 0
uppercase, lowercase, specialChar, digit = False, False, False, False
l1 = requirements.split()

#in this loop I want to check if the list has an interger if so make that the pwd length
#then if it has the other requiremetns in list set parameter to true and implement them into the password

for x in l1:
   if(x.isdigit()):
      pwdLength = x
   elif(x.lower() == 'uppercase'):
      uppercase = True
   elif(x.lower() == 'lowercase'):
      lowercase = True
   elif(x.lower() == 'special' or x.lower() == 'specialcharacter'):
      specialChar = True
   elif(x.lower() == 'digit'):
      digit = True
if(not(lowercase) and not(uppercase) and not(specialChar) and not(digit)):
   print("No parameters were input")
   exit()
   
print(pwdGenerater(pwdLength, uppercase, lowercase, specialChar, digit))     
exit()