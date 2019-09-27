# Day 040 - Introduction to Physics simulation in python

The purpose of this day is to understand some basic physics concepts having to do with orbits and their respective gravitational pull. We will be using

### Physics:

We need to define a few things here. First, for the gravity function to work, we need to know the radius of Earth (6.37e6 m), the mass of the earth (5.97e24 kg - that's heavy!), and the Gravitational constant (6.67e-11). 

Now we look at the actual gravitational force that each one has. Our distance `r` is the position of our orbital object minus our earth position. The force on the orbital object is ((-G* earth mass * OO mass * `r.hat`)/`r.mag`**2). We don't need to understand r.hat and r.mag, just know they are vectors. Now we look at `p`, the OO momentum. This is defined as ((-G * Earth mass * OO mass * `r.hat`)/(`r.mag`) ** 2). The `r.hat` and `r.mag` define vectors from our distance from OO to earth. We next need to update the position of the OO,  which is its previous position + (`p`/OO mass) * `delta_t` (our change in time, which is basically 60 fps for simulating purposes). 

### Your Task:

1. After you finish reading through this guide, visit the documentation to get an understanding how to use things

2. Install all dependencies:
    ```
    pip install vpython 
    https://pip.pypa.io/en/stable/installing/
    ^ if you do not have pip installed on machine
    ```

3. follow the code comments!

Good luck and happy coding!