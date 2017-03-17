# This is a test to see my implementation using hash map in the interview versus the suggested regex solution performance.

Problem statement:  
Find the longest repeating character string.

Example in:  
"aaaabbccccccdd"

Example out:
 c : 6

 ### Solution 1:

 read through the string and whenever there's a change in character, reset the counter and put the pair in the hash map. Record the maximum as well.



```python
In [27]: def native_max_only(s):
    ...:     max_rep = -1
    ...:     max_char = 'a'
    ...:     current_char = 'a'
    ...:     count = 0
    ...:     for index, value in enumerate(s):
    ...:         if value != current_char:
    ...:             if count > max_rep:
    ...:                 max_rep = count
    ...:                 max_char = current_char
    ...:             count = 1
    ...:             current_char = value
    ...:         else:
    ...:             count += 1
    ...:     if count > max_rep:
    ...:         max_rep = count
    ...:         max_char = current_char
    ...:     return (max_rep, max_char)
```

### Solution 2:

 Use regular expression to split all repeating substring, test against the length of each substring

```python
In [23]: def regex(s):
    ...:     all_match = [x.group() for x in re.finditer(r'(\w)\1+', s)]
    ...:     match_length = [len(x) for x in all_match]
    ...:     index = match_length.index(max(match_length))
    ...:     return (match_length[index], all_match[index][0])

```

## Result



### short string
```python
In [30]: short_string = "aaaaaabbbbcccddddeeeeeeeeeeeeeeeeeeeeeeee"

In [25]: %timeit regex(short_string)
100000 loops, best of 3: 4.07 µs per loop

In [29]: %timeit native_max_only(short_string)
100000 loops, best of 3: 2.89 µs per loop
```


### long string

```python
In [40]: long_string = ".join([chr(int(random.random(*128)) for i in range(100000)]))"

In [48]: %timeit native_max_only(long_string)
100 loops, best of 3: 8.5 ms per loop

In [51]: %timeit regex(long_string)
100 loops, best of 3: 4.59 ms per loop
```



### extra tests, test all word occurrence using a dictionary. I'm pretty sure this is the optimum implementation

```python
In [35]: def native_all_with_dic(s):
    ...:     d = {}
    ...:     for char in s:
    ...:         if char in d:
    ...:             d[char] += 1
    ...:         else:
    ...:             d[char] = 1
    ...:     key = max(d, key=d.get)
    ...:     return (d[key], key)

```

```python
In [50]: %timeit native_all_with_dic(long_string)
100 loops, best of 3: 9.07 ms per loop

n [37]: %timeit native_all_with_dic(short_string)
The slowest run took 8.50 times longer than the fastest. This could mean that an intermediate result is being cached.
100000 loops, best of 3: 3.85 µs per loop
```


## insight
