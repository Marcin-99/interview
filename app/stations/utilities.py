from app.models import Station
from app import db


'''Function checks if given argument (for example form.data) is an int.'''
def is_int(var):
    try:
        int(var)
        return True
    except ValueError:
        return False


'''Function checks if given (for example [1,2,3]) contains only float type variables.'''
'''It also checks if there are any empty forms (if var != '').'''
def is_float(vars):
    result = True
    for var in vars:
        if var != '':
            try:
                float(var)
            except ValueError:
                result = False
                break

    return result


'''Function checks if there is already station with the same ID when user tries to add new station.'''
def look_for_duplicates(id):
    duplicate = Station.query.filter_by(id=id).first()
    if duplicate:
        return True
    else:
        return False