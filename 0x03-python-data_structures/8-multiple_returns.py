#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None or len(sentence) == 0:
        first = None
        length = 0
    
    else:
        first = sentence[0]
        length = len(sentence)

    tuple_t = (length, first)
    return tuple_t
