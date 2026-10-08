import tkinter as tk
expenses = []

def get_total_expense():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total

window = tk.Tk()

window.title("Trakerz")
window.geometry("800x600")

sidebar = tk.Frame(window, width=200)
sidebar.pack(side="left", fill="y")

main_area = tk.Frame(window)
main_area.pack(side="right", fill="both", expand=True)

dashboard_title = tk.Label(
    main_area,
    text="Dashboard",
    font=("Arial", 24, "bold")
)

subtitle = tk.Label(
    main_area,
    text="Your personal finance overview",
    font=("Arial", 11)
)

subtitle.pack(anchor="w", padx=30)
dashboard_title.pack(anchor="w", padx=30, pady=(30, 5))

total_card = tk.Frame(main_area, width=250, height=120)
total_card.pack(anchor="w", padx=30, pady=30)

total_label = tk.Label(
    total_card,
    text="Total Spending",
    font=("Arial", 12)
)

total_label.pack(pady=(20, 5))

total_amount = tk.Label(
    total_card,
    text="₹0",
    font=("Arial", 24, "bold")
)

total_amount.pack()

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
