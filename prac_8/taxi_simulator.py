from prac_8.taxi import Taxi
from prac_8.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def test():
    # bus = Car("Datsun", 180)
    # bus.drive(30)
    # print("fuel =", bus.fuel)
    # print("odo =", bus._odometer)
    # bus.drive(55)
    # print("fuel =", bus.fuel)
    # print("odo = ", bus._odometer)
    # print(bus)
    #
    # # drive bus (input/loop is oblivious to fuel)
    # distance = int(input("Drive how far? "))
    # while distance > 0:
    #     travelled = bus.drive(distance)
    #     print(bus)
    #     distance = int(input("Drive how far? "))

    t = Taxi("Prius 1", 100)
    print(t)
    t.drive(25)
    print(t, t.get_fare())
    t.start_fare()
    t.drive(40)
    print(t, t.get_fare())

    sst = SilverServiceTaxi("Limo", 100, 2)
    print(sst, sst.get_fare())
    sst.drive(10)
    print(sst, sst.get_fare())


# if __name__ == "__main__":
#     test()


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, str(taxi)))


def play_game():
    """
    Write a taxi simulator program that uses your Taxi and SilverServiceTaxi classes.
Each time, until they quit:
The user should be presented with a list of available taxis and get to choose one
Then they should say how far they want to drive
At the end of each trip, show them the price and add it to their bill
    """
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            # no error-checking
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except:
                print("Invalid Option")
        elif menu_choice == "d":
            current_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.car_name,
                                                         trip_cost))
            total_bill += trip_cost
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        menu_choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


play_game()