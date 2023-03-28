from poppy_humanoid import PoppyHumanoid

def pause():
    programPause = input("Press the <ENTER> key to continue...")
    return
# poppy = PoppyHumanoid(camera = "dummy")
poppy = PoppyHumanoid(simulator = "vrep")
for m in poppy.motors:
        m.compliant = False
        m.goto_position(0, 0.01, wait=True)
        print(m.name,", initialisation: ", m.present_position)
        # f.write("%s, initialisation: %f\n"%(m.name,m.present_position))  
motors = [poppy.l_shoulder_y, poppy.l_shoulder_x, poppy.l_arm_z, poppy.l_elbow_y]
for m in motors:
    m.goto_position(50, 0.5, wait = True)
    pause()