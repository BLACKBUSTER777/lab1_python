#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solve():
    goods = {
        'Лампа': '12345',
        'Стол': '23456',
        'Диван': '34567',
        'Стул': '45678',
    }

    store = {
        '12345': [{'quantity': 27, 'price': 42}],
        '23456': [{'quantity': 22, 'price': 510}, {'quantity': 32, 'price': 520}],
        '34567': [{'quantity': 2, 'price': 1200}, {'quantity': 1, 'price': 1150}],
        '45678': [{'quantity': 50, 'price': 100}, {'quantity': 12, 'price': 95}, {'quantity': 43, 'price': 97}],
    }

    lamps = store[goods['Лампа']][0]
    lamp_quantity = lamps['quantity']
    lamp_cost = lamps['quantity'] * lamps['price']

    table1, table2 = store[goods['Стол']]
    table_quantity = table1['quantity'] + table2['quantity']
    table_cost = table1['quantity'] * table1['price'] + table2['quantity'] * table2['price']

    sofa1, sofa2 = store[goods['Диван']]
    sofa_quantity = sofa1['quantity'] + sofa2['quantity']
    sofa_cost = sofa1['quantity'] * sofa1['price'] + sofa2['quantity'] * sofa2['price']

    chair1, chair2, chair3 = store[goods['Стул']]
    chair_quantity = chair1['quantity'] + chair2['quantity'] + chair3['quantity']
    chair_cost = (
        chair1['quantity'] * chair1['price']
        + chair2['quantity'] * chair2['price']
        + chair3['quantity'] * chair3['price']
    )

    return {
        "Лампа": {"quantity": lamp_quantity, "cost": lamp_cost},
        "Стол": {"quantity": table_quantity, "cost": table_cost},
        "Диван": {"quantity": sofa_quantity, "cost": sofa_cost},
        "Стул": {"quantity": chair_quantity, "cost": chair_cost},
    }


