#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solve():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
    zoo.insert(1, 'bear')

    birds = ['rooster', 'ostrich', 'lark']
    zoo.extend(birds)

    if 'elephant' in zoo:
        zoo.remove('elephant')

    lion_pos = zoo.index('lion') + 1
    lark_pos = zoo.index('lark') + 1

    return {"zoo": zoo, "lion_cell": lion_pos, "lark_cell": lark_pos}


