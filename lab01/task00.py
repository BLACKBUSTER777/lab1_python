#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solve():
    sites = {
        'Moscow': (550, 370),
        'London': (510, 510),
        'Paris': (480, 480),
    }

    distances = {}
    for city1, coord1 in sites.items():
        distances[city1] = {}
        for city2, coord2 in sites.items():
            if city1 == city2:
                distances[city1][city2] = 0
            else:
                distances[city1][city2] = (
                    (coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2
                ) ** 0.5
    return distances







