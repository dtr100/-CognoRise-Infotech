import tkinter as tk
from tkinter import messagebox
import time

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        
        self.time_label = tk.Label(root, text="00:00", font=("Helvetica", 48))
        self.time_label.pack(pady=20)
        
        self.entry_label = tk.Label(root, text="Enter time (in seconds):")
        self.entry_label.pack()
        
        self.time_entry = tk.Entry(root, font=("Helvetica", 24))
        self.time_entry.pack()
        
        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer)
        self.stop_button.pack(pady=5)
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(pady=5)
        
        self.seconds_left = 0
        self.timer_running = False
        self.update_time()
    
    def start_timer(self):
        if not self.timer_running:
            try:
                self.seconds_left = int(self.time_entry.get())
                if self.seconds_left <= 0:
                    raise ValueError
                self.timer_running = True
                self.update_time()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid positive integer.")
    
    def stop_timer(self):
        self.timer_running = False
    
    def reset_timer(self):
        self.timer_running = False
        self.seconds_left = 0
        self.time_label.config(text="00:00")
    
    def update_time(self):
        if self.timer_running and self.seconds_left > 0:
            minutes, seconds = divmod(self.seconds_left, 60)
            self.time_label.config(text=f"{minutes:02d}:{seconds:02d}")
            self.seconds_left -= 1
            self.root.after(1000, self.update_time)
        elif self.seconds_left == 0:
            self.timer_running = False
            messagebox.showinfo("Timer", "Time's up!")
        
root = tk.Tk()
app = CountdownTimer(root)
root.mainloop()
