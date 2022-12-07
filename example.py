class student:
    def __init__(self, roll, cgpa):
        self.roll = roll
        self.cgpa = cgpa

    def display(self):
        print(f"roll:{self.roll},cgpa{self.cgpa}")


abc = student("10", "10")
abc.display()
