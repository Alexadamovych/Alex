import random

class Simulation:
    def __init__(self, population_size):
        self.population_size = population_size
        self.population = [Person() for _ in range(population_size)]

    def run_simulation(self):
        print("Simulation is running...")
        for person in self.population:
            person.interact()

class Person:
    def __init__(self):
        self.name = self.generate_name()
        self.age = random.randint(18, 80)

    def generate_name(self):
        names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Harry"]
        return random.choice(names)

    def interact(self):
        print(f"{self.name} is interacting in the simulation.")

# Запускаємо симуляцію з популяцією розміром 10 осіб
simulation = Simulation(population_size=10)
simulation.run_simulation()