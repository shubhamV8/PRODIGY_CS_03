import re

def assess_password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Feedback/Comments about the missing requirements for pass
    strength = 0
    feedback = []

    if length_criteria:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if uppercase_criteria and lowercase_criteria:
        strength += 1
    else:
        feedback.append("Password should contain both uppercase and lowercase letters.")

    if digit_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one digit.")

    if special_char_criteria:
        strength += 1
    else:
        feedback.append("Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>).")
    
    # Strength Assessment
    if strength == 4:
        feedback.append("Password is strong.")
    elif strength >= 2:
        feedback.append("Password is moderate.")
    else:
        feedback.append("Password is weak.")
    
    return feedback

def main():
    while True:
        password = input("Enter your password: ")
        strength_feedback = assess_password_strength(password)
        for feedback in strength_feedback:
            print(feedback)
        
        choice = input("Do you want to check another password? (yes/no): ").strip().lower()
        if choice == 'no':
            print("Exiting...")
            break
        elif choice != 'yes':
            print("Invalid choice. Exiting...")
            break

if __name__ == "__main__":
    main()
