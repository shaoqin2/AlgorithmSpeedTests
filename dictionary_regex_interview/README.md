# This is a test to see my implementation using hash map in the interview versus the suggested regex solution performance.

Problem statement:  
Find the longest repeating character string.

Example in:  
"aaaabbccccccdd"

Example out:
 c : 6

 ### Solution 1:

 read through the string and whenever there's a change in character, reset the counter and put the pair in the hash map. Record the maximum as well.


 ### Solution 2:

 Use regular expression to split all repeating substring, test against the length of each substring

 ### Result


```python
In [30]: short_string = "aaaaaabbbbcccddddeeeeeeeeeeeeeeeeeeeeeeee"

```
