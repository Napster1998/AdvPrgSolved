class clockType:
    hours = 0
    minutes = 0
    seconds = 0

    hours2 = 0
    minutes2 = 0
    seconds2 = 0

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def SecondsElapsed(self):
        elapsed_time = self.hours * 3600 + self.minutes * 60 + self.seconds
        return elapsed_time

    def RemainingTime(self):
        TotalTimeSeconds = 24 * 3600
        RemainingTime = TotalTimeSeconds - (self.hours * 3600 + self.minutes * 60 + self.seconds)
        return RemainingTime

    def TwoClocksDifference(self, c1, c2):
        clock1 = c1.split(':')
        clock2 = c2.split(':')

        if int(clock1[0]) >= int(clock2[0]):
            self.hours = int(clock1[0]) - int(clock2[0])
        else:
            self.hours = int(clock2[0]) - int(clock1[0])

        if clock1[1] >= clock2[1]:
            self.minutes = int(clock1[1]) - int(clock2[1])
        else:
            self.minutes = int(clock2[1]) - int(clock1[1])

        if int(clock1[2]) >= int(clock2[2]):
            self.seconds = int(clock1[2]) - int(clock2[2])
        else:
            self.seconds = int(clock2[2]) - int(clock1[2])

        print("%d:%d:%d" % (self.hours, self.minutes, self.seconds))


clock1 = clockType(13, 56, 6)

Seconds_Elapsed = clock1.SecondsElapsed()
print("Seconds_Elapsed: %d seconds" % Seconds_Elapsed)

Remaining_Time = clock1.RemainingTime()
print("Remaining_Time: %d seconds" % Remaining_Time)

clock1.TwoClocksDifference("14:16:54", "16:44:19")