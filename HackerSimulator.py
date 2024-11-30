import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
from threading import Thread

# Global Variables
wallet = 0
police_meter = 0
tasks_completed = 0
upgrades = {"VPN Boost": False, "Mining Rig": False, "Firewall Bypass": False, "Dark Web Access": False}
current_task = None
total_earnings = 0

# Helper Functions
def update_stats():
    """Updates the stats displayed in the GUI. Created by MapLe."""
    wallet_label.config(text=f"Wallet: ${wallet:.2f}")
    police_label.config(text=f"Police Meter: {police_meter}%")
    tasks_label.config(text=f"Tasks Completed: {tasks_completed}")
    total_label.config(text=f"Total Earnings: ${total_earnings:.2f}")

def show_message(title, message):
    """Displays a popup message. Created by MapLe."""
    messagebox.showinfo(title, message)

def simulate_progress(task_name, reward_range, success_chance, police_increase):
    """Simulates task progress with a progress bar. Created by MapLe."""
    def task_logic():
        global wallet, police_meter, tasks_completed, total_earnings
        task_window = tk.Toplevel(root)
        task_window.title(f"{task_name} - Hacker OS")
        task_window.geometry("500x150")
        task_window.resizable(False, False)
        task_window.config(bg="black")
        
        tk.Label(task_window, text=f"Executing {task_name}... - MapLe", font=("Courier", 16), fg="white", bg="black").pack(pady=10)
        progress = ttk.Progressbar(task_window, length=400, mode='determinate')
        progress.pack(pady=10)

        for i in range(100):
            time.sleep(0.03)
            progress["value"] += 1
            task_window.update_idletasks()

        task_window.destroy()
        
        # Outcome
        if random.random() < success_chance:
            reward = random.randint(*reward_range)
            wallet += reward
            total_earnings += reward
            tasks_completed += 1
            show_message(task_name, f"Success! Earned ${reward}.")
        else:
            police_meter += police_increase
            show_message(task_name, f"Failed! Police meter increased by {police_increase}.")
        update_stats()
    
    Thread(target=task_logic).start()

def bitcoin_miner():
    """Simulate Bitcoin mining task. Created by MapLe."""
    if upgrades["Mining Rig"]:
        simulate_progress("Bitcoin Mining", (50, 200), 0.9, 5)
    else:
        simulate_progress("Bitcoin Mining", (10, 50), 0.8, 10)

def password_cracking():
    """Simulate Password Cracking task. Created by MapLe."""
    simulate_progress("Password Cracking", (100, 500), 0.7, 15)

def ddos_attack():
    """Simulate DDoS Attack task. Created by MapLe."""
    simulate_progress("DDoS Attack", (300, 1000), 0.6, 20)

def phishing_emails():
    """Simulate Phishing Campaign task. Created by MapLe."""
    simulate_progress("Phishing Campaign", (200, 800), 0.75, 10)

def black_market():
    """Opens the black market window. Created by MapLe."""
    global wallet
    def purchase_item(item, cost, key):
        global wallet
        if wallet >= cost:
            wallet -= cost
            upgrades[key] = True
            update_stats()
            show_message("Black Market", f"{item} purchased successfully! - MapLe")
        else:
            show_message("Black Market", "Not enough money to purchase this item. - MapLe")

    # Black Market Window
    bm_window = tk.Toplevel(root)
    bm_window.title("Black Market - Hacker OS")
    bm_window.geometry("500x400")
    bm_window.resizable(False, False)
    bm_window.config(bg="black")

    tk.Label(bm_window, text="Welcome to the Black Market! - MapLe", font=("Courier", 18), fg="white", bg="black").pack(pady=10)
    items = [
        ("VPN Boost", 500, "VPN Boost"),
        ("Mining Rig", 1000, "Mining Rig"),
        ("Firewall Bypass", 800, "Firewall Bypass"),
        ("Dark Web Access", 1500, "Dark Web Access"),
    ]

    for item, cost, key in items:
        tk.Button(bm_window, text=f"Buy {item} (${cost})", 
                  command=lambda i=item, c=cost, k=key: purchase_item(i, c, k), width=30, bg="green", fg="white").pack(pady=5)

def escape_police():
    """Reduces the police meter with a chance of failure. Created by MapLe."""
    global police_meter
    def task_logic():
        task_window = tk.Toplevel(root)
        task_window.title("Escape Police - Hacker OS")
        task_window.geometry("500x150")
        task_window.resizable(False, False)
        task_window.config(bg="black")
        
        tk.Label(task_window, text="Escaping police... - MapLe", font=("Courier", 16), fg="white", bg="black").pack(pady=10)
        progress = ttk.Progressbar(task_window, length=400, mode='determinate')
        progress.pack(pady=10)

        for i in range(100):
            time.sleep(0.02)
            progress["value"] += 1
            task_window.update_idletasks()

        task_window.destroy()
        
        # Outcome
        if random.random() < 0.7:  # 70% chance of success
            reduction = random.randint(10, 30)
            police_meter = max(0, police_meter - reduction)
            show_message("Escape Police", f"Police Meter reduced by {reduction}! - MapLe")
        else:
            show_message("Escape Police", "Failed to escape! - MapLe")
        update_stats()
    
    Thread(target=task_logic).start()

# Police Meter Check
def check_police_meter():
    """Ends the game if the police meter reaches 100%. Created by MapLe."""
    global police_meter
    if police_meter >= 100:
        show_message("Game Over", "The police have caught you! Game Over. - MapLe")
        root.quit()

# Search Files
def search_files():
    """Simulate a file search operation. Created by MapLe."""
    def search_logic():
        task_window = tk.Toplevel(root)
        task_window.title("Search Files - Hacker OS")
        task_window.geometry("500x150")
        task_window.resizable(False, False)
        task_window.config(bg="black")
        
        tk.Label(task_window, text="Searching for Files... - MapLe", font=("Courier", 16), fg="white", bg="black").pack(pady=10)
        progress = ttk.Progressbar(task_window, length=400, mode='determinate')
        progress.pack(pady=10)

        for i in range(100):
            time.sleep(0.05)
            progress["value"] += 1
            task_window.update_idletasks()

        task_window.destroy()
        
        # Outcome
        result = random.choice(["Found confidential documents", "No files found", "Discovered hidden folder"])
        show_message("File Search", result + " - MapLe")
        update_stats()

    Thread(target=search_logic).start()

# Main GUI
root = tk.Tk()
root.title("Hacker OS - Main Terminal")
root.geometry("800x600")
root.resizable(False, False)
root.config(bg="black")

# Header
tk.Label(root, text="Hacker OS - MapLe", font=("Courier", 24, "bold"), fg="lime", bg="black").pack(pady=10)

# Stats Frame
stats_frame = tk.Frame(root, bg="black")
stats_frame.pack(pady=10)
wallet_label = tk.Label(stats_frame, text=f"Wallet: ${wallet:.2f}", font=("Courier", 14), fg="white", bg="black")
wallet_label.grid(row=0, column=0, padx=10)
police_label = tk.Label(stats_frame, text=f"Police Meter: {police_meter}%", font=("Courier", 14), fg="white", bg="black")
police_label.grid(row=0, column=1, padx=10)
tasks_label = tk.Label(stats_frame, text=f"Tasks Completed: {tasks_completed}", font=("Courier", 14), fg="white", bg="black")
tasks_label.grid(row=0, column=2, padx=10)
total_label = tk.Label(stats_frame, text=f"Total Earnings: ${total_earnings:.2f}", font=("Courier", 14), fg="white", bg="black")
total_label.grid(row=0, column=3, padx=10)

# Command Center (Buttons)
command_center_frame = tk.Frame(root, bg="black")
command_center_frame.pack(pady=20)
tk.Button(command_center_frame, text="Crack Password", command=password_cracking, width=20, bg="blue", fg="white").grid(row=0, column=0, padx=10, pady=5)
tk.Button(command_center_frame, text="Launch DDoS Attack", command=ddos_attack, width=20, bg="red", fg="white").grid(row=0, column=1, padx=10, pady=5)
tk.Button(command_center_frame, text="Phishing Campaign", command=phishing_emails, width=20, bg="yellow", fg="black").grid(row=1, column=0, padx=10, pady=5)
tk.Button(command_center_frame, text="Mine Bitcoin", command=bitcoin_miner, width=20, bg="purple", fg="white").grid(row=1, column=1, padx=10, pady=5)
tk.Button(command_center_frame, text="Search Files", command=search_files, width=20, bg="green", fg="white").grid(row=2, column=0, padx=10, pady=5)
tk.Button(command_center_frame, text="Escape Police", command=escape_police, width=20, bg="gray", fg="white").grid(row=2, column=1, padx=10, pady=5)

# Black Market Button
tk.Button(root, text="Enter Black Market", command=black_market, width=20, bg="orange", fg="white").pack(pady=10)

# Game Loop
def game_loop():
    check_police_meter()
    root.after(1000, game_loop)

# Start the game loop
game_loop()

root.mainloop()

# Coded by MapLe
