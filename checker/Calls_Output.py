import csv


class Calls_Output:
    def __init__(self, calls_file):
        self.rows = self.load_csv(calls_file)
        self.change_status(self.rows)

    def load_csv(self, calls_file):
        temp_list = []
        try:
            with open(calls_file, "r") as file:
                csvreader = csv.reader(file)
                for row in csvreader:
                    temp_list.append(row)
        except IOError as e:
            print(e)
        return temp_list

    @staticmethod
    def change_status(rows):
        for row in rows:
            if row[2] < row[3]:
                row[4] = 1
            else:
                row[4] = -1

    @staticmethod
    def save_csv(filename, calls_list):
        try:
            with open(filename, "w", newline="") as f:
                csvwriter = csv.writer(f)
                csvwriter.writerows(calls_list, )
        except IOError as e:
            print(e)

    def __str__(self):
        return f"{self.rows}"

    def __repr__(self):
        return f"{self.rows}"
