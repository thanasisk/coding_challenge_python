#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

class Basket(object):
    def __init__(self, ts, items):
        self.timestamp = long(ts)
        self.items = items

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                               sort_keys=True, indent=4)

class Item(object):
    def __init__(self, name, gtin, price):
        self.name = name
        self.gtin = gtin
        self.price = price

    def __lt__(self, other):
        return self.price < other.price

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                               sort_keys=True, indent=4)

class Promotion(object):
    def __init__(self, name, discountPercent, gtins):
        self.name = name
        self.discountPercent = discountPercent
        self.gtins = gtins

    def __lt__(self, other):
        return self.discountPercent< other.discountPercent

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                               sort_keys=True, indent=4)

class Redemption(object):
    def __init__(self, item, promotion):
        self.item = item
        self.promotion = promotion
        self.saved = self.item.price * self.promotion.discountPercent / 100

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4)

# some utility methods
def dict2Promotion(rawDict):
    return Promotion(rawDict["name"], rawDict["discountPercent"], list(set(rawDict["gtins"])))


def dict2Item(rawDict):
    return Item(rawDict["name"], rawDict["gtin"], rawDict["price"])


def dict2Basket(rawDict):
    items = []
    ts = rawDict["timestamp"]
    itemsRaw = rawDict["items"]
    for itemRaw in itemsRaw:
        items.append(dict2Item(itemRaw))
    return Basket(ts, items)
