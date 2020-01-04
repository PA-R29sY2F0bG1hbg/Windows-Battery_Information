import psutil
import tkinter as tk
import tkMessageBox

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent
print percent
if percent == 95:
        # message box
        root = tk.Tk()
        root.withdraw()
        tkMessageBox.showwarning("Battery Information", "Battery Fully Charged Please Unplug the charger")
