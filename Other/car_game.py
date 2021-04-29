car_state = -1
while True:
    command = input(">")
    if command.upper() == "HELP":
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif command.upper() == "START":
        if car_state > 0:
            print("Car is already running!")
        else:
            print("Car started...Ready to go!")
            car_state = 1
    elif command.upper() == "STOP":
        if car_state == 0:
            print("Car already stopped!")
        else:
            car_state = 0
            print("Car stopped.")
    elif command.upper() == "QUIT":
        break
    else:
        print("Could not understand your command. Try one of the below commands.")
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
