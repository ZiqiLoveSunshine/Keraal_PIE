from pypot.vrep import from_vrep
from poppy_humanoid import PoppyHumanoid
poppy = PoppyHumanoid(simulator='vrep')
def pause():
    programPause = input("Press the <ENTER> key to continue...")
    return

for m in poppy.motors:
    print(m.name)
    m.compliant = False
    m.goal_position = 60
    pause()
