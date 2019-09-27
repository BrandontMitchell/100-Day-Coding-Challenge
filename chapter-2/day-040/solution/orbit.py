#pip install vpython
# GlowScript 2.6 VPython
# https://www.glowscript.org/#/user/bmitchell0919/folder/Public/program/HW03-P65b/edit
from vpython import *
#constants
RE=6.378e6 #radius of Earth
ME=5.97e24 #mass of Earth
G=6.67e-11 #gravitational constant


earth = sphere(pos=vector(0,0,0), 
        radius=RE,     
        color=color.blue, 
        mass=ME)

rocket = box(pos=vector(-10*RE,0,0),  
            size=vector(10e5,20e5,10e5), 
            color=color.white,
            mass=15000,
            velocity=vector(0,2e3,0),
            make_trail=True)
            
rocket.v=vector(0,2e3,0)
rocket.p=vector(0,2e7,0)

t=0
delta_t=60

while t<1000000:
    rate(300)
    r=rocket.pos-earth.pos
    rocket.force=((-G)*earth.mass*rocket.mass*r.hat)/((r.mag)**2)
    rocket.p=rocket.p+rocket.force*delta_t
    rocket.pos=rocket.pos+(rocket.p/rocket.mass)*delta_t
    t=t+delta_t
    
