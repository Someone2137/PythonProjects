import random
import json
import csv
import math

class Sheep:
    def __init__(self, sheep_number, x, y):
        self.sheep_number = sheep_number
        self.x = x
        self.y = y

    def sheep_position(self):
        return (self.x, self.y)

    def sheep_move(self):
        movement_direction = random.choice(['north', 'south', 'east', 'west'])

        if movement_direction == 'north':
            self.y += 0.5
        elif movement_direction == 'south':
            self.y -= 0.5
        elif movement_direction == 'east':
            self.x += 0.5
        elif movement_direction == 'west':
            self.x -= 0.5

class Wolf:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

    def wolf_position(self):
        return (round(self.x, 3), round(self.y, 3))

    def wolf_move(self, sheep):
        sheep_x, sheep_y = sheep.sheep_position()
        distance_between_wolf_and_sheep = math.sqrt((sheep_x - self.x) ** 2 + (sheep_y - self.y) ** 2)

        if distance_between_wolf_and_sheep <= 1.0:
            self.x, self.y = sheep_x, sheep_y
            return True
        else:
            ratio = 1.0 / distance_between_wolf_and_sheep
            self.x += (sheep_x - self.x) * ratio
            self.y += (sheep_y - self.y) * ratio
            return False

class Meadow:
    def __init__(self, maximum_number_of_rounds, number_of_sheep):
        self.maximum_number_of_rounds = maximum_number_of_rounds
        self.number_of_sheep = number_of_sheep
        self.round_number = 0
        self.sheep_list = []
        self.wolf = Wolf()
        self.number_of_alive_sheep = number_of_sheep

        for index in range(number_of_sheep):
            x = random.uniform(-10.0, 10.0)
            y = random.uniform(-10.0, 10.0)
            self.sheep_list.append(Sheep(index, x, y))

    def find_closest_sheep(self):
        min_distance = float('inf')
        closest_sheep = None
        for sheep in self.sheep_list:
            if sheep:
                distance_between_wolf_and_sheep = math.sqrt((sheep.x - self.wolf.x) ** 2 + (sheep.y - self.wolf.y) ** 2)
                if distance_between_wolf_and_sheep < min_distance:
                    min_distance = distance_between_wolf_and_sheep
                    closest_sheep = sheep
        return closest_sheep

    def run_simulation(self):
        positions_of_animals = []
        sheep_alive = []

        for _ in range(self.maximum_number_of_rounds):
            self.round_number += 1
            for sheep in self.sheep_list:
                if sheep:
                    sheep.sheep_move()

            closest_sheep = self.find_closest_sheep()

            if closest_sheep:
                eaten_sheep = self.wolf.wolf_move(closest_sheep)

                if eaten_sheep:
                    self.sheep_list[closest_sheep.sheep_number] = None
                    self.number_of_alive_sheep -= 1
                    print(f'Round {self.round_number}: Wolf ate sheep {closest_sheep.sheep_number}.')
                else:
                    print(f'Round {self.round_number}: Wolf is chasing sheep {closest_sheep.sheep_number}.')

            print(f'Round {self.round_number}: Wolf position is {self.wolf.wolf_position()}.')
            print(f'Round {self.round_number}: Alive sheep count: {self.number_of_alive_sheep}.')

            positions_of_animals.append({
                'round_number': self.round_number,
                'wolf_position': self.wolf.wolf_position(),
                'sheep_position': [sheep.sheep_position() if sheep else None for sheep in self.sheep_list]
            })

            sheep_alive.append([self.round_number, self.number_of_alive_sheep])

            if self.number_of_alive_sheep == 0:
                break

        self.save_json(positions_of_animals)
        self.save_csv(sheep_alive)

    def save_json(self, data):
        with open('positions_of_animals.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def save_csv(self, data):
        with open('alive_sheep.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['round_number', 'alive_sheep'])
            writer.writerows(data)

meadow = Meadow(number_of_sheep=15, maximum_number_of_rounds=50)
meadow.run_simulation()








