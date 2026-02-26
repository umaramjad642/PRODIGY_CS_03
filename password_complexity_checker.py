import re

def assess_password_strength(password):

    length_ok = 8 <= len(password) <= 16
    

    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    
    if not length_ok:
        return "Invalid", "Password must be between 8 and 16 characters long."


    criteria_met = sum([has_upper, has_lower, has_digit, has_special])

    if criteria_met == 4:
        return "Strong", "Excellent! Your password is secure."
    elif criteria_met == 3:
        return "Medium", "Good, but try adding more character variety."
    else:
        return "Weak", "Warning: Add numbers, symbols, or mixed casing."

print("--- Prodigy Tech: Password Complexity Checker (Task 03) ---")

while True:
    pwd = input("\nEnter password to assess (or 'Q' to quit): ")
    
    if pwd.lower() == 'q':
        print("Exiting... Stay secure!")
        break
        
    strength, feedback = assess_password_strength(pwd)
    print(f"[{strength.upper()}] - {feedback}")