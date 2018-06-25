
class Car:
    def __init__(self):
        self.__updateSoftware__()
        pass
    def drive(self):
        print ('driving')
    def __updateSoftware__(self):
        print ('updating software')
redcar=Car()
redcar.drive()
