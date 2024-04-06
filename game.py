welcome ="WELCOME TO MY SIMPLE GAME!"
print(welcome)
name= input("what is you name? ")
age =input("how are old are you ? ")
print("hello" , name , "you are " , age, "years old")
# isOlder = int(age)>=18
# print(isOlder)
if int(age) >18:
   print("you are old enough to play!") 
   want_to_play = input("Do you want to pay? ")
   if want_to_play=="yes":
      print("Let's play!")
   else:print("you are boring go home")

else: 
 print("you are not old enogh to play...")    
