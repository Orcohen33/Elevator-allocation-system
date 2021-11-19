import math

from Elevators import *


class Elevator:
    def __init__(self, elev_dict):
        self._id = elev_dict['_id']
        self._speed = elev_dict['_speed']
        self._minFloor = elev_dict['_minFloor']
        self._maxFloor = elev_dict['_maxFloor']
        self._closeTime = elev_dict['_closeTime']
        self._openTime = elev_dict['_openTime']
        self._startTime = elev_dict['_startTime']
        self._stopTime = elev_dict['_stopTime']

        self.current_floor = 0
        self.next_time_free = 0
    def get_curr_floor(self):
        return self.current_floor

    def ride_time(self, df):
        return self._startTime + df / self._speed + self._stopTime + self._openTime + self._closeTime

    def reach2floor(self, df):
        return self._openTime + self._startTime + df / self._speed + self._stopTime

    def new_floor(self, call, time):
        self.current_floor = call['dst']
        self.next_time_free += math.ceil(time)
