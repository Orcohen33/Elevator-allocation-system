import sys

import numpy as np
from Calls import *
from Calls_Output import Calls_Output
from Elevators import *
import json


def allocate_call(calls: Calls, elevs: Elevators, calls_output: Calls_Output):
    """
    allocating elevator for each call
    :param calls: list of calls (loaded with pandas)
    :param elevs: list of elevators ( loaded from json file)
    :param calls_output: list of calls with csv writer
    :return:None
    """
    for i, c in calls.events.iterrows():
        list_of_time = []
        x = 0
        for elev in elevs.elevators:
            E_time = elev.next_time_free
            arrive_time = abs(elev.current_floor - c['src'])
            if arrive_time != 0:
                E_time += math.ceil(elev.ride_time(arrive_time))
            E_time += math.ceil(calls.events.iloc[i][f'el{x}_dt_f2f'])
            list_of_time.append(E_time)
            x += 1

        elev_index = np.argmin(list_of_time)
        calls_output.rows[i][5] = elev_index
        elevs.elevators[elev_index].new_floor(call=c, time=list_of_time[elev_index])


if __name__ == '__main__':
    calls = Calls(sys.argv[2])
    elevs = Elevators(sys.argv[1])
    calls_output = Calls_Output(sys.argv[2])
    calls.set_elevator_f2f(elevs)
    allocate_call(calls, elevs, calls_output) # <-this function allocate the calls
    calls_output.save_csv(filename=sys.argv[3], calls_list=calls_output.rows)
