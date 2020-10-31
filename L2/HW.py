import sqlite3, os, random

dbo = sqlite3.connect("Person.db")
db = dbo.cursor()


# se7brQdRAAWf - GitHub pass


class Person:
    def __init__(self, name: str, birthYear: str):
        self.name = name
        self.birthYear = birthYear
    
    def __repr__(self):
        return f"\nИмя: {self.name}\nГод рождения: {self.birthYear}"


class Passenger(Person):
    def __init__(self, id: str, name: str, birthYear: str):
        super().__init__(name, birthYear)

        self.id = id
        self.route = None

    def setRoute(self, id: str = "0"):
        db.execute("select * from Routes where ID = :id", {"id": str(id)})
        data = db.fetchall()[0]

        self.route = Route(data[0], data[1], data[2], int(data[3]), int(data[4]))

    def __repr__(self):
        return super().__repr__() + self.route.__repr__()


class Route:
    def __init__(self, id, arrival, departure, distance, price):
        self.id = id
        self.arrival = arrival
        self.departure = departure
        self.distance = distance
        self.price = price

    def __repr__(self):
        return f"""\n\nМесто отправления: {self.arrival}\nМесто прибытия: {self.departure}\nДистанция: {self.distance}\nПлата за билет: {self.distance * self.price}"""


class Manager:
    @classmethod
    def checkPassengerID(cls, id: str = "0"):
        db.execute("select ID from Passengers")
        data = db.fetchall()

        if not data:
            return False

        if not id in data[0]:
            return False

        return True

    @classmethod
    def checkRouteID(cls, id: str = "0"):
        db.execute("select ID from Routes")

        data = db.fetchall()

        if not data:
            return False

        if not id in data[0]:
            return False

        return True

    @classmethod
    def createPassenger(cls) -> Passenger:
        p = None

        while True:
            os.system("cls")
            act = input("1. Создать нового пассажира.\n2. Взять пассажира из базы данных.\n>>> ")
            act = int(act) if act.isdigit() else None

            if not act in [1, 2]:
                continue

            elif act == 1:
                data = [str(random.randint(0, 9999)), input("\nВведите имя: "), input("Введите год рождения: ")]

            elif act == 2:
                id = input("\nВведите ID пассажира: ")

                if Manager.checkPassengerID(id):
                    db.execute("select * from Passengers where ID = :id", {"id": id})
                    data = db.fetchall()[0]

                else:
                    print("Пассажира с таким ID не существует.")
                    os.system("pause")
                    continue

            p = Passenger(data[0], data[1], data[2])

            break

        if not Manager.checkPassengerID(p.id):
            act = input("\nВы хотите сохранить пассажира? (y/n)\n>>> ")
            
            if act == "y":
                Manager.savePassenger(p)


        id = input("Введите ID маршрута: ")

        if Manager.checkRouteID(id):
            p.setRoute(id)

        else:
            print("Маршрута с таким ID не существует.")
            act = input("\nВы хотите создать маршрут? (y/n)\n>>> ")
    
            if act == "y":
                p.route = Manager.createRoute()

        return p

    @classmethod
    def createRoute(cls) -> Route:
        r = None

        while True:
            os.system("cls")
            act = int(input("1. Создать новый маршрут.\n2. Взять маршрут из базы данных\n>>> "))

            if not act in [1, 2]:
                continue

            elif act == 1:
                data = [
                    str(random.randint(0, 9999)), input("\nВведите место отправления: "),
                    input("Введите место прибытия: "), input("Введите расстояние: "), input("Введите цену за км: ")
                    ]

            elif act == 2:
                id = input("\nВведите ID маршрута: ")

                if Manager.checkRouteID(id):
                    db.execute("select * from Routes where ID = :id", {"id": id})
                    data = db.fetchall()[0]

                else:
                    print("Маршрута с таким ID не существует.")
                    os.system("pause")
                    continue

            r = Route(data[0], data[1], data[2], data[3], data[4])

            break

        if not Manager.checkRouteID(r.id):
            act = input("\nВы хотите сохранить маршрут? (y/n)\n>>> ")

            if act == "y":
                Manager.saveRoute(r)

        return r

    @classmethod
    def savePassenger(cls, p: Passenger):
        db.execute("insert into Passengers values (:id, :name, :birthYear)", {"id": p.id, "name": p.name, "birthYear": p.birthYear})
        dbo.commit()

        print(f"\nПассажир с ID {p.id} сохранен успешно!")

    @classmethod
    def saveRoute(cls, r: Route):
        db.execute("insert into Routes values (:id, :arrival, :departure, :distance, :price)", 
            {"id": r.id, "arrival": r.arrival, "departure": r.departure, "distance": r.distance, "price": r.price}
        )
        dbo.commit()

        print(f"\nМаршрут с ID {r.id} сохранен успешно!")


manager = Manager()

p = manager.createPassenger()

print(p)