from vpython import *

#constants
RE= #radius of Earth
ME= #mass of Earth
G= #gravitational constant


earth = sphere(pos=vector(0,0,0), 
        radius=RE,     
        color=color.blue, 
        mass=ME)

# implement this! Look at earth for features/arguments
# and decide what is needed for the rocket
rocket = box()

# DONT TOUCH 
rocket.v=vector(0,2e3,0)
rocket.p=vector(0,2e7,0)

t= # initial time
delta_t= # change in time (fps)

while t<1000000:
    rate(300)
    # implement updating position, momentum, and
    # more in here!
    
