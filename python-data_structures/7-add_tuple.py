#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_result = []
    for i in range(2):
        value_tup_a = 0 if len(tuple_a) <= i else tuple_a[i]
        value_tup_b = 0 if len(tuple_b) <= i else tuple_b[i]
        tuple_result.append(value_tup_a + value_tup_b)

    return tuple(tuple_result)
