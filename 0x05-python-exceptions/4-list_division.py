#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    str = []
    change = 0
    for y in range(list_length):
        try:
            z = my_list_1[y] / my_list_2[y]
        except ZeroDivisionError:
            print("division by 0")
            change = 1
        except TypeError:
            print("wrong type")
            change = 1
        except IndexError:
            print("out of range")
            change = 1
        finally:
            if change:
                change = 0
                str.append(0)
            else:
                str.append(z)
    return str
