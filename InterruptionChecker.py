import ctypes
from datetime import datetime
from sty import fg, bg, ef, rs

class InterruptionChecker:
    def __init__(self, times=[]):
        self.times = times
        self.interrupted = {"yes": 0, "no": 0}
        self.last_print = ""
        self.update_time()

    def does_interrupt(self):
        check = ""
        while check not in ("yes", "no"):
            check = input("Was the flow interupted? :").lower()
        return check

    def update_time(self):
        dt = datetime.now()
        self.time = datetime.strftime(dt, "%H:%M:%S")
        self.seconds = int(datetime.strftime(dt, "%S"))

    def update_interrupt(self):
        check = self.does_interrupt()
        self.interrupted[check] += 1

    def print_interrupt(self):
        print(f"{fg.green}The number of successful sessions: {self.interrupted['no']}{fg.rs}")
        print(f"{fg.red}The number of interrupted sessions: {self.interrupted['yes']}{fg.rs}")      

    def mainloop(self):
        while True:
            self.update_time()
            if not self.seconds % 5 and self.time != self.last_print:
                self.last_print = self.time
                print(self.time)
            if self.time in self.times:
                self.update_interrupt()
                self.print_interrupt()

if __name__ == "__main__":
    ichecker = InterruptionChecker(times=["20:33:00", "20:58:00", "20:57:00"])
    ichecker.mainloop()