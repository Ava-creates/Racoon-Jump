
RESX=400
RESY=800
import random
import os
path=os.getcwd()


class Racoon:
  def __init__(self):
      self.x = 35
      self.vx = 0
      self.y = 800
      self.r = 35
      self.w=100
      self.h=70
      self.vy = 0
      self.img = loadImage(path + "/images/" + "mario.png")

      self.frame = 0
      self.img_total = 11
      
      self.direction = RIGHT 
      self.key_handle = {"SPACE":False}
  
  def switch_dir(self):
      if(self.key_handle["SPACE"] == True):
    
        
        if(self.direction == RIGHT):
            self.direction = LEFT
            self.x = RESX - self.x
                
        else: 
            self.direction = RIGHT
            self.x = RESX - self.x
  
  def display(self): 
    self.up()
    if(self.y<=RESY//2):
      game.y_shift-=self.vy

    if self.direction == RIGHT:
            image(self.img, self.x - self.w//2 , self.y - self.h//2 - game.y_shift , self.w, self.h, self.frame * self.h, 0, (self.frame + 1) * self.w, self.h)
    elif self.direction == LEFT:
            image(self.img, self.x - self.w//2 , self.y - self.h//2 - game.y_shift , self.w, self.h, (self.frame + 1) * self.w, 0, self.frame * self.w, self.h)
  
  def distance(self, other):
    distance = ((self.x - other.x) ** 2 + (self.y - other.y - game.y_shift) ** 2) ** 0.5
    return(distance)
    
  def contact(self, other):
    d=self.distance(other)
    if(d <= self.r + other.r):
      return True
      
    return False
    
  def up(self):
    self.y-=self.vy
    
    if(self.y%100 == 0):         
      self.vy += 0.1
      
      
class Coin:
  def __init__(self, y, dire):
      
      self.y=y
      self.img=loadImage(path+"/images/coin.jpg")
      self.r=10
      self.w=10
      self.h=10
      
      if dire == "LEFT":
        self.x=  35#fix later
      
      else: 
        self.x = RESX - 35

  #def changedir(self):
      #if(game.coin[len(game.coin)-2].dir=="LEFT"):
      #self.dir=="RIGHT" 
        
  def scoreupdate(self): #ADD MUSIC 
      if(game.racoon.contact(self)==True):
        game.score+=100
        game.coin.pop()
        
  def display(self):
      self.scoreupdate()
      image(self.img, self.x, self.y - game.y_shift, self.w, self.h)
      
      
  
class Coconut:

    def __init__(self):
        self.y=0
        self.img= loadImage(path+"/images/coin.jpg")
        directions=["LEFT","RIGHT"]
        self.dir= random.choice(directions)
        if self.dir == "LEFT":
            self.x= 35#fix later
      
        else: 
            self.x = RESX - 35
      
        self.r=10
        self.w=10
        self.h=10
    
    def gravity(self):
      if(self.y+self.r<=RESY):
        self.y+=1
        
  
    def lifereduction(self):
      if(game.racoon.contact(self)==True):
        game.life-=1
    
    def display(self):
      image(self.img, self.x, self.y, self.w, self.h)
      self.lifereduction()
      self.gravity()
      
    
    def change(self):
      self.y=0
      directions=["LEFT","RIGHT"]
      self.dir= random.choice(directions)
      if self.dir == "LEFT":
        self.x= 35#fix later
      
      else: 
        self.x = RESX - 35     
    
    def onground(self):
      if(self.y + self.r >= RESY):
        return True
      return False
    

class Game():
  
  def __init__(self):
    self.racoon=Racoon()
    self.score = 0
    self.life = 3
    self.coin = []
    n=1
    
    for i in range(0, 2000, 50):
      if(n%2 == 0): 
        self.coin.append(Coin(i,"RIGHT"))
        n+=1
      
      else:
        self.coin.append(Coin(i,"LEFT"))
      n+=1
      
    self.coco=Coconut()
                          
    self.bg2=loadImage(path+"/images/background.JPG")
    self.bg1=loadImage(path+"/images/trees.PNG")
    self.bg1y=0
    self.bg2y=0
    self.y_shift=0
                             

  #def addCoconuts(self):
   # if(self.racoon.y%100==0):
     # coco.append(Coconut())
      
  def display(self):   
      if(self.life==0):
        background(255)
        text("Game over")
        noLoop()
      image(self.bg2,0, 0,RESX,RESY, 0, self.bg2y, RESX, RESY+self.bg2y)
      image(self.bg1,0, 0,RESX,RESY, 0, self.bg1y, RESX, RESY)

      self.bg2y+=1
      self.racoon.display()
      
      for i in self.coin:
        i.display()
                             
      if(self.racoon.contact(self.coco)==True or self.coco.onground()==True):
        
        self.coco.change()
        
      self.coco.display()
      
      fill(0)
      textSize(15)
      text("Score: "+str(self.score), 785, 0)
      
      text("Life: "+str(self.life),0,0)
      
      self.y_shift+=1
      
      
game=Game()
def setup():
    size(RESX,RESY)
  
def draw():
    background(250)
    game.display()
    
def keyPressed():
    if(keyCode == UP):
      game.racoon.key_handle["SPACE"] = True
      game.racoon.switch_dir()
  
def keyReleased():
    if(keyCode == UP):
      game.racoon.key_handle["SPACE"] = False
      
      
      
      
      
      
      
        
      
      
          
      
                             
    
    
     
    
    
      

        
    
    
        
      
  

  
        
        

        
    
    
    
        
  
        
  
      
  
  
  
  
  
  
