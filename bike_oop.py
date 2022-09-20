class bike(object):

    fuel_type = "Petrol" # can be similar to like static field in java

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.on = False


pulsar = bike("Bajaj", "Blue") # 1st Object
print(f"Pulsar brand : {pulsar.brand}")
print(f"Pulsar color : {pulsar.color}")
print()
pulsar.color = "Red"
print(f"Pulsar color : {pulsar.color}")
print(f"Pulsar brand : {pulsar.brand}")
print()
classic = bike("RoyalEnfield", "StealthBlack") # 2nd Object
print(f"Classic brand : {classic.brand}")
print(f"Classic color : {classic.color}")
print()
pulsar.price = 150 # creating new object for pulsar
print(f"Pulsar price : {pulsar.price}")
classic.price = 180 # creating new object for RE classic
print(f"Royal Enfield Classic price : {classic.price}")
print()
print(f"bike fuel type : {bike.fuel_type}")
print(f"pulsar fuel type : {pulsar.fuel_type}")
print(f"RE clasic fuel type : {classic.fuel_type}")
print()
bike.fuel_type="Diesel"
print(f"bike fuel type : {bike.fuel_type}")
print(f"pulsar fuel type : {pulsar.fuel_type}")
print(f"RE clasic fuel type : {classic.fuel_type}")
print()
pulsar.fuel_type="Petrol" # in java accessing static variable through instance variable will give warning but not in python
print(f"bike fuel type : {bike.fuel_type}")
print(f"pulsar fuel type : {pulsar.fuel_type}")
print(f"RE clasic fuel type : {classic.fuel_type}")
print()
print("Namespaces : ")
print(f"bike class Namespaces : {bike.__dict__}")
print(f"pulsar object Namespaces : {pulsar.__dict__}")
print(f"RE clasic object Namespaces : {classic.__dict__}")



