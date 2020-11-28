#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 19:56:21 2020

@author: darrenhsu
"""

def word_reduce(s, vowel=0, repeat=0, listAll=False):
    vowel_set = {'a','e','i','o','u','A','E','I','O','U'}
    # Assertions
    if type(s) == list:
        pass
    elif listAll == False:
        new_s = ''
        last_c = ''
        vowel_index = 0
        repeat_index = 0
        for c in s:
            # print(c)
            if (c != last_c) or (repeat_index < repeat):
                if last_c == c:
                    repeat_index += 1
                if c in vowel_set:
                    if vowel_index < vowel:
                        new_s += c
                        last_c = c
                        vowel_index += 1
                else:
                    new_s += c
                    last_c = c
    else:
        result_set = []
        prev_result = ''
        for i in range(sum([c in vowel_set for c in s])+1):
            r = 0
            for j in range(len(s)):
                result = word_reduce(s, vowel=i, repeat=r)
                if result != prev_result:
                    result_set.append(result)
                    r += 1
                else:
                    break
        return set(result_set)
                
    return new_s