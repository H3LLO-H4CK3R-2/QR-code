import pyqrcode as qrcode
import sys
import time
import os
os.system('clear')


print ("###################################################################################")
time.sleep(3)
print ("░██████╗░██████╗░░█████╗░░█████╗░██████╗░███████╗")
print ("██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝")
print ("██║██╗██║██████╔╝██║░░╚═╝██║░░██║██║░░██║█████╗░░")
print ("╚██████╔╝██╔══██╗██║░░██╗██║░░██║██║░░██║██╔══╝░░")
print ("░╚═██╔═╝░██║░░██║╚█████╔╝╚█████╔╝██████╔╝███████╗")
print ("░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═════╝░╚══════╝")
time.sleep(3)
print ("░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░")
print ("██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗")
print ("██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝")
print ("██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗")
print ("╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║")
print ("░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝")
time.sleep(3)
print ("**********************************************************************************")
time.sleep(4)

print ("_______________________________ ")
print ("|  Coded by H3LL0-H4CK3R       |")
print ("|  Thanks for using my tool    |")
print ("|______________________________|")

time.sleep(4)


print (" PROGRAM STARTED ")
time.sleep(3)
def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = spinning_cursor()
for _ in range(50):
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')

print("QRCODE GENERATOR STARTED ")

time.sleep(4)

name = input("Enter your link here : ")
time.sleep(2)

my_qr = qrcode.create(name)

my_qr.png("QRcode.png")
time.sleep(3)

print (" PROGRAM FINISHED ")


