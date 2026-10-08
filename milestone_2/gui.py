import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

import database as database
import analytics as analytics


class TrakerzApp:

    def __init__(self, window):
        self.window = window

        self.window.title("Trakerz")
        self.window.geometry("1100x700")
        self.window.minsize(900, 600)

        self.setup_style()
        self.create_layout()

        self.show_dashboard()

    # -------------------------
    # STYLE
    # -------------------------

    def setup_style(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Treeview",
            rowheight=35,
            font=("Arial", 10)
        )

        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )

    # -------------------------
    # LAYOUT
    # -------------------------

    def create_layout(self):

        self.sidebar = tk.Frame(
            self.window,
            width=220
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.main_area = tk.Frame(
            self.window
        )

        self.main_area.pack(
            side="right",
            fill="both",
            expand=True
        )

        # Logo

        logo = tk.Label(
            self.sidebar,
            text="TRAKERZ",
            font=("Arial", 22, "bold")
        )

        logo.pack(pady=30)

        # Navigation

        tk.Button(
            self.sidebar,
            text="Dashboard",
            width=20,
            command=self.show_dashboard
        ).pack(pady=8)

        tk.Button(
            self.sidebar,
            text="Add Expense",
            width=20,
            command=self.show_add_expense
        ).pack(pady=8)

        tk.Button(
            self.sidebar,
            text="Expenses",
            width=20,
            command=self.show_expenses
        ).pack(pady=8)

        tk.Button(
            self.sidebar,
            text="Analytics",
            width=20,
            command=self.show_analytics
        ).pack(pady=8)

    # -------------------------
    # CLEAR SCREEN
    # -------------------------

    def clear_main_area(self):

        for widget in self.main_area.winfo_children():
            widget.destroy()

    # -------------------------
    # DASHBOARD
    # -------------------------

    def show_dashboard(self):

        self.clear_main_area()

        title = tk.Label(
            self.main_area,
            text="Dashboard",
            font=("Arial", 28, "bold")
        )

        title.pack(
            anchor="w",
            padx=40,
            pady=(40, 10)
        )

        subtitle = tk.Label(
            self.main_area,
            text="Your personal finance overview"
        )

        subtitle.pack(
            anchor="w",
            padx=40
        )

        total = database.get_total_expense()

        card = tk.Frame(
            self.main_area,
            relief="solid",
            borderwidth=1
        )

        card.pack(
            anchor="w",
            padx=40,
            pady=30,
            ipadx=50,
            ipady=25
        )

        tk.Label(
            card,
            text="Total Spending",
            font=("Arial", 12)
        ).pack()

        tk.Label(
            card,
            text=f"₹{total:,.2f}",
            font=("Arial", 25, "bold")
        ).pack(pady=10)

        tk.Button(
            self.main_area,
            text="+ Add Expense",
            command=self.show_add_expense
        ).pack(
            anchor="w",
            padx=40
        )

    # -------------------------
    # ADD EXPENSE
    # -------------------------

    def show_add_expense(self):

        self.clear_main_area()

        tk.Label(
            self.main_area,
            text="Add Expense",
            font=("Arial", 28, "bold")
        ).pack(
            anchor="w",
            padx=40,
            pady=(40, 30)
        )

        form = tk.Frame(self.main_area)

        form.pack(
            anchor="w",
            padx=40
        )

        # Category

        tk.Label(
            form,
            text="Category"
        ).grid(
            row=0,
            column=0,
            sticky="w",
            pady=10
        )

        self.category_entry = tk.Entry(
            form,
            width=40
        )

        self.category_entry.grid(
            row=0,
            column=1,
            padx=20
        )

        # Amount

        tk.Label(
            form,
            text="Amount"
        ).grid(
            row=1,
            column=0,
            sticky="w",
            pady=10
        )

        self.amount_entry = tk.Entry(
            form,
            width=40
        )

        self.amount_entry.grid(
            row=1,
            column=1,
            padx=20
        )

        # Description

        tk.Label(
            form,
            text="Description"
        ).grid(
            row=2,
            column=0,
            sticky="w",
            pady=10
        )

        self.description_entry = tk.Entry(
            form,
            width=40
        )

        self.description_entry.grid(
            row=2,
            column=1,
            padx=20
        )

        # Save button

        tk.Button(
            form,
            text="Add Expense",
            command=self.save_expense
        ).grid(
            row=3,
            column=1,
            sticky="w",
            pady=25
        )

    # -------------------------
    # SAVE EXPENSE
    # -------------------------

    def save_expense(self):

        category = self.category_entry.get().strip()
        amount = self.amount_entry.get().strip()
        description = self.description_entry.get().strip()

        if not category:
            messagebox.showerror(
                "Error",
                "Please enter a category."
            )
            return

        if not amount:
            messagebox.showerror(
                "Error",
                "Please enter an amount."
            )
            return

        try:
            amount = float(amount)

            if amount <= 0:
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Error",
                "Enter a valid positive amount."
            )

            return

        database.add_expense(
            category,
            amount,
            description,
            date.today().isoformat()
        )

        messagebox.showinfo(
            "Success",
            "Expense added successfully!"
        )

        self.show_dashboard()

    # -------------------------
    # EXPENSE LIST
    # -------------------------

    def show_expenses(self):

        self.clear_main_area()

        tk.Label(
            self.main_area,
            text="Expenses",
            font=("Arial", 28, "bold")
        ).pack(
            anchor="w",
            padx=40,
            pady=(40, 20)
        )

        table_frame = tk.Frame(
            self.main_area
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=10
        )

        columns = (
            "id",
            "category",
            "amount",
            "description",
            "date"
        )

        self.expense_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.expense_table.heading(
            "id",
            text="ID"
        )

        self.expense_table.heading(
            "category",
            text="Category"
        )

        self.expense_table.heading(
            "amount",
            text="Amount"
        )

        self.expense_table.heading(
            "description",
            text="Description"
        )

        self.expense_table.heading(
            "date",
            text="Date"
        )

        self.expense_table.pack(
            fill="both",
            expand=True
        )

        expenses = database.get_expenses()

        for expense in expenses:

            self.expense_table.insert(
                "",
                "end",
                values=(
                    expense[0],
                    expense[1],
                    f"₹{expense[2]:,.2f}",
                    expense[3],
                    expense[4]
                )
            )

        button_frame = tk.Frame(
            self.main_area
        )

        button_frame.pack(
            pady=15
        )

        tk.Button(
            button_frame,
            text="Delete Selected",
            command=self.delete_selected
        ).pack(
            side="left",
            padx=10
        )

    # -------------------------
    # DELETE
    # -------------------------

    def delete_selected(self):

        selected = self.expense_table.selection()

        if not selected:
            messagebox.showwarning(
                "Warning",
                "Select an expense first."
            )

            return

        item = self.expense_table.item(
            selected[0]
        )

        expense_id = item["values"][0]

        confirmation = messagebox.askyesno(
            "Confirm Delete",
            "Delete this expense?"
        )

        if confirmation:

            database.delete_expense(
                expense_id
            )

            self.show_expenses()

    # -------------------------
    # ANALYTICS
    # -------------------------

    def show_analytics(self):

        self.clear_main_area()

        tk.Label(
            self.main_area,
            text="Analytics",
            font=("Arial", 28, "bold")
        ).pack(
            anchor="w",
            padx=40,
            pady=(40, 30)
        )

        monthly = analytics.monthly_total()

        tk.Label(
            self.main_area,
            text=f"This Month: ₹{monthly:,.2f}",
            font=("Arial", 18, "bold")
        ).pack(
            anchor="w",
            padx=40,
            pady=10
        )

        tk.Label(
            self.main_area,
            text="Spending by Category",
            font=("Arial", 16, "bold")
        ).pack(
            anchor="w",
            padx=40,
            pady=(30, 10)
        )

        categories = analytics.category_totals()

        for category, amount in categories:

            tk.Label(
                self.main_area,
                text=f"{category}: ₹{amount:,.2f}",
                font=("Arial", 12)
            ).pack(
                anchor="w",
                padx=60,
                pady=4
            )


def main():

    database.initialize_database()

    window = tk.Tk()

    app = TrakerzApp(window)

    window.mainloop()


if __name__ == "__main__":
    main()