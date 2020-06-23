class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name}, {self.connected_by}, {self.connected}"

    def disconnect(self):
        self.connected = False
        print("disconnected")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()}, remaining pages = {self.remaining_pages}"
        # return f"printer vagyok, nevem {self.name}, conn {self.connected_by}, capacity {self.capacity}"

printer = Device("laserprinter", "USB")
print(printer)
printer.disconnect()
print(printer)

princsi = Printer("lazi", "USB", 1000)
print(princsi)