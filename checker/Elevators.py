import json
from Elevator import *


class Elevators(Elevator):
    def __init__(self, elev_file):
        self.elevators = []
        try:
            with open(elev_file, "r") as e:
                building = json.load(e)
                for d in building["_elevators"]:
                    self.elevators.append(Elevator(d))

        except IOError as e:
            print(e)

    def __len__(self):
        return len(self.elevators)

    def __getitem__(self, item):
        return self.elevators[item]

    def __str__(self):
        return f'{self.elevators}'

    def getList(self):
        return self.elevators

    def save_to_json(self, file_name):
        try:
            with open(file_name, "w") as f:
                json.dump(self, indent=4, fp=f, default=lambda x: x.__dict__)
        except IOError as e:
            print(e)
