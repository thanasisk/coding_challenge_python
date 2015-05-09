#!/usr/bin/env python
# -*- coding: utf-8 -*-

import model
from model import Basket, Item, Promotion, Redemption
import random
import time
import json

item_titles = [ "bread", "chicken", "keys", "pen", "burger", "book", "speaker",
        "CD", "DVD", "cup", "thumbdrive", "caviar", "joghurt", "magazine"]
items = []
def gtins():
    return random.randint(0,100)+1000

def ts():
    return random.getrandbits(64)

def price():
    return random.randint(1,10000)

for title in item_titles:
    tmp = Item(title, gtins(), price())
    items.append(tmp)

tmp = Basket(ts(), items)
print tmp.toJSON()
