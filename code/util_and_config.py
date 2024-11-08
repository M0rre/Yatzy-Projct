# Config to for changing constant variables, such as dies and scoring rules

def error_handling_int(external_input):
    while True:
        user_input = input(external_input)
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")




def error_handling_string(external_input):
    while True:
        try:
            user_input = input(external_input)
            if not user_input.strip():
                raise ValueError("Input cannot be empty or whitespace.")
            return (user_input) #Returns if valid
        except ValueError:
            print("Invalid input. Please enter a valid string.")


    """
    Example on how to use ^
    user_input = error_handling_[type]("[Text]")
    """
    
    
def clear_terminal():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    # found how to find out if it's windows/linux: https://note.nkmk.me/en/python-platform-system-release-version/
    
