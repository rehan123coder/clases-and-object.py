import random 
class fruitquiz:
    def __init__(self):
          self.furit={'apple':'red','orange': 'orange','watermelon':'green','banana':'yellow'}
    def quiz (self):
          while (True):
                  fruit,  colour = random.choice(list(self.fruits.items()))
                  print("whats the colour of {}". format (fruit))
                  user_anwser=input()
                  if(user_anwser.lower()== colour):
                        print("right")
                  else:
                        print("wrong")
                        option = int(input("enter0,if you want to play otherwise enter 1"))    
                        if (option):
                              break
print("welcome to fruitquiz")
fq=fruitquiz()
fq.quiz()
