import time
import pystray
from PIL import Image
import tkinter as tk
from tkinter.simpledialog import askinteger


# Function to perform the task with the integer input
def perform_task():
    # Get the integer input from the user
    integer_input = askinteger("Integer Input", "Enter an integer:")

    if integer_input is not None:
        # User provided an integer input, perform the task with it
        print(f"You entered: {integer_input}")
        # Your task logic with the integer_input goes here


def on_exit(systray):
    # Function to handle exit action
    systray.stop()


# Create the system tray icon
# Replace "icon.png" with your icon image file
image = Image.open("icon.png")
menu = (pystray.MenuItem("Perform Task", perform_task), pystray.MenuItem("Exit", on_exit))

# Create the system tray app
systray = pystray.Icon("MyApp", image, menu)

# Run the system tray app
systray.run()

# Your code can continue running in the background
while True:
    # Your background task goes here
    # Adjust the sleep interval as needed
    time.sleep(1)
