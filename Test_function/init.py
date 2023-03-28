from poppy_humanoid import PoppyHumanoid
import time
# poppy = PoppyHumanoid(camera = 'dummy')
for m in poppy.motors:
    time.sleep(0.1)
    m.compliant = True