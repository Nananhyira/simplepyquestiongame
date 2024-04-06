welcome = "WELCOME TO MY SIMPLE GAME!"
print(welcome)
name = input("what is you name? ")
age = input("how are old are you ? ")
print("hello", name, "you are ", age, "years old")
# isOlder = int(age)>=18
# print(isOlder)
health = 10

if int(age) > 18:
  print("you are old enough to play!")
  want_to_play = input("Do you want to pay? ").lower()
  if want_to_play == "yes":
      print("you are statring with ", health, "health")
      print("Let's play!")
      head_or_tale = input("First choice... Head or tale (head/tale)? ")
      if head_or_tale == "tale":
        ans = input(
            "Nice... you followed the path and reached a lake ... Do you swim across or swim around?  (across/around)?").lower()
        if ans == "around":
          print("You went around and reach the other side of the lake")
        elif ans == "across":
          print("you managed to go across but was bitten by a fish and lost five health.")
          health -= 5
        ans = input(
            "you see a house and a river. Which do you go to ? (house/river?) ").lower()
        if ans == "house":
            print( "you went to the house greeted by the owner... he hit you with a log and you loose 5 health")
            health -= 5
            if health <= 0:
              print("you now have ", health, "health and you loose the game .")
            else: print("you survived... You win")
        else: print("you fell in deep river and lost")

      else: print("you lost dumb ass")

  else: print("you can't win a jackpot , you lost...")  
# else:print("you are boring go home")
else: 
  print("you are not old enough to play...")    
