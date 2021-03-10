"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """class constructor"""
        self.start = start
        self.current = start

    def __repr__(self):
        """Representation of SerialGenorator Instance"""
        return f"<SerialGenerator (start={self.start} current={self.current})>"
    
    
    def generate(self):
        """Return current as the next serial number"""
        self.current += 1
        return self.current - 1


    def reset(self):
        """Reset the current number to be the start number"""
        self.current = self.start

    
    


