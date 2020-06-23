# Magnetic Pendulum Attractor Basin Fractals (Matlab Code)
## Generate colorful representations of the attractor basins of a magnetic pendulum

The program *magnetic_pendulum.m* generates trajectories of a pendulum starting from random positions. the tip of the pendulum is magnetic and gets attracted to (by default) 4 magnets. 
The trajectories end up on top of one of the magnets, over which the pendulum gets trapped. 

<p align="center">
<img src="https://github.com/Ntropic/Physics/blob/master/Magnetic_Pendulum_Attractor_Fractal/trajectory.png?raw=true" width="540" height="304" />
</p>
<p align="center">
*A trajectory created by the script magnetic_pendulum.m*
</p>

The script *attractor_Basin_generator.m* calculates a trajectory for every pixel in an image, where every pixel corresponds to a starting position of the pendulum. By coloring the pixels in a color, corresponding to the magnet over which the trajectory ends, we get a map of the attractor basins for the starting positions.

<p align="center">
<img src="https://github.com/Ntropic/Physics/blob/master/Magnetic_Pendulum_Attractor_Fractal/magnetic_pendulum_attractor_1080_608_0_0_8_0.3_0.1.gif?raw=true" width="540" height="304" />
</p>
<p align="center"> 
*Animation of the attractor basins for a change in strength of the gravitational force, with the parameters: R=0.3 (friction), d=0.1 (inverse measure of strength of the magnets) and C=0.1 to 1.0 (strength of gravity)*
</p>

<p align="center">
<img src="https://github.com/Ntropic/Physics/blob/master/Magnetic_Pendulum_Attractor_Fractal/magnetic_pendulum_attractor_1080_608_0_0_8_0.5_0.1.gif?raw=true" width="540" height="304" />
</p>
<p align="center"> 
*Animation of the attractor basins for a change in strength of the gravitational force, with the parameters: R=0.5 (friction), d=0.1 (inverse measure of strength of the magnets) and C=0.1 to 1.0 (strength of gravity)*
</p>
