from gardnr import drivers


class Sensor(drivers.Sensor):

    def read(self):
        print('hello world')
