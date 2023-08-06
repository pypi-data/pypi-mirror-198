from .Package import Package


class RobotModePacket(Package):
    def __init__(self):
        self.timestamp = 0
        self.isConnected = False
        self.isEnabled = False
        self.isPowerOn = False
        self.isEmergencyStopped = False
        self.isProtectiveStopped = False
        self.isProgramRunning = False

    def parse(self):
        self.timestamp = super().popInt64()
        self.isConnected = super().popBool()
        self.isEnabled = super().popBool()
        self.isPowerOn = super().popBool()
        self.isEmergencyStopped = super().popBool()
        self.isProtectiveStopped = super().popBool()
        self.isProgramRunning = super().popBool()