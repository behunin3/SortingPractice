import random
import time

def Rand(start, end, num):
    random.seed(time.time())
    res = []
 
    for j in range(num):
        res.append(random.randint(start, end))
 
    return res