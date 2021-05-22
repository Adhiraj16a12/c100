class Car (object) : 
    def __init__(self , comfort , speedLimit , brand , color) :
        self.comfort = comfort
        self.speedLimit = speedLimit
        self.brand = brand
        self.color = color
    
    def setStart(self):
        print("started")
    def setStop(self):
        print("stop")

    def setAccelerate(self):
        print("accerlerate")

    def setGear(self):
        print("changed gear")

bmw = Car("good" , 200 , "x3" , "red")
royalce = Car("good" , 100 , "o" , "white")

bmw.setStart()
bmw.setStop()
bmw.color