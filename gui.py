import tkinter as tk

window = tk.Tk()

window.title("Trakerz")
window.geometry("800x600")

sidebar = tk.Frame(window, width=200)
sidebar.pack(side="left", fill="y")


main_area = tk.Frame(window)
main_area.pack(side="right", fill="both", expand=True)

title = tk.Label(sidebar, text="TRAERZ")
title.pack(pady=20)


window.mainloop()
