class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


class Track:
    def __init__(self, start_x, start_y):
        self.track = [TrackLine(start_x, start_y, 0)]

    def add_track(self, tr):
        self.track.append(tr)

    def get_tracks(self):
        return tuple(self.track)

    @staticmethod
    def __get_dist(start, end):
        x0, y0 = start.to_x, start.to_y
        x1, y1 = end.to_x, end.to_y
        return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5

    def __len__(self):
        track = self.track
        return int(sum([self.__get_dist(track[i], track[i + 1]) for i in range(len(track) - 1)]))

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __le__(self, other):
        return len(self) <= len(other)


track1 = Track(0, 0)
track2 = Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
