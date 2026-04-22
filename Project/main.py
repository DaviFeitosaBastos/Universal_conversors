from time import sleep
import functions


def main():
    while True:
        functions.main_menu()

        try:
            choice = int(input("Choose an option -> "))

            if choice == 1:
                functions.celsius_to_fahrenheit()
            elif choice == 2:
                functions.km_to_miles()
            elif choice == 3:
                functions.brl_to_usd()
            elif choice == 4:
                functions.minutes_to_hours()
            elif choice == 5:
                print("Exiting...")
                break
            else:
                print("Invalid option. Choose between 1 and 5.")

        except ValueError:
            print("\nInvalid input. Please enter a number from 1 to 5.")
            sleep(1)


if __name__ == "__main__":
    main()
