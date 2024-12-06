class Boat:
    def __init__(self, time, record_distance):
        self.time = time
        self.record = record_distance
        self.wins = self.ways_to_win()

    def ways_to_win(self):
        wins = 0
        for i in range(0, self.time):
            distance = self.distance_travelled(i)
            if distance > self.record:
                wins += 1
        return wins

    def distance_travelled(self, time_button_pressed):
        speed = time_button_pressed
        travel_distance = (self.time - time_button_pressed) * speed
        return travel_distance

    def get_wins(self):
        return self.wins


Time = [38, 67, 76, 73]
Record_Distance = [234, 1027, 1157, 1236]

total_wins = 1
for i in range(0, len(Time)):
    boat = Boat(Time[i], Record_Distance[i])
    total_wins *= boat.wins
print(total_wins)

boat = Boat(38677673, 234102711571236)
print(boat.wins)
