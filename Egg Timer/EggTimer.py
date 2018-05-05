import time
import snaps

#Egg timer program by Connor Cozart V1.0

snaps.display_image('eggs.jpg')
snaps.display_message('Make sure the water is boiling and get ready to drop the egg in!', size=50)
snaps.clear_display
time.sleep(10)
snaps.display_message('On go, drop the egg in.', size=50)
snaps.clear_display
time.sleep(1)
snaps.display_message('1', size=50)
time.sleep(1)
snaps.clear_display
snaps.display_message('2', size=50)
time.sleep(1)
snaps.clear_display
snaps.display_message('3', size=50)
time.sleep(1)
snaps.clear_display
snaps.display_message('GO!')
time.sleep(2)
snaps.clear_display
snaps.display_message('The egg should be in the water', size=50)
time.sleep(30) #Sleeps for a half minute.
snaps.clear_display
snaps.display_message('Only 30 seconds left to go, get that spoon ready!',size=50)#Notify user to 30 seconds remaining. 
time.sleep(30)
snaps.clear_display
snaps.play_sound('ding.wav')
snaps.display_message("Fish that egg out and enjoy. But don't forget to let it cool!", size=50)
