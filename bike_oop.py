class bike(object):

    def __init__(self, brand, color):
        self.brand = 'Bajaj'
        self.color = 'Blue'
        self.on = False


pulsar = bike("Bajaj", "Blue")
print(pulsar.brand)
print(pulsar.color)
print()
pulsar.color = "Red"
print(pulsar.color)
print(pulsar.brand)