LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", "\"", ",", ".", "<", ">", "?", "/", "\\","`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    """Check if word is in file. case_sensitive defaults to False."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                file_word = line.strip()
                if case_sensitive:
                    if word == file_word:
                        return True
                else:
                    if word.lower() == file_word.lower():
                        return True
        return False
    except FileNotFoundError:
        return False

def word_has_character(word, character_list):
    """Returns True if any char in word is in character_list."""
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    """Complexity 0-4 based on types of characters used."""
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):
    """Checks dictionary, toppasswords, length, complexity and returns strength 0-5."""
    
    # 1. Dictionary check - case insensitive
    if word_in_file(password, "wordlist.txt", case_sensitive=False):
        print("Password is a dictionary word and is not secure.")
        return 0

    # 2. Top passwords check - case sensitive
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0

    # 3. Too short
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

    # 4. Too long - strong
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5

    # 5. Complexity based
    complexity = word_complexity(password)
    strength = 1 + complexity
    return strength

def main():
    print("Password Strength Checker - Enter Q to quit")
    while True:
        password = input("Enter a password to check: ")
        if password.lower() == "q":
            break
        
        strength = password_strength(password)
        print(f"The password '{password}' has a strength of {strength}")
        print()

if __name__ == "__main__":
    main()
