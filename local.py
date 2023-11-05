import pyperclip
from pynput import keyboard
import time
import sys
import random

typing_enabled = True

def on_key_release(key):
    global typing_enabled
    if key == keyboard.Key.ctrl and is_ctrl_pressed[0]:
        is_ctrl_pressed[0] = False
    elif key == keyboard.Key.shift and is_shift_pressed[0]:
        is_shift_pressed[0] = False
    elif key == keyboard.KeyCode.from_char('g') and is_ctrl_pressed[0] and is_shift_pressed[0]:
        paste_text_letter_by_letter()
    elif key == keyboard.Key.esc:  # Change to Escape key to stop pasting
        typing_enabled = False
        return False  # Stop listening for more key events after Escape is pressed

def on_key_press(key):
    if key == keyboard.Key.ctrl:
        is_ctrl_pressed[0] = True
    elif key == keyboard.Key.shift:
        is_shift_pressed[0] = True

def paste_text_letter_by_letter():
    text_to_paste = pyperclip.paste()
    total_chars = len(text_to_paste)
    start_time = time.time()
    
    for i, char in enumerate(text_to_paste, 1):
        if typing_enabled:
            keyboard.Controller().type(char)
            time.sleep(random.uniform(0.01, 0.09))  # Adjust the delay as needed
            
            # Calculate progress and display it
            progress = i / total_chars * 100
            progress_bar = '█' * int(progress / 2)
            elapsed_time = time.time() - start_time
            letters_per_sec = i / elapsed_time
            estimated_time_left = (total_chars - i) / letters_per_sec
            
            sys.stdout.write("\rTotal progress: {:.2f}% |{}| [{}<{}, {:.2f} lts/s]".format(progress, progress_bar.ljust(30), time.strftime("%M:%S", time.gmtime(elapsed_time)), time.strftime("%M:%S", time.gmtime(estimated_time_left)), letters_per_sec))
            sys.stdout.flush()
    
    sys.stdout.write("\n")
    sys.stdout.flush()

is_ctrl_pressed = [False]
is_shift_pressed = [False]

with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()
