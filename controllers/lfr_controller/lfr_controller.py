"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

if __name__ == "__main__":


    # create the Robot instance.
    robot = Robot()
    
    # get the time step of the current world.
    timestep = 32
    max_speed = 7
    
    
    #Created motor instances
    left_motor = robot.getDevice('motor_1')
    right_motor = robot.getDevice('motor_2')
       
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
       
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
   
    left_ir = robot.getDistanceSensor('ir_1')
    left_ir.enable(timestep)
   
    right_ir = robot.getDistanceSensor('ir_2')
    right_ir.enable(timestep)
    
    centre_ir = robot.getDistanceSensor('ir_3')
    centre_ir.enable(timestep)
    
    r_ir = robot.getDistanceSensor('ir_4')
    r_ir.enable(timestep)
    
    l_ir = robot.getDistanceSensor('ir_5')
    l_ir.enable(timestep)
    count = 0
    while robot.step(timestep) != -1:
       #get ir sensor readings
       left_ir_value = left_ir.getValue()
       right_ir_value = right_ir.getValue()
       c = centre_ir.getValue()
       l = l_ir.getValue()
       r = r_ir.getValue()
       right_speed = max_speed
       left_speed = max_speed
        
       print("left: {} right: {} centre: {} wheelleft: {} wheelright: {}".format(left_ir_value,right_ir_value,c,l,r))
       if (count>741):
        right_speed = max_speed
        left_speed = max_speed
        if ((left_ir_value > 400) and (right_ir_value > 400) and (c > 400) and (l > 400) and (r > 400)):  
         left_motor.setVelocity(0)
         right_motor.setVelocity(0)
         break
        
        left_speed = max_speed 
        right_speed = max_speed 
         
       
       elif (((l>400) and (c>400) and (r>400)) or ((l>400) and (r>400)) or ((l>400) and (c>400)) or (l>400)):
        print("Go left")
        left_speed = -max_speed 
        right_speed = max_speed 
        #Go left
       
       elif (((c>400) and (l<400) and (r<400)) or ((c>400) and (r>400))):
        print("Go straight")
        count = count + 1
        if (left_ir_value > right_ir_value) and (400 < left_ir_value < 1000):
           print("Go minor left")
           left_speed = -max_speed * 0.75
           right_speed = max_speed * 0.75   
       elif (right_ir_value > left_ir_value) and (400 < right_ir_value < 1000):
            print("Go minor Right")
            right_speed = -max_speed * 0.75
            left_speed = max_speed * 0.75
      
        #Go straight
       
       elif ((r>400) and (l<400) and (c<400)):
        print("Go Right")
        
        left_speed = max_speed 
        right_speed = -max_speed 
         #Go Right
       
       
       left_motor.setVelocity(left_speed)
       right_motor.setVelocity(right_speed)