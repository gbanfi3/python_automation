class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name}, {self.connected_by}"

    def disconnect(self):
        self.connected = False

printer = Device("laserprinter", "USB")
print(printer)