

from oops2 import zone, car, driver, user
z1 =  zone()

c1 = car("HB 5967","Hyundai", "Aura")
c2 = car("BV 8963", "Toyota", "Etios")

d1 = driver(1, "John", vechile=c1, status='Lunch')
d2 = driver(2, "Stephen", vechile=c2, status='Lunch')
d3 = driver(3, "Rechen", status='Lunch')
d4 = driver(4, "Smith", status='availabel')

u1 = user(1, "Jennifer")
u2 = user(3, "Kryz")

z1.addCars([c1, c2])
z1.addDrivers([d1, d2, d3, d4])
z1.addUsers([u1, u2])

# print(d1.get_details())
# print(d1.accept_ride(u1,dist=10))

# print(d1.complete_ride())
u1.recquest_ride(100,z1)