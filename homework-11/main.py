def arrays_sum(array1, array2):
    if len(array1) > len(array2):
        array2 = array2 + [0] * (len(array1) - len(array2))
    else:
        array1 = array1 + [0] * (len(array2) - len(array1))

    return [sum(x) for x in zip(array1, array2)]

