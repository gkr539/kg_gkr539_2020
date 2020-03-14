#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 20:17:59 2020

@author: gouthamkrs
"""
import sys
'''
Assuming every character in s1 should be mapped to a character in s2 but not  vice versa. 
so if length of s1 is less than s2 then return false.
'''

def check_mapping(s1,s2):
    if len(s1) < len(s2):
        return False
    used = set()
    for char in s1:
        if char in used:
            return False
        used.add(char)
    return True


def main():
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    print(check_mapping(s1,s2))
    


if __name__ == '__main__':
    main()

    