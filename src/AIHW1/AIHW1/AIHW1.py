from random import *

# ths class that handles throwing something off a cliff
class CliffThrow:
    def __init__(self):
        global distance
        distance = 9900

    def throw(self, velocity):
        # distance = v*t +.5a*t^2
        # velocity needs to be 50 to win with distnace 9900
        # I arbitraily chose a time since it doesn't change
        # if you drop something off a cliff or throw it striaght off a cliff with no air resistance
        x = velocity*100+.5*9.8*1000
        if(x==distance):
            # 0 if you made it
            return 0
        elif(x<distance):
            # -1 if you landed before the goal
            return -1
        else:
            # 1 if you landed after the goal
            return 1

class NoMemeoryAgent:

    count = 0
    def __init__(self):
       global game
       game  = CliffThrow()

    def getCount(self):
        return self.count

    #returns how fast tot hrow the ball
    def action(self):
        return randint(1,100)

    def goal(self, x):
        won = False
        if(x == 0):
            won = True
        elif(x > 0):
            print("Threw the ball too far")
        else:                
            print("Threw the ball too short")
        return won

    def play(self):
        won = False
        self.count
        # randomly generates a velocity until it gets it right
        # it randomly choosing how fast to throw the object because
        # it doesn't remember how hard it threw it before
        while(not won):
            play = self.action()
            x = game.throw(play)
            self.count += 1
            won = self.goal(x)
            
        print("You won the game it took "+ str(self.count)+" throws")

class MemeoryAgent:

    count = 0
    memory = 0
    placement = 0

    #initialize game object
    def __init__(self):
        game = CliffThrow()

    def getCount(self):
        return self.count

    #returns how fast to throw the ball based on memory and placement
    def action(self):
        if(self.placement == 0):
            return randint(1,100)
        elif(self.placement == 1):
            return self.memory - 1
        else:
            return self.memory + 1

    #updates the memory and placement variables
    def updateMemory(self, newMemValue,newPlaceValue):
        self.memory = newMemValue
        self.placement = newPlaceValue
    
    def goal(self,x,play):
        won = False
        if (x == 0):
            won = True
        elif (x > 0):
           print("Threw the ball too far need to decrease speed")
           self.updateMemory(play,1)
        else:
           print("Threw the ball too short need to increase speed")
           self.updateMemory(play,-1)
        return won

    #plays the game 
    def play(self):
        won = False
        while (not won):
            #get what we should throw it at 
            #the action function decides this based on memory
            play = self.action()
            x = game.throw(play)
            won = self.goal(x,play)
            self.count += 1
                  
        print("You won the game it took " + str(self.count) + " throws")

def main():
    noMemCount = 0
    memCount = 0
    iterations = 50
    
    #loop through multiple iterations of the game being to played to get average throws per agent
    for x in range(0,iterations):
        print("NO MEM AGENT ------")
        obj = NoMemeoryAgent()
        obj.play()
        noMemCount+=obj.getCount()
        print("MEM AGENT ---------")
        obj = MemeoryAgent()
        obj.play()
        memCount+=obj.getCount()

    print("On averagte the agent with no memory took " + str(noMemCount/iterations) + " throws")
    print("On avearege the agent with memory took " + str(memCount/iterations) + " throws")

main()
