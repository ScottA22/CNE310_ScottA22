# Convert Fahrenheit to Celsius

def user_input():
    temp_input = int(input("Enter a temperature in Fahrenheit: "))
    return temp_input;

def f_to_c(f_temp):
    c_temp = (f_temp - 32) / 1.8
    return c_temp;

def print_results(c_temp):
    print(f"Temperature in Celsius: {c_temp}")
    return

def main():
    f_temp = user_input()
    c_temp = f_to_c(f_temp)
    print_results(c_temp)


main()