class Person:
    def __init__(self):
        self.name = None
        self.byear = None
    
    def input(self, name, byear, *args, **kwargs):
        self.name = name
        self.byear = byear

    def __repr__(self):
        return f"Имя: {self.name}\nГод рождения: {self.byear}"

class Passenger(Person):
    def __init__(self):
        super().__init__()
        self.arrival = None
        self.departure = None
        self.distance = None

    def input(self, name, byear, *args, **kwargs):
        super().input(name, byear, *args, **kwargs)
        self.arrival = kwargs["arrival"]
        self.departure = kwargs["departure"]
        self.distance = kwargs["distance"]

    def getRoutePrice(self):
        price = self.getKmPrice()

        if price is None:
            raise RuntimeError("Invalid price value: None.")
        if self.distance is None:
            raise RuntimeError("Invalid distance value: None.")

        return price * self.distance

    @classmethod
    def getKmPrice(cls, meta: dict = None):
        return 0.55

    
data = [
    ("Lol", "Kek", 123),
    ("A", "B", 23),
    ("G", "D", 100)
]

passengers = [
    {
        "name": "Dima",
        "byear": 2007
    },
    {
        "name": "Chelovek",
        "byear": 3000
    },
    {
        "name": "PDSK",
        "byear": 700
    }

]

for pass_id, passenger_data in enumerate(passengers):
    passenger = Passenger()

    passenger.input(**passenger_data, arrival = data[pass_id][0], departure = data[pass_id][1], distance = data[pass_id][2])
    print(passenger.getRoutePrice())