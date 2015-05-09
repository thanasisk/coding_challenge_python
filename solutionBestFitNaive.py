#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import itertools
# bad style?
import model
from model import Basket, Redemption


def loadJSON(fname):
    with open(fname, "rb") as ifile:
        tmp = ifile.read()
        obj = json.loads(tmp)
    return obj


def redeem(basket, promotions):
    # let's try to reduce the dataset - maybe not all items have applicable
    # discounts
    totalSavings = 0
    redemptions = []
    basket = trimBasket(basket, promotions)
    # sort in ascending order items and promotions
    items = sorted(basket.items, reverse=True)
    promotions = sorted(promotions)
    while promotions != []:
        # for each promotion, try to apply it to the most expensive item
        promo = promotions.pop()
        for item in items:
            if item.gtin in promo.gtins:
                redemption = Redemption(item, promo)
                totalSavings += redemption.saved
                redemptions.append(redemption)
                items.pop(0)
                break
    print "By Grabthar's hammer, what a savings: " + str(totalSavings)
    return redemptions

def trimBasket(basket, promotions):
    gtins = []
    for promotion in promotions:
        gtins.append(promotion.gtins)
    # let's flatten gtins
    gtins = list(set(itertools.chain.from_iterable(gtins)))
    # it should have been better named as possible discounted items
    discountedItems = []
    for item in basket.items:
        if item.gtin in gtins:
            discountedItems.append(item)
    return Basket(basket.timestamp, discountedItems)


def main():
    promotions = []
    basketRaw = loadJSON("basket.json")
    basketRaw = loadJSON("datasets/random_basket.json")
    basket = model.dict2Basket(basketRaw)
    promotionsRaw = loadJSON("promotions.json")
    promotionsRaw = loadJSON("datasets/random_promotions.json")
    for promotionRaw in promotionsRaw["promotions"]:
        promotions.append(model.dict2Promotion(promotionRaw))
    redemptions = redeem(basket, promotions)
    for redemption in redemptions:
        print redemption.toJSON()


if __name__ == '__main__':
    sys.exit(main())
