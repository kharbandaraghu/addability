import braille
import time
usbport = '/dev/tty.usbmodem141101'

a = braille.braille(90,30,97,37,90,30,90,150,90,157,100,167,usbport,[1,2,3,4,5,6])

a.AllUp()
time.sleep(2)
a.AllDown()
time.sleep(1)

# a.WriteStr('Hello Rags')

