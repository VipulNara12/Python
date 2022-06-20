cal_to_units = 24
name_of_units = "Hours"


def days_of_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * cal_to_units} {name_of_units}"
    
    
def validate_execute():
    try:
        user_input_user = int(num_of_days_element)
        if user_input_user > 0:
            result_units = days_of_units(user_input_user)
            print(result_units)
        elif user_input_user == 0:
            print("You entered Zero so no conversion takes place.")
        else:
            print("Your entered a Negative Number.")
    except ValueError:
        print("Your input is not a valid number")

user_input = ""
while user_input != "Exit":
    user_input = input("Enter a number of days and I will convert it to hours\n") 
    for num_of_days_element in user_input.split(","):
     validate_execute()