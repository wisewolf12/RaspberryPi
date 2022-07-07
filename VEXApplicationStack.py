from bluedot import BlueDot
from gpiozero import Robot
from signal import pause
from gpiozero import Motor
from time import sleep
from bluedot import MockBlueDot


robot = Robot(left = (18,17), right = (22,23))



bd = BlueDot


    
    
def forward():
    robot.forward(0.7)
            
def backward():
    robot.backward(0.7)
            
def left():
    robot.left(0.3)
            
def right():
    robot.right(0.3)
            
bd = BlueDot(cols=3, rows=3)
bd.color = 'gray'
bd.square = True

bd[0,0].visible = False
bd[2,0].visible = False
bd[0,2].visible = False
bd[2,1].visible = False
bd[1,1].visible = False


bd[1,0].when_pressed = forward
bd[1,2].when_pressed = backward
bd[0,1].when_pressed = left
bd[2,1].when_pressed = right
        
#def pos_to_values(x, y):
    #left = y if x > 0 else y + x
    #right = y if x < 0 else y-x
    #return (clamped(left), clamped(right))

#def clamped(v):
    #return max(-1, min(1, v))

#def drive():
    #while True:
        #if bd.is_pressed:
            #x, y = bd.position.x, bd.position.y
            #yield pos_to_values(x, y)
        #else:
            #yield (0, 0)
            
#def swiped(swipe):
    #if swipe.up:
        #robot.forward(4)
    #elif swipe.down:
        #robot.backward(4)
            
#robot.source = drive()
            
def stop():
    robot.stop()
        
#bd.when_pressed = dpad
#bd.when_moved = dpad
bd.when_released = stop
#bd.when_swiped = swiped

#bd = MockBlueDot
#bd.launch_mock_app()
#bd.start()



pause()
