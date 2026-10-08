import tkinter as tk

window = tk.Tk()

window.title("Trakerz")
window.geometry("800x600")

sidebar = tk.Frame(window, width=200)
sidebar.pack(side="left", fill="y")


main_area = tk.Frame(window)
main_area.pack(side="right", fill="both", expand=True)

title = tk.Label(sidebar, text="TRAKERZ")
title.pack(pady=20)

dashboard_button = tk.Button(sidebar, text="Dashboard")
dashboard_button.pack(pady=10)

expenses_button = tk.Button(sidebar, text="Expenses")
expenses_button.pack(pady=10)

analytics_button = tk.Button(sidebar, text="Analytics")
analytics_button.pack(pady=10)

settings_button = tk.Button(sidebar, text="Settings")
settings_button.pack(pady=10)


window.mainloop()
