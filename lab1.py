# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}
# Test coment
def text_to_morse(text):
    """Convert text to Morse code"""
    morse_code = []
    
    for char in text.upper():
        if char == ' ':
            morse_code.append('/')  # Use / to separate words
        elif char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            # Skip unsupported characters
            continue
    
    return ' '.join(morse_code)

def morse_to_text(morse):
    """Convert Morse code back to text"""
    # Create reverse dictionary
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    
    # Split by word separators
    words = morse.split(' / ')
    decoded_words = []
    
    for word in words:
        letters = word.split(' ')
        decoded_letters = []
        
        for letter in letters:
            if letter in reverse_dict:
                decoded_letters.append(reverse_dict[letter])
            elif letter == '':
                continue
        
        decoded_words.append(''.join(decoded_letters))
    
    return ' '.join(decoded_words)

def main():
    """Main program loop"""
    print("=" * 50)
    print("          MORSE CODE CONVERTER")
    print("=" * 50)
    print("Options:")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    print("3. Exit")
    print("=" * 50)
    
    while True:
        try:
            choice = input("\nSelect option (1-3): ").strip()
            
            if choice == '1':
                text = input("Enter text to convert to Morse code: ")
                if text.strip():
                    morse = text_to_morse(text)
                    print(f"\nOriginal text: {text}")
                    print(f"Morse code: {morse}")
                else:
                    print("Please enter some text!")
                    
            elif choice == '2':
                morse = input("Enter Morse code (use spaces between letters, '/' between words): ")
                if morse.strip():
                    text = morse_to_text(morse)
                    print(f"\nMorse code: {morse}")
                    print(f"Decoded text: {text}")
                else:
                    print("Please enter some Morse code!")
                    
            elif choice == '3':
                print("Thank you for using Morse Code Converter!")
                break
                
            else:
                print("Invalid option! Please select 1, 2, or 3.")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()