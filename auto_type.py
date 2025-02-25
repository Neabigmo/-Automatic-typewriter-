import time
import pyautogui

def auto_type(text, delay=0.1):
    """
    Automatically type the given text at the current cursor position
    
    Args:
        text (str): The text to type
        delay (float): Delay between each character (seconds)
    """
    # Add a small initial delay to give time to focus the desired window
    time.sleep(3)
    
    # Type the text with the specified delay between characters
    pyautogui.write(text, interval=delay)

if __name__ == "__main__":
    # Example usage
    print("Place your cursor where you want to type.")
    print("The typing will begin in 3 seconds...")
    
    # Demo text to type
    sample_text = "Hello! This is automatically typed text."
    auto_type(sample_text)