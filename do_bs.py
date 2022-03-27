import math


class DoBs:

    def __init__(self):
        pass

    @staticmethod
    def bs(arr, find):
        arr_len = len(arr)

        if arr_len == 0 or sorted(arr) != arr:
            return 0, 'error'
        elif arr_len == 1 and arr[0] != find:
            return 0, 'not found'

        mid = math.floor(arr_len / 2)

        if arr[mid] == find:
            return mid, ''

        if arr[mid] > find:
            nom, ert = DoBs.bs(arr[0:mid:], find)
        elif arr[mid] < find:
            nom, ert = DoBs.bs(arr[mid:arr_len + 1:], find)
            nom += mid

        return nom, ert
