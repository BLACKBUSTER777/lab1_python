#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solve():
    garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')
    meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

    garden_set = set(garden)
    meadow_set = set(meadow)

    return {
        "all": garden_set | meadow_set,
        "both": garden_set & meadow_set,
        "garden_only": garden_set - meadow_set,
        "meadow_only": meadow_set - garden_set,
    }


