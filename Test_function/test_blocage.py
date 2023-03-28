from poppy_humanoid import PoppyHumanoid
import time

# if you are using a Humanoid
fichier = "init_motor.txt"
# poppy = PoppyHumanoid(simulator = "vrep")
poppy = PoppyHumanoid(camera = 'dummy')

def pause():
    programPause = input("Press the <ENTER> key to continue...")
    return
with open(fichier,"w+") as f:
    f.write("-------------------------Initialisation---------------------------\n")
    for m in poppy.motors:
        m.compliant = False
        m.goto_position(0, 0.01, wait=True)
        print(m.name,", initialisation: ", m.present_position)
        pause()
        # f.write("%s, initialisation: %f\n"%(m.name,m.present_position))
    print("Fin de l'initialisation")    
    
f.close()
for m in poppy.motors:
    m.compliant = True