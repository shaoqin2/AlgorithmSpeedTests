# This is aimed to test different ways to return index of the max list value in python

problem statement: given a list with integers or floats, assuming all numerical. Test the fastest way to return the index of the max value


### Solution1:

Use intuitive method. keep `max_value` and `max_index`, keep getting the maximum value


### Solution2:

Use `max(list)` to get the max value and then `list.index(maxx_value)` to get the index. May seem unintuitive since it iterates twice but we will see :)


### Solution3:

Use `numpy.argmax()` 


## Result:
