#!/usr/bin/env python

import json
import random
from model import Basket, Item, Promotion, Redemption

REPS = 100

for i in xrange(REPS):
    tmp = Promotion("Promo %d" % i, random.randint(1,99), 1000+i)
    print json.dumps(tmp.__dict__)
