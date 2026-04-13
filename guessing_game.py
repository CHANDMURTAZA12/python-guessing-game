import random
‎while True:   
‎
‎    secret=random.randint(1,100)
‎    attempts=7
‎
‎    for i in range(1,attempts+1):
‎    
‎        guess=int(input("Guess a number:"))
‎        remaining=attempts-i
‎    
‎        if guess<secret:
‎            print("too low")
‎            print(f"Attempts remaining {remaining}")
‎        elif guess>secret:
‎            print("Too high")
‎            print(f"Attempts remaining {remaining}")
‎        elif guess==secret:
‎            print(f"{i} Attempts taken")
‎            break
‎    else:
‎        print(f"You fell short of attempts !.Here's the secret {secret}")
‎    playagain=input("play again?(yes/no)")
‎    if playagain!="yes":
‎        print("Good luck!")
‎        break
