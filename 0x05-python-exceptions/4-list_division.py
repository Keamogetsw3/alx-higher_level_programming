#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for num in range(list_length):
        try:
            prodct = my_list_1[num] / my_list_2[num]
        except (ValueError, TypeError):
            print("wrong type")
            prodct = 0
        except ZeroDivisionError:
            print("division by 0")
            prodct = 0
        except IndexError:
            print("out of range")
            prodct = 0
        finally:
            new_list.append(prodct)
    return new_list
