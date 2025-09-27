#vechile
#driver
#user

class zone:

    def __init__(self):
        self.drivers =[]
        self.cars = []
        self.users = []

    def addDrivers(self, drivers_list):
        self.drivers.append(drivers_list)
        print('Drivers are added to zone')
   
    def addCars(self,cars_list):
        self.cars.append(cars_list)
        print('Cars are added to the zone')
    
    def addUsers(self, users_list):
        self.users.append(users_list)
        print('the Users in this zone')
    def getDrivers(self):
        return self.drivers

class car:
    
    def __init__(self,plate,model,condition):
        self.plate=plate
        self.model=model
        self.fuel_percentage= 70
        self.condition=condition
        
    def getdetails(self):
        return f'number plate: {self.plate}, car model: {self.model}, fuel percentage: {self.fuel_percentage}, condition: {self.condition}'

class driver:
    def __init__(self,id, driver,vechile=None, status='Availabel'):
        self.id=id
        self.driver=driver
        self.status = status
        self.history=[]
        self.location=None
    def get_driver(self):
        return self.id, self.driver, self.status, 
    def get_history(self):
        print(self.history)
    def get_details(self):
        return f'Name: {self.driver}, status: {self.status}'

    def set_status(self,status):
        old_status=self. status
        self.status=status
        print(f'the status is changed to {old_status}--->{self.status}')
    def accept_ride(self,user,dist=20):
        if self.status != 'Availabel':
            print('the driver is not avaialabele')
        else:
            print(f'the driver {self.driver} is on the way')
            self.set_status= 'Busy'
            self.history.append([self.driver, f'user:{user.u_name}', f'Distance: {dist}'])
    def complete_ride(self):
        return self.set_status("Availabel")
class user:
    
    def __init__(self,u_name,id):
        self.u_name= u_name
        self.id=id
        self.history=[]
    
    def recquest_ride(self,dist,zone):
        drivers_list = zone.getDrivers()[0]
        act_drivers_status= [i.get_driver() for i in drivers_list]
        print(act_drivers_status)
        # print(drivers_list)
    


        
        
 



        