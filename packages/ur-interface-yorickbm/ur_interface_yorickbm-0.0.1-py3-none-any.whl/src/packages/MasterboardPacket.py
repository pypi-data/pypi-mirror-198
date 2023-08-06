from .Package import Package


class MasterboardPacket(Package):
    def __init__(self):
        self.digitalInputBits = 0
        self.digitalOutputBits = 0
        self.analogInputRange0 = 0
        self.analogInputRange1 = 0
        self.analogInput0 = 0
        self.analogInput1 = 0
        self.analogOutputDomain0 = 0
        self.analogOutputDomain1 = 0
        self.analogOutput0 = 0
        self.analogOutput1 = 0
        self.masterBoardTemperature = 0
        self.robotVoltage48V = 0
        self.robotCurrent = 0
        self.masterIOCurrent = 0
        self.safetyMode = 0
        self.inReducedMode = 0

    def parse(self):
        self.digitalInputBits = super().popInt32()
        self.digitalOutputBits = super().popInt32()
        self.analogInputRange0 = super().popUChar()
        self.analogInputRange1 = super().popUChar()
        self.analogInput0 = super().popDouble()
        self.analogInput1 = super().popDouble()
        self.analogOutputDomain0 = super().popUChar()
        self.analogOutputDomain1 = super().popUChar()
        self.analogOutput0 = super().popDouble()
        self.analogOutput1 = super().popDouble()
        self.masterBoardTemperature = super().popFloat()
        self.robotVoltage48V = super().popFloat()
        self.robotCurrent = super().popFloat()
        self.masterIOCurrent = super().popFloat()
        self.safetyMode = super().popUChar()
        self.inReducedMode = super().popUInt8()
