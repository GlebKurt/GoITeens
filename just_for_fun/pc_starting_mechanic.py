start_btn = input("Press power button to start PC (START)")

def start_btn():
    if start_btn == START:
        Print("///")
        # starting_pc()
    else:
        print("You missed the button, stupid fool!")
        start_btn = input("Press power button to start PC (START)")
        start_btn()