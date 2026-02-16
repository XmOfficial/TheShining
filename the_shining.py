import time
import random
import sys

# Standard QWERTY layout for adjacent key simulation
KEYBOARD_LAYOUT = {
    'q': 'w', 'w': 'qe', 'e': 'wr', 'r': 'et', 't': 'ry', 'y': 'tu', 'u': 'yi', 'i': 'uo', 'o': 'ip', 'p': 'o',
    'a': 's', 's': 'ad', 'd': 'sf', 'f': 'dg', 'g': 'fh', 'h': 'gj', 'j': 'hk', 'k': 'jl', 'l': 'k',
    'z': 'x', 'x': 'zc', 'c': 'xv', 'v': 'cb', 'b': 'vn', 'n': 'bm', 'm': 'n'
}

def get_typo_char(char):
    """Returns an adjacent character on QWERTY keyboard if possible."""
    lower_char = char.lower()
    if lower_char in KEYBOARD_LAYOUT:
        replacement = random.choice(KEYBOARD_LAYOUT[lower_char])
        return replacement.upper() if char.isupper() else replacement
    return char

def apply_typos(text):
    """
    Introduces 1-2 typos into the text with a certain probability.
    Types of typos:
    1. Adjacent key hit
    2. Repetition
    3. Omission
    4. Transposition
    """
    if random.random() > 0.5: # 调整错字概率处
        return text

    # Copy to list for modification
    chars = list(text)
    num_typos = random.randint(1, 2)

    for _ in range(num_typos):
        if not chars: break
        
        idx = random.randint(0, len(chars) - 1)
        typo_type = random.choice(['adjacent', 'repeat', 'omit', 'transpose'])
        
        if typo_type == 'adjacent':
            chars[idx] = get_typo_char(chars[idx])
            
        elif typo_type == 'repeat':
            chars.insert(idx, chars[idx])
            
        elif typo_type == 'omit':
             # Prevent empty string if it's the only char
            if len(chars) > 1:
                chars.pop(idx)
                
        elif typo_type == 'transpose':
            if idx < len(chars) - 1:
                chars[idx], chars[idx+1] = chars[idx+1], chars[idx]
            elif idx > 0:
                chars[idx-1], chars[idx] = chars[idx], chars[idx-1]

    return "".join(chars)

def type_writer(text):
    """Simulates typewriter effect with varying delays."""
    for i, char in enumerate(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        
        # Base typing speed
        delay = random.uniform(0.03, 0.15)
        
        # Longer pause at spaces (thinking pause)
        if char == ' ':
            if random.random() < 0.2: # 20% chance to pause at space
                delay += random.uniform(0.2, 0.4)
        
        time.sleep(delay)
    
    # End of line pause/carriage return simulation
    time.sleep(random.uniform(0.3, 0.8))
    sys.stdout.write('\n')
    sys.stdout.flush()

def main():
    base_phrase = "All work and no play makes Jack a dull boy"
    
    time.sleep(1)
    
    try:
        while True:
            phrase_to_type = apply_typos(base_phrase)
            type_writer(phrase_to_type)
            
    except KeyboardInterrupt:
        ascii_art = r"""
  _    _ ______ _____  ______  _  _____ 
 | |  | |  ____|  __ \|  ____|' |/ ____|
 | |__| | |__  | |__) | |__     | (___  
 |  __  |  __| |  _  /|  __|     \___ \ 
 | |  | | |____| | \ \| |____    ____) |
 |_|  |_|______|_|  \_\______|  |_____/ 
                                        
       _  ____  _   _ _   _ __   __      _ 
      | |/ __ \| \ | | \ | |\ \ / /     | |
      | | |  | |  \| |  \| | \ V /      | |
  _   | | |  | | . ` | . ` |  | |       | |
 | |__| | |__| | |\  | |\  |  | |       |_|
  \____/ \____/|_| \_|_| \_|  |_|       (_)
 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!     
"""
        sys.stdout.write('\n' + ascii_art + '\n')
        sys.exit(0)

if __name__ == "__main__":
    main()
