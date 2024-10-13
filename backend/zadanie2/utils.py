from datetime import datetime


def check_control_number(pesel):
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    checksum = sum(int(pesel[i]) * weights[i] for i in range(10))
    checksum = (10 - (checksum % 10)) % 10

    if checksum != int(pesel[10]):
        return False
    return True
    
def extract_pesel_data(pesel):
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    if month > 80:
        year += 1800
        month -= 80
    elif month > 60:
        year += 2200
        month -= 60
    elif month > 40:
        year += 2100
        month -= 40
    elif month > 20:
        year += 2000
        month -= 20
    else:
        year += 1900

    birthdate = datetime(year, month, day).strftime('%Y-%m-%d')
    sex = 'Male' if int(pesel[9]) % 2 != 0 else 'Female'

    return {'birthdate': birthdate, 'sex': sex}
