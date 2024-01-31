#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
    except TypeError:
        return False
    # Other solution
    # except Exception
    # except Exception as e ('e' is variable where last
    # step was store)
