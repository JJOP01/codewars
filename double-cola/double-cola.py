#!/usr/bin/env python3

'''
Problem:

Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine; there are no other people in the queue. The first one in the queue (Sheldon) buys a can, drinks it and doubles! The resulting two Sheldons go to the end of the queue. Then the next in the queue (Leonard) buys a can, drinks it and gets to the end of the queue as two Leonards, and so on.

Solution Approach:

Queue = 0 1 2 3 4, 0 0 1 1 2 2 3 3 4 4, 0 0 0 0 1 1 1 1 2 2 2 2 3 3 3 3 4 4 4 4, ... n*{0,1,2,3,4}

Relative to the initial position, the 1st group ends after 5 people, the 2nd group ends after 5*3 people, the 3rd group ends after 5*7 people, so the kth group ends after g(k) = 5(2^k - 1) people.

We then consider a position n to be a pair (k, d) where k is the last group you passed and d is the distance you are into the next group. With this information, then d/(2^k) is the value at your position, and so, a[d/2^k] is the solution.

To get d, just take n - g(k). To get k, just solve n = g(k) and round down, k = floor(log_2(1 + n/5)).
'''

from math import floor, log2

def get_name_at_position(names, position):
    k   = floor(log2(1 + position/len(names)))
    g_k = len(names)*(2**k - 1)
    d   = position - g_k - 1 # -1 for 0 based index
    return names[d // 2**k]

def tests():
    names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
    positions = [1, 52, 10010]
    for position in positions:
        print(f'Person[{position}] == {get_name_at_position(names, position)}')

if __name__ == '__main__' and '__file__' in globals():
    tests()
