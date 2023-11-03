import time
import pystray
from PIL import Image, ImageDraw
import tkinter as tk
from tkinter.simpledialog import askinteger
from rest_timer import RestTimer


def draw_circle(image, color="green"):
    draw = ImageDraw.Draw(image)
    draw.ellipse((2, 2, 14, 14), fill=color)


class BreakSystemTrayApp:
    def __init__(self):
        self.running = True

        # Create a new image with a transparent background
        self.icon = Image.new("RGBA", (16, 16), (255, 255, 255, 0))
        draw_circle(self.icon, color="green")

        # Create the system tray app
        menu = (pystray.MenuItem("Perform Task", self.perform_task), pystray.MenuItem("Exit", self.on_exit))
        self.systray = pystray.Icon("BreakTimer", self.icon, menu=menu)
        self.rest_timer = RestTimer()

    def perform_task(self):
        # Get the integer input from the user
        integer_input = askinteger("Break interval", "Enter an integer:")
        if integer_input is not None:
            print(f"You entered: {integer_input}")

    def on_exit(self, systray):
        # Function to handle exit action
        systray.stop()
        self.running = False

    def run(self):
        # Run the system tray app
        self.systray.run_detached()

        # Your code can continue running in the background
        while self.running:
            status_change = self.rest_timer.break_timing()

            if status_change == "active":
                self.update_icon(color="green")
            elif status_change == "break":
                self.update_icon(color="red")

    def update_icon(self, color="green"):
        draw_circle(self.icon, color=color)
        self.systray.update_menu()


if __name__ == "__main__":
    app = BreakSystemTrayApp()
    app.run()
