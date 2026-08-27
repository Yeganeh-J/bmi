class Student:
    def __init__(self):
        self.name=input("n:")
        self.score=float(input("s:"))

    def show_status(self):
        if self.score >= 12:
            print(self.name,"pass ba:", self.score)
        else:
            print(self.name,"oftad ba:",self.score)
