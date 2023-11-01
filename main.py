import time
import sys

import pyautogui
from win10toast import ToastNotifier

CHECK_INTERVAL = 30
BREAK_TIME = 60 * 3
MAX_TIME = 60 * 57

BREAK_INTERVALS = BREAK_TIME // CHECK_INTERVAL

notifier = ToastNotifier()


def print_char(c):
    sys.stdout.write(c)
    sys.stdout.flush()


def check_mouse_activity():
    slices = []
    on_break = False
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()

        # Wait for 10 minutes
        # 10 minutes = 600 seconds
        time.sleep(CHECK_INTERVAL)

        # Check if the mouse position is still the same
        new_x, new_y = pyautogui.position()
        if x == new_x and y == new_y:
            # Rested
            slices.append(True)
            print_char("T")
        else:
            # Moved
            slices.append(False)
            print_char("F")

        if len(slices) >= BREAK_INTERVALS and all(slices[-BREAK_INTERVALS:]):
            # If had break, reset counter
            slices = []
            print("\nSlices reset")
            if on_break:
                print("\nHad a break")
                notifier.show_toast("Rest Timer", "You had a break!")
                on_break = False
                print_char("S")

        if len(slices) == MAX_TIME // CHECK_INTERVAL:
            notifier.show_toast("Rest Timer", "Take a break!")
            on_break = True


if __name__ == "__main__":
    print_char("S")
    check_mouse_activity()
