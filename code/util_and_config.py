# Config to for changing constant variables, such as dies and scoring rules

def error_handling_int(external_input):
    while True:
        user_input = input(external_input)
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    """
    Example on how to use ^
    user_number = error_handling_int("Enter a number: ")
    print(f"You entered: {user_number}")
    """
    
    
def clear_terminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    # found how to find out if it's windows/linux: https://note.nkmk.me/en/python-platform-system-release-version/