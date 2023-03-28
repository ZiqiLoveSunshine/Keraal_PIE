from poppy_humanoid import PoppyHumanoid
import time

# if you are using a Humanoid
fichier = "test_motor.txt"
# poppy = PoppyHumanoid(simulator = "vrep")
poppy = PoppyHumanoid(camera = 'dummy')

def pause():
    programPause = input("Press the <ENTER> key to continue...")
    return
with open(fichier,"w+") as f:
    f.write("\n-------------------------Test---------------------------\n")
    for i in range (15,len(poppy.motors)):
        m = poppy.motors[i]
        print(m.name)
        m.compliant = False
        pause()
        m.goto_position(0, 0.5, wait=True)
        pause()
        print(m.name,", initialisation: ", m.present_position)
        f.write("%s, initialisation: %f\n"%(m.name,m.present_position))
        pause()
        m.goto_position(180, 0.5, wait=True)
        pause()
        print(m.name,", Angle max: ",m.present_position)
        f.write("%s, Angle max: %f\n"%(m.name,m.present_position))
        pause()
        m.goto_position(-180, 0.5, wait=True)
        pause()
        print(m.name,", Angle min: ",m.present_position)
        f.write("%s, Angle min: %f\n"%(m.name,m.present_position))
        pause()
        m.goto_position(0, 0.5, wait=True)
        pause()
        print(m.name,", retour à l'état initial: ",m.present_position)
        f.write("%s, retour à l'état initial: %f\n"%(m.name,m.present_position))
        
        m.compliant = True
f.close()