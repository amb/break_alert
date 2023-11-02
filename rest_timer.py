import time
import sys
import pyautogui
from win10toast import ToastNotifier
from audio import alarm


class RestTimer:
    def __init__(self):
        self.notifier = ToastNotifier()
        # True is rested, False is moved
        self.slices = []
        self.on_break = False

        self.break_time = 60 * 3
        self.max_time = 60 * 57

    def print_char(self, c):
        assert len(c) == 1
        sys.stdout.write(c)
        sys.stdout.flush()

    def check_mouse_activity(self, check_interval=30):
        """Blocking function that checks if the mouse has moved in the last <check_interval> seconds"""
        x, y = pyautogui.position()
        time.sleep(check_interval)
        new_x, new_y = pyautogui.position()
        if x == new_x and y == new_y:
            return False
        else:
            return True

    def break_timing(self, check_interval=30):
        activity = self.check_mouse_activity(check_interval)
        self.slices.append(not activity)
        self.print_char("R" if activity else "M")

        break_intervals = self.break_time // check_interval
        if len(self.slices) >= break_intervals and all(self.slices[-break_intervals:]):
            # If had a break, reset counter
            self.slices = []
            print("\nSlices reset")
            if self.on_break:
                print("\nHad a break")
                self.notifier.show_toast("Rest Timer", "You had a break!")
                self.on_break = False
                self.print_char("S")

        if len(self.slices) == self.max_time // check_interval:
            self.notifier.show_toast("Rest Timer", "Take a break!")
            self.on_break = True
            alarm()

        return activity


if __name__ == "__main__":
    rest_timer = RestTimer()
    rest_timer.print_char("S")
    while True:
        _ = rest_timer.check_mouse_activity()
