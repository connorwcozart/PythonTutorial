import time
import random
import snaps

snaps.display_image("nervesofsteel.jpg")
snaps.display_message("Players Stand.", size=50)
time.sleep(5)
snaps.clear_display

time.sleep(random.randint(5,20))

snaps.display_message("Last player to sit down wins!", size=50)
time.sleep(3)