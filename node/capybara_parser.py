import serial
import threading

class CapybaraParser(threading.Thread):

    #SerialPort
    _serialPort=serial.Serial()

    #Capybara reference
    _robot=None

    #Private stuff
    _getCommand=0
    _buffer=""
    _header="$"
    _footer="%"
    _running=1
    #Ctor
    #--------------------------------------------------------------------------------------
    def __init__(self, serialPort, robotInstance):
        
        print "Serial init from inside"
        self._serialPort = serial.Serial(serialPort, 115200)
        self._serialPort.xonxoff = False
        self._serialPort.rtscts = False
        self._serialPort.dsrdtr = False
        self._serialPort.open()
        print "Serial ready"
        self._robot=robotInstance
        super(CapybaraParser, self).__init__()
        self.start()

    #SendCommand
    #--------------------------------------------------------------------------------------
    def sendCommand(self,command):
        self._serialPort.write(command)

    def sendSpeedCommand(self,leftD,rightD,leftSpeed,RightSpeed):
        speedHeader="01"
        fullCommand=self._header+speedHeader+leftD+rightD+leftSpeed+RightSpeed+self._footer 
        self.sendCommand(fullCommand)

    def closeAll(self):
        self._running=0

    #Thread main loop
    #--------------------------------------------------------------------------------------
    def run(self):
        while self._running:
            
            if self._getCommand == 0:
                firstChar = str(self._serialPort.read(1))
                if firstChar == "#":
                    self._getCommand = 1
            if self._getCommand == 1:
                commandChar = str(self._serialPort.read(1))
                if str(commandChar) != '@':
                    self._buffer += commandChar
                if str(commandChar) == "@":
                    SplittedMessage = self._buffer.split(" ");
                    tl=int(SplittedMessage[0])
                    tr=int(SplittedMessage[1])
                    self._robot.serialHandler(tl,tr)
                    self._getCommand=0
                    self._buffer = ""
					