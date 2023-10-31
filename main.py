import time

import pyautogui
from win10toast import ToastNotifier

CHECK_INTERVAL = 20
BREAK_TIME = 120
MAX_TIME = 60 * 60

BREAK_INTERVALS = BREAK_TIME // CHECK_INTERVAL


def check_mouse_activity():
    slices = []
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
        else:
            # Moved
            slices.append(False)

        if all(slices[-BREAK_INTERVALS:]):
            # If had break, reset counter
            slices = []
            print("Had a break")

        if len(slices) >= MAX_TIME // CHECK_INTERVAL:
            notifier = ToastNotifier()
            notifier.show_toast("Activity Alert", "No break for an hour!", duration=10)


if __name__ == "__main__":
    check_mouse_activity()
