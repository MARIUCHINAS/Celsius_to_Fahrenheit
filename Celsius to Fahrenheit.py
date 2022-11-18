from time import sleep

def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32

def main():
    print("This program converts temperatures from Celsius to Fahrenheit.")
    print()

    celsius = eval(input("Enter the temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print("The temperature in Fahrenheit is", fahrenheit)
    print()
    sleep(15)
main()