# This is aimed to test different ways to return index of the max list value in python

problem statement: given a list with integers or floats, assuming all numerical. Test the fastest way to return the index of the max value


### Solution1:

Use intuitive method. keep `max_value` and `max_index`, keep getting the maximum value

```python
In [24]: def native_solution(l):
    ...:     max_value = -99999999
    ...:     max_index = -1
    ...:     for index, value in enumerate(l):
    ...:         if value>max_value:
    ...:             max_value = value
    ...:             max_index = index
    ...:
    ...:     return max_index
```


### Solution2:

Use `max(list)` to get the max value and then `list.index(maxx_value)` to get the index. May seem unintuitive since it iterates twice but we will see :)

```python
In [35]: def built_in_solution(l):
    ...:     return l.index(max(l))
```

### Solution3:

Use `numpy.argmax()` 


## Result:

### Test on small list
`In [17]: small_list = [random.random for i in range(100)]`

```
In [34]: %timeit native_solution(small_list)
100000 loops, best of 3: 5.28 µs per loop

In [37]: %timeit built_in_solution(small_list)
100000 loops, best of 3: 2.59 µs per loop


# small_list is a list passed in
In [40]: %timeit numpy_solution(small_list)
The slowest run took 4.37 times longer than the fastest. This could mean that an intermediate result is being cached.
100000 loops, best of 3: 8.72 µs per loop

In [41]: small_array = np.array(small_list)

In [43]: %timeit numpy_solution(small_array)
The slowest run took 12.68 times longer than the fastest. This could mean that an intermediate result is being cached.
1000000 loops, best of 3: 1.54 µs per loop
```


