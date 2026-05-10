import os

def clear_screen():
    print("\033[H\033[J", end="")
    
def color_str(text, color):
    """
    Returns a string colored in the terminal.
    Supported colors: 'red', 'green', 'yellow'.
    """
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
    }
    
    reset = '\033[0m'
    
    # Default to white/no color if the color name is invalid
    code = colors.get(color.lower(), '')
    
    return f"{code}{text}{reset}"