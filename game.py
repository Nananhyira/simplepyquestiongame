welcome ="WELCOME TO MY SIMPLE GAME!"
print(welcome)
name= input("what is you name? ")
age =input("how are old are you ? ")
print("hello" , name , "you are " , age, "years old")
# isOlder = int(age)>=18
# print(isOlder)
health =10

if int(age) >18:
   print("you are old enough to play!") 
   want_to_play = input("Do you want to pay? ").lower()
   if want_to_play=="yes":
      print("you are statring with ", health, "health")
      print("Let's play!")
      head_or_tale= input("First choice... Head or tale (head/tale)? ")
      if head_or_tale=="tale":
        ans=input("Nice... you followed the path and reached a lake ... Do you swim across or swim around?  (across/around)?").lower()
        if ans =="around":
          print("You went around and reach the other side of the lake")

        elif ans =="across": 
           print("you managed to go accross but was bitten by a fish and lost five health.")
           health -= 5
        else:print("you lost dumb ass")
      else: print("you can't win a jackpot , you lost...")
      
   else:print("you are boring go home")

else: 
 print("you are not old enogh to play...")    
