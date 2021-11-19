import pandas as pd


class Calls:
    def __init__(self, calls_file: str):
        self.events = pd.read_csv(calls_file, header=None, usecols=[1, 2, 3, 4],
                                  names=['time_0', 'src', 'dst', 'elev_idx'])
        self.events['df'] = abs(self.events['dst'] - self.events['src'])

    def set_elevator_f2f(self, elevators):
        for i, e in enumerate(elevators):
            col_name = f'el{i}_dt_f2f'
            dfs = self.events['df']
            dts = e.ride_time(dfs)
            self.events[col_name] = dts
    """calculate the time from src to dst"""



    def set_elevator_totalTimeForCall(self, elevators):
        for i, e in enumerate(elevators):
            col_name = f'el{i}_dt_totalTime'
            col1 = self.events[f'el{i}_dt_f2f']
            self.events[col_name] = col1 + e.next_time_free
    """calculate the total time from curr floor to src to dst"""
