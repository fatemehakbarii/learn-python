import random
def main():
   level = get_level()
   problem = []
   correct_answer = 0
   for _ in range (10):
       x=generate_integer(level)
       y=generate_integer(level)
       problem.append({"key": f"{x} + {y}=", "value": x + y})
    for problem in problem:
        for j in range(1,4):
            try:
                answer = int(input(problem["key"] + ""))
                if answer == problem["value"]:
                   correct_answer +=1
                   break
                else: 
                    raise ValueError
            except:
                print("EEE")
                if j == 3:
                print(problem["key"], problem["value"])
    print("score: ", correct_answer)            
                      
def get_level():
    while true:
        try:
            level1= int(input("level: "))
            if 1 <= level <= 3:
                return level
        except:
            pass
        
def generate_integer(level):
    if level == 1:
        return random.randrange(0,10)
    else:
        return random.randrange(10**(level -1 ), 10**level)      

          
