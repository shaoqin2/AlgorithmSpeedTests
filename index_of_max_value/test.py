import timeit

# solution1
def intuitive(l):
    max_index = -1
    max_value = -999999999999999

    for index, value in enumerate(l):
        if value > max_value:
            max_value = value
            max_index = index
    return max_index


# solution2
def built_in_max_index(l):
    max_value = max(l)
    return l.index(max_value)

# solution3
def numpy_argmax(l):
    import numpy as np
    return np.argmax(l)


if __name__ == '__main__':
    print(timeit.timeit('''
def intuitive(l):
    max_index = -1
    max_value = -999999999999999

    for index, value in enumerate(l):
        if value > max_value:
            max_value = value
            max_index = index
    return max_index

intuitive([1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 2, 7])
    ''', number = 1000000))

    print(timeit.timeit('''
def built_in_max_index(l):
    max_value = max(l)
    return l.index(max_value)
    
built_in_max_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 2, 7])
    ''', number = 1000000))

    print(timeit.timeit('''
def numpy_argmax(l):
    import numpy as np
    return np.argmax(l)
    
numpy_argmax([1, 2, 3, 4, 5, 6, 7, 8, 9, 6, 2, 7])
    ''', number = 1000000))
