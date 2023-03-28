from poppy_humanoid import PoppyHumanoid
from pypot.primitive.move import MovePlayer
from pypot.primitive.move import Move


with open('my-first-demo.move') as f:
    my_loaded_move = Move.load(f)

print(len(my_loaded_move.positions()))
print(my_loaded_move.positions())
# poppy = PoppyHumanoid(camera = "dummy")
poppy = PoppyHumanoid(simulator = "vrep")
for m in poppy.motors:
        m.compliant = False
        m.goto_position(0, 0.01, wait=True)
        print(m.name,", initialisation: ", m.present_position)
        # f.write("%s, initialisation: %f\n"%(m.name,m.present_position))  
motors = [poppy.l_shoulder_y, poppy.l_shoulder_x, poppy.l_arm_z, poppy.l_elbow_y]
for m in motors:
    m.compliant = True


print("Robot movement.")
player = MovePlayer(poppy, my_loaded_move)
player.start()
player.wait_to_stop()