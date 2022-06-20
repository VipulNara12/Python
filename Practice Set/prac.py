cal_to_units = 24
name_of_units = "Hours"


def days_of_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * cal_to_units} {name_of_units}"
    
    
def validate_execute():
    if user_input.isdigit():
        user_input_user = int(user_input)
        if user_input_user > 0:
            result_units = days_of_units(user_input_user)
            print(result_units)
        elif user_input_user == 0:
            print("You entered Zero so no conversion takes place.")
    else:
         print("Your input is not a number")

user_input = ""
while user_input != "Exit":
    user_input = input("Enter a number of days and I will convert it to hours\n")
    validate_execute()
