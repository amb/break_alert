import time
import sys
import pyautogui
from win10toast import ToastNotifier
from audio import alarm


def check_mouse_activity(check_interval=30):
    """Blocking function that checks if the mouse has moved in the last <check_interval> seconds"""
    x, y = pyautogui.position()
    time.sleep(check_interval)
    new_x, new_y = pyautogui.position()
    if x == new_x and y == new_y:
        return False
    else:
        return True


class RestTimer:
    def __init__(self, break_interval=60, break_time=3):
        """Times are in minutes"""

        self.notifier = ToastNotifier()
        # True is rested, False is moved
        self.slices = []
        self.on_break = False

        self.break_time = 60 * break_time
        self.max_time = 60 * (break_interval - break_time)

    def break_timing(self, check_interval=30):
        activity = check_mouse_activity(check_interval)
        self.slices.append(not activity)
        print("Pause" if not activity else "Active", len(self.slices))
        break_intervals = self.break_time // check_interval
        change_status = None
        if len(self.slices) >= break_intervals and all(self.slices[-break_intervals:]):
            # If had a break, reset counter
            self.slices = []
            print("Slices reset")
            if self.on_break:
                self.notifier.show_toast("Rest Timer", "You had a break!")
                self.on_break = False
                change_status = "active"

        if len(self.slices) == self.max_time // check_interval:
            print("Break alert")
            self.notifier.show_toast("Rest Timer", "Take a break!")
            self.on_break = True
            change_status = "break"
            alarm()

        return change_status


if __name__ == "__main__":
    rest_timer = RestTimer()
    while True:
        _ = rest_timer.break_timing()
