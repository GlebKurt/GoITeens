start_btn = input("Press power button to start PC (START)")

trying_to_start = True

while trying_to_start:
    if start_btn == "START":
        print("///")
        # starting_pc()
        trying_to_start = False
    else:
        print("You missed the button, stupid fool!")
        start_btn = input("Press power button to start PC (START)")