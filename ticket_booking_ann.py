import tkinter as tk
from tkinter import messagebox

class TicketBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Ticket Booking App")

        self.movie_tickets = 50
        self.total_bill = 0

        self.create_widgets()

    def create_widgets(self):
        self.label_movie = tk.Label(self.root, text="Movie Tickets Available: 50")
        self.label_movie.pack(pady=5)

        self.movie_var = tk.IntVar(self.root)
        self.movie_var.set(0)
        self.option_menu_movie = tk.OptionMenu(self.root, self.movie_var, *range(self.movie_tickets+1))
        self.option_menu_movie.pack(pady=10)

        self.btn_calculate = tk.Button(self.root, text="Calculate Bill", command=self.calculate_bill)
        self.btn_calculate.pack(pady=10)

        self.label_total_bill = tk.Label(self.root, text="Total Bill: ₹0")
        self.label_total_bill.pack(pady=10)

    def calculate_bill(self):
        movie_tickets_booked = self.movie_var.get()

        if movie_tickets_booked == 0:
            messagebox.showerror("Error", "Please select at least one movie ticket.")
            return

        self.total_bill = movie_tickets_booked * 100
        self.label_total_bill.config(text=f"Total Bill: ₹{self.total_bill}")

        self.movie_tickets -= movie_tickets_booked
        self.label_movie.config(text=f"Movie Tickets Available: {self.movie_tickets}")

        messagebox.showinfo("Success", "Movie tickets booked successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicketBookingApp(root)
    root.mainloop()
