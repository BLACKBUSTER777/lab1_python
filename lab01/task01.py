#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solve():
    radius = 42
    pi = 3.1415926
    area = round(pi * radius ** 2, 4)

    point_1 = (23, 34)
    point_2 = (30, 30)

    inside1 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5 <= radius
    inside2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5 <= radius

    return {"area": area, "point1_inside": inside1, "point2_inside": inside2}
