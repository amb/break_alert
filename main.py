import time
import pyautogui
from win10toast import ToastNotifier


def check_mouse_activity():
    ticks = 0
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()
        moved = False

        # Wait for 10 minutes
        # 10 minutes = 600 seconds
        time.sleep(600)

        # Check if the mouse position is still the same
        new_x, new_y = pyautogui.position()
        if x == new_x and y == new_y:
            if moved == True:
                print("Ticks reset.")
            moved = False
            ticks = 0
        else:
            moved = True
            ticks += 1
            print("Tick.")

        if moved == True and ticks > 6:
            # Mouse hasn't moved, send a notification
            notifier = ToastNotifier()
            notifier.show_toast("Activity Alert", "No 10 minute break for an hour!", duration=10)


if __name__ == "__main__":
    check_mouse_activity()
