import Particle_Swarm
import setting

MyCalculate = Particle_Swarm.Particle_Swarm()

while MyCalculate.iteration_time < setting.MAX_ITERATION:
    MyCalculate.compute_once()
