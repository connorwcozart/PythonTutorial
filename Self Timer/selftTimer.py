import time
import random
import snaps

snaps.display_message("Players stand", size=50,)
time.sleep(3)
snaps.clear_display

time_standing = random.randint(5,20)

snaps.display_message("Time to remain standing is... ")
time.sleep(5)
snaps.display_message(time_standing)
time.sleep(3)
snaps.clear_display
snaps.display_message("Sit When you would like.")
time.sleep(time_standing)
snaps.display_message("Last person to sit wins!")
time.sleep(5)