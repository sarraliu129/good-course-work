# while loop
# increase variable
#use draw() for animation
import time
def setup():
    size (640, 480)

x = 0
y = 0
z = 0

def setup():
    size(640, 480)


def draw():
    global x
    global y
    global z
    noStroke()
   
    if y < 480:
         background(100 + y , 80 + y , 0)
         y += 0.5
         fill(255, 255, 25)
         ellipse(width/2, 350 - y, 70, 70)
         
    if y > 480:
        z += 5
        background(200 - z, 255, 255)
        
    fill(0, 30, 179)
    rect(0, 350, 700 , 250)

    if x >= 640:
        x = 0
    x += 1
    fill(250, 250, 250)
    ellipse(x, height / 5, 50 , 50 )
    ellipse (x + 35, height / 5 , 70 , 50)
    ellipse (x - 35, height / 5 + 15, 65, 50 )
    ellipse (x - 10, height / 5 - 15, 65, 50 )
    ellipse (x, height / 5, 50, 50)
    
    
    
    
         

    
    
