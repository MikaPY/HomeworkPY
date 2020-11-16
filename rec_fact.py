def rec_fact(n):
    if n == 0:
        return 1
    return rec_fact(n-1) * n

 print(rec_fact(12))