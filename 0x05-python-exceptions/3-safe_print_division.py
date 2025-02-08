#!/usr/bin/python3
def safe_print_division(a, b):
    prodct = 0
    try:
        prodct = a / b
    except Exception:
        prodct = None
    finally:
        print("Inside result: {}".format(prodct))
    return (prodct)
