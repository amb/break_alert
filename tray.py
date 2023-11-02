import time
import pystray
from PIL import Image, ImageDraw
import tkinter as tk
from tkinter.simpledialog import askinteger
from rest_timer import RestTimer


class MySystemTrayApp:
    def __init__(self):
        self.running = True
        # Create a new image with a transparent background
        self.icon_green = Image.new("RGBA", (16, 16), (255, 255, 255, 0))

        # Draw on the icon (e.g., a blue circle)
        draw = ImageDraw.Draw(self.icon_green)
        draw.ellipse((2, 2, 14, 14), fill="green")

        menu = (pystray.MenuItem("Perform Task", self.perform_task), pystray.MenuItem("Exit", self.on_exit))

        # Create the system tray app
        self.systray = pystray.Icon("MyApp", self.icon_green, menu=menu)

        self.rest_timer = RestTimer()

    def perform_task(self):
        # Get the integer input from the user
        integer_input = askinteger("Integer Input", "Enter an integer:")
        if integer_input is not None:
            print(f"You entered: {integer_input}")

    def on_exit(self, systray):
        # Function to handle exit action
        systray.stop()
        self.running = False

    def run(self):
        # Run the system tray app
        self.systray.run()

        # Your code can continue running in the background
        while self.running:
            _ = self.rest_timer.break_timing()


if __name__ == "__main__":
    app = MySystemTrayApp()
    app.run()
