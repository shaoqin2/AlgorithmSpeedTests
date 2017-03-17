# Check existance in two lists and return a dataframe result

Problem Statement:

I have two lists of protein sequences, I have to check every entry's existence in the two lists, say like 

``` python
list A = [1,2,3,4]
list B= [3,4,5]

## just an example. The result would be convert into csv
result = [
[1, true, false],
[2, true, false],   ## 2 only exist in the first list
[3, true, true],    ## 3 exist in both lists
[4, true, true],
[5, false, true]
]
```


## Solution1

Use native list operation


```python
def FindDifferences():    
    df1 = pd.read_csv('Gmax_v6_annotation_info.txt', names=['name'], usecols=[0], delimiter='\t')
    df2 = pd.read_csv('Gmax_v9_annotation_info.txt', names=['name'], usecols=[2], delimiter='\t')
    v6_set = set(df1['name'])
    v9_set = set(df2['name'])
    result = []
    for val in v6_set:
        if val in v9_set:
            result.append([val, True, True])
        else:
            result.append([val, True, False])
    for val in v9_set:
        if val not in v6_set:
            result.append([val, False, True])
    result_df = pd.DataFrame(result, columns=['name', 'inv6', 'inv9'])
    result_df.to_csv('result_csv.csv', index=False, header=False)
    return

```

## Solution2

Use pandas dataframe merge and indication

```python
In [13]: def pandas_solution():
    ...:     df1 = pd.read_csv('Gmax_v6_annotation_info.txt', names=['name'], usecols=[0], delimiter='\t')
    ...:     df2 = pd.read_csv('Gmax_v9_annotation_info.txt', names=['name'], usecols=[2], delimiter='\t')
    ...:     df1.merge(df2, how='outer', indicator=True).assign(inv6 = lambda x:x._merge != "right_only", inv9 = lambda x:x._merge != "left_only").drop("_merge", 1).to_csv('resultcsv.csv')

```

## Results


```
In [7]: %timeit FindDifferences()
1 loop, best of 3: 386 ms per loop

In [16]: %timeit pandas_solution()
1 loop, best of 3: 389 ms per loop

```

## Insight

Amazingly, they almost have no performance difference. I did run multiple times using timeit and yield roughly the same result.
I will look into how merge in pandas work and the time complexity in both of the solutions. I originally thought the pandas merge
solution will outperform the native list solution significantly
