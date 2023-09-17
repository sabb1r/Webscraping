class Train:
    def __init__(self, name, code, off_day, stations, exclude_station=None):
        self.name = name
        self.down_code = code
        self.down_stations = stations
        self.off_day = off_day

        self.up_code = code + 1
        if not exclude_station:
            self.up_stations = stations[::-1]
        else:
            self.up_stations = [station for station in stations if station not in exclude_station]

    # def does_touch(self, station, direction):
    #     if direction not in ['up', 'down']:
    #         raise BadInput
    #     if (direction == 'up' and station in self.up_stations) or (
    #             direction == 'down' and station in self.down_stations):
    #         return True
    #     else:
    #         return False

    def previous_stations(self, station, direction):
        if direction not in ['up', 'down']:
            raise BadInput

        # if self.does_touch(station, direction):
        #     return self.down_stations[0:self.down_stations.index(station)] if direction == 'down' else self.up_stations[
        #                                                                                                0:self.up_stations.index(
        #                                                                                                    station)]
        # else:
        #     raise WrongStation


class BadInput:
    print('Input does not match with preferred format')


class WrongStation:
    print('The train does not touch the station')

