#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solve():
    movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
    first = movies[:10]
    last = movies[-15:]
    second = movies[12:26]
    second_last = movies[-22:-16]
    return [first, last, second, second_last]


