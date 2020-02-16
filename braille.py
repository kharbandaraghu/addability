import serial
import time
import struct
# Assign Arduino's serial port address
#   Windows example
#     usbport = 'COM3'
#   Linux example
#     usbport = '/dev/ttyUSB0'
#   MacOSX example
#     usbport = '/dev/tty.usbserial-FTALLOK2'
# basically just see what ports are open  - >>> ls /dev/tty*

class braille:
    
    def __init__(self,tlu=30,tld=0,mlu=30,mld=0,blu=30,bld=0,tru=30,trd=0,mru=30,mrd=0,bru=30,brd=0,usbport = '/dev/ttyS3',servo_ports=[0,1,2,3,4,5]):

        # command variables for up and down state of servos
        self.tlu = tlu
        self.tld = tld
        self.mlu = mlu
        self.mld = mld
        self.blu = blu
        self.bld = bld
        self.tru = tru
        self.trd = trd
        self.mru = mru
        self.mrd = mrd
        self.bru = bru
        self.brd = brd

        # servo ports
        self.servo_ports = servo_ports

        # creating braille array
        # the order follows conventional numbering
        brailleDict = {
            'A':[1,0,0,0,0,0],
            'B':[1,1,0,0,0,0],
            'C':[1,0,0,1,0,0],
            'D':[1,0,0,1,1,0],
            'E':[1,0,0,0,1,0],
            'F':[1,1,0,1,0,0],
            'G':[1,1,0,1,1,0],
            'H':[1,1,0,0,1,0],
            'I':[0,1,0,1,0,0],
            'J':[0,1,0,1,1,0],
            'K':[1,0,1,0,0,0],
            'L':[1,1,1,0,0,0],
            'M':[1,0,1,1,0,0],
            'N':[1,0,1,1,1,0],
            'O':[1,0,1,0,1,0],
            'P':[1,1,1,1,0,0],
            'Q':[1,1,1,1,1,0],
            'R':[1,1,1,0,1,0],
            'S':[0,1,1,1,0,0],
            'T':[0,1,1,1,1,0],
            'U':[1,0,1,0,0,1],
            'V':[1,1,1,0,0,1],
            'W':[0,1,0,1,1,1],
            'X':[1,0,1,1,0,1],
            'Y':[1,0,1,1,1,1],
            'Z':[1,0,1,0,1,1],
            '#':[0,0,1,1,1,1],
            '0':[1,0,0,0,0,0],
            '1':[1,1,0,0,0,0],
            '2':[1,0,0,1,0,0],
            '3':[1,0,0,1,1,0],
            '4':[1,0,0,0,1,0],
            '5':[1,1,0,1,0,0],
            '6':[1,1,0,1,1,0],
            '7':[1,1,0,0,1,0],
            '8':[0,1,0,1,0,0],
            '9':[0,1,0,1,1,0],
            '*':[0,0,0,0,0,0],
            'ALLUP':[1,1,1,1,1,1],
            'ALLDOWN':[0,0,0,0,0,0]
       }

        # Replace the numbers with braille up and down positions
        for key in brailleDict:
            if brailleDict[key][0] == 0:
                brailleDict[key][0] = self.tld
            else:
                brailleDict[key][0] = self.tlu
            
            if brailleDict[key][1] == 0:
                brailleDict[key][1] = self.mld
            else:
                brailleDict[key][1] = self.mlu

            if brailleDict[key][2] == 0:
                brailleDict[key][2] = self.bld
            else:
                brailleDict[key][2] = self.blu

            if brailleDict[key][3] == 0:
                brailleDict[key][3] = self.trd
            else:
                brailleDict[key][3] = self.tru
            
            if brailleDict[key][4] == 0:
                brailleDict[key][4] = self.mrd
            else:
                brailleDict[key][4] = self.mru

            if brailleDict[key][5] == 0:
                brailleDict[key][5] = self.brd
            else:
                brailleDict[key][5] = self.bru
        
        self.brailleDict = brailleDict
        print(brailleDict)

        # initialize serial port
        self.ser = serial.Serial(usbport,9600,timeout=1)
        # time.sleep is necessary - it takes some time to open serial port
        time.sleep(2)


    # function to write character
    def WriteChar(self,mychar):
        mychar = mychar.upper()
        print(mychar)
        if mychar in self.brailleDict:
            print('found - sending...')
            self.ser.write(struct.pack('>BBB',255,self.servo_ports[0],self.brailleDict[mychar][0]))
            self.ser.write(struct.pack('>BBB',255,self.servo_ports[1],self.brailleDict[mychar][1]))
            self.ser.write(struct.pack('>BBB',255,self.servo_ports[2],self.brailleDict[mychar][2]))
            self.ser.write(struct.pack('>BBB',255,self.servo_ports[3],self.brailleDict[mychar][3]))
            self.ser.write(struct.pack('>BBB',255,self.servo_ports[4],self.brailleDict[mychar][4]))
            self.ser.write(struct.pack('>BBB',255,self.servo_ports[5],self.brailleDict[mychar][5]))
        else:
            pass

    def AllUp(self):
        self.WriteChar('allup')
    def AllDown(self):
        self.WriteChar('alldown')

    # writing strings
    def WriteStr(self,mystr):
        # struing preprocessing
        mystr = mystr.replace(' ','*')
        for ch in mystr:
            print('sending '+ch)
            self.WriteChar(ch)
            time.sleep(0.5)



    
