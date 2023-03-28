from pypot.primitive.move import MoveRecorder
from poppy_humanoid import PoppyHumanoid
from pypot.primitive.move import MovePlayer
from copy import deepcopy

poppy = PoppyHumanoid(camera = "dummy")
for m in poppy.motors:
        m.compliant = False
        m.goto_position(0, 0.01, wait=True)
        print(m.name,", initialisation: ", m.present_position)
        # f.write("%s, initialisation: %f\n"%(m.name,m.present_position))  
motors = [poppy.l_shoulder_y, poppy.l_shoulder_x, poppy.l_arm_z, poppy.l_elbow_y]
for m in motors:
    m.compliant = True
record = MoveRecorder(poppy, 50, motors)
import time
def pause():
    programPause = input("Press the <ENTER> key to continue...")
    return

# Give you time to get ready
print('Get ready to record a move...')
pause()

# Start the record
record.start()
print('Now recording !')

# Wait for 10s so you can record what you want
time.sleep(30)

# Stop the record
print('The record is over!')
record.stop()

pause()
print("write in a document.")
my_recorded_move = deepcopy(record.move)
with open('my-first-demo.move', 'w') as f:
    my_recorded_move.save(f)

print(len(my_recorded_move.positions()))
print(my_recorded_move.positions())

pause()
print("Robot movement.")
player = MovePlayer(poppy, my_recorded_move)
player.start()
player.wait_to_stop()