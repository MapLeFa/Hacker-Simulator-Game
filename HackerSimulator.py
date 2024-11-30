import time
import random
import os

# Utility Functions
def print_slow(text, delay=0.03):
    """Prints text character by character for dramatic effect."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    """Clears the console for better UI."""
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(text="Loading", dots=3, cycles=3):
    """Simulates a loading animation."""
    for _ in range(cycles):
        for dot_count in range(dots + 1):
            print(f"\r{text}{'.' * dot_count}{' ' * (dots - dot_count)}", end="", flush=True)
            time.sleep(0.3)
    print()

# ASCII Art for Design
def hacker_art():
    """Displays cool hacker-themed ASCII art."""
    art = """
   ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
   ██║  ██║██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗
   ███████║███████║██║     ███████║█████╗  ██████╔╝
   ██╔══██║██╔══██║██║     ██╔══██║██╔══╝  ██╔═══╝ 
   ██║  ██║██║  ██║╚██████╗██║  ██║███████╗██║     
   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝     
    """
    print_slow(art, 0.002)

# Login System
def login_screen():
    """Simulates a login screen with username and password."""
    clear_screen()
    hacker_art()
    print("\nWelcome to the Hacker OS\n")
    username = input("Enter your email: ")
    password = input("Enter your password: ")
    loading_animation("Authenticating", cycles=5)
    print_slow(f"Access Granted. Welcome, {username.split('@')[0]}!")
    time.sleep(1)

# Main Menu
def main_menu():
    """Displays the main menu with options."""
    clear_screen()
    hacker_art()
    print("=== Hacker Simulator OS ===")
    print(f"💰 Wallet: ${wallet:.2f} | 🕵️ Police Meter: {police_meter}% | ✅ Tasks Completed: {tasks_completed}")
    print("\nMain Menu:")
    print("1. Crack a password")
    print("2. Launch a DDoS attack")
    print("3. Start a phishing campaign")
    print("4. Mine Bitcoin")
    print("5. Exit")
    return input("Enter your choice: ")

# Game Elements
wallet = 0  # Bitcoin wallet balance
police_meter = 0  # Risk of being caught
tasks_completed = 0

def bitcoin_miner():
    """Simulates mining Bitcoin."""
    global wallet
    print_slow("\n🔨 Starting Bitcoin miner...")
    loading_animation("Mining Bitcoins", cycles=5)
    mined_bitcoins = random.uniform(0.001, 0.01)  # Random small amount
    wallet += mined_bitcoins
    print_slow(f"✅ Successfully mined {mined_bitcoins:.6f} BTC!")
    time.sleep(2)

def password_cracking():
    """Simulates a password cracking task."""
    global wallet, police_meter, tasks_completed
    print_slow("\n🔓 Connecting to target server...")
    loading_animation("Brute-forcing password", cycles=4)
    if random.random() > 0.3:  # 70% success rate
        reward = random.randint(100, 1000)
        wallet += reward
        tasks_completed += 1
        print_slow(f"✅ Password cracked! Earned ${reward}.")
    else:
        police_meter += random.randint(5, 15)
        print_slow("❌ Failed! The police meter increased.")
    time.sleep(2)

def ddos_attack():
    """Simulates a DDoS attack task."""
    global wallet, police_meter, tasks_completed
    print_slow("\n🌐 Launching DDoS attack...")
    loading_animation("Overloading target", cycles=4)
    if random.random() > 0.5:  # 50% success rate
        reward = random.randint(500, 2000)
        wallet += reward
        tasks_completed += 1
        print_slow(f"✅ Attack successful! Earned ${reward}.")
    else:
        police_meter += random.randint(10, 20)
        print_slow("❌ Attack traced back! Police meter increased.")
    time.sleep(2)

def phishing_emails():
    """Simulates a phishing email campaign."""
    global wallet, police_meter, tasks_completed
    print_slow("\n📧 Setting up phishing campaign...")
    loading_animation("Sending fake emails", cycles=5)
    if random.random() > 0.4:  # 60% success rate
        reward = random.randint(300, 1500)
        wallet += reward
        tasks_completed += 1
        print_slow(f"✅ Phishing successful! Earned ${reward}.")
    else:
        police_meter += random.randint(5, 25)
        print_slow("❌ Campaign detected! Police meter increased.")
    time.sleep(2)

def check_police_meter():
    """Checks if the police meter is too high."""
    if police_meter >= 100:
        print_slow("\n🚨 The police have caught you! Game Over.")
        exit()
    else:
        print_slow(f"🕵️ Police Meter: {police_meter}%")

# Game Loop
def main():
    login_screen()
    while True:
        choice = main_menu()
        if choice == "1":
            password_cracking()
        elif choice == "2":
            ddos_attack()
        elif choice == "3":
            phishing_emails()
        elif choice == "4":
            bitcoin_miner()
        elif choice == "5":
            print_slow("Exiting the Hacker OS... Goodbye!")
            break
        else:
            print_slow("Invalid choice. Please try again.")
        check_police_meter()
        time.sleep(1)

# Start the Game
if __name__ == "__main__":
    main()
