class bike(object):

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.on = False


pulsar = bike("Bajaj", "Blue")
print(f"Pulsar brand : {pulsar.brand}")
print(f"Pulsar color : {pulsar.color}")
print()
pulsar.color = "Red"
print(f"Pulsar color : {pulsar.color}")
print(f"Pulsar brand : {pulsar.brand}")
print()
classic = bike("RoyalEnfield", "StealthBlack")
print(f"Classic brand : {classic.brand}")
print(f"Classic color : {classic.color}")
print()
pulsar.price = 150 # creating new object for pulsar
print(f"Pulsar price : {pulsar.price}")
classic.price = 180 # creating new object for RE classic
print(f"Royal Enfield Classic price : {classic.price}")

