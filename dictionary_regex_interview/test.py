import timeit
import re

def regex(s):
    splitted_result = re.find_all('(\w)\1+', s)
    # TODO may do a timing analysis on native iteration
    
