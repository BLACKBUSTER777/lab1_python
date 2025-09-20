#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solve():
    my_family_height = [
        ['папа', 180],
        ['мама', 165],
        ['я', 175],
    ]

    father_height = my_family_height[0][1]
    total_height = sum(member[1] for member in my_family_height)

    return {"father_height": father_height, "total_height": total_height}


