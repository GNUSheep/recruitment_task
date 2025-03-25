from datetime import date

def check_control_number(pesel: str) -> bool:
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    pesel_control_number = int(pesel[-1])

    control_sum = sum(weight * int(num) for weight, num in zip(weights, pesel[:-1]))
    calculated_control_number = control_sum % 10

    return 10 - calculated_control_number == pesel_control_number

def is_male(pesel: str) -> bool:
    if pesel[-2] in "13579":
        return True
    return False

def get_birth_date(pesel: str) -> (bool, str):
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    if 1 <= month <= 12:
        year += 1900
    elif 21 <= month <= 32:
        year += 2000
        month -= 20
    elif 81 <= month <= 92:
        year += 1800
        month -= 80
    elif 41 <= month <= 52:
        year += 2100
        month -= 40
    elif 61 <= month <= 72:
        year += 2200
        month -= 60
    else:
        return (False, "Error: Wrong birth date in PESEL")

    # checking if date is correct
    try:
        date(year, month, day)
    except ValueError:
        return (False, "Erorr: Invalid birth date in PESEL")

    return (True, f"{day:02d}-{month:02d}-{year}")
    
def is_valid(pesel: str) -> (bool, str, str):
    if not pesel.isdigit():
        return (False, "Error: PESEL should only contains digits", "")  
    if len(pesel) != 11:
        return (False, "Error: PESEL should be 11 numbers long", "")
    if not check_control_number(pesel):
        return (False, "Error: PESEL control numbers doesn't match with calculated one", "")  

    (is_ok, birth_date_or_err) = get_birth_date(pesel)
    if not is_ok:
        return (False, birth_date_or_err, "")

    gender = "female"
    if is_male(pesel):
        gender = "male"
    
    return (True, birth_date_or_err, gender)
