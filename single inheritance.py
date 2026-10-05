# 1. Without Constructor — Book → EBook
print("-------Book Details---------")
class Book:
    def read(self):
        print("Reading a book")
class EBook(Book):
    def download(self):
        print("Downloading e-book")
e=EBook()
e.read()
e.download()

# 2. With Constructor — Employee → Developer
print("-------Employee Details--------")
class Employee:
    def __init__(self):
        self.company="Wipro technologies"
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def __init__(self):
        self.role="python developer"
    def display(self):
        print("Role:",self.role)
d=Developer()
d.work()
d.display()

# 3. With Constructor + super() — Hospital → Doctor
print("--------Hospital Details--------")
class Hospital:
    def __init__(self):
        self.hospital_name="City Hospital"
class Doctor(Hospital):
    def __init__(self):
        super().__init__()
        self.specialization="Cardiology"
    def display(self):
        print("Hospital:",self.hospital_name)
        print("Specialization",self.specialization)
d=Doctor()
d.display()

# 4. With Constructor + super() — Restaurant → Chef
print("--------Restaurant Details---------")
class Restaurant:
    def __init__(self):
        self.restaurant_name="Spice Garden"
class Chef(Restaurant):
    def __init__(self):
        super().__init__()
        self.speciality="Indian Cuisine"
    def display(self):
        print("Restaurant:",self.restaurant_name)
        print("Speciality:",self.speciality)
c=Chef()
c.display()