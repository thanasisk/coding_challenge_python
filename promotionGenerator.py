#!/usr/bin/env python

import json
import random
from model import Promotion

REPS =  1024 

promos = []
print "{\"promotions\": ["
for i in xrange(REPS):
    peep = []
    for x in xrange(random.randint(1,5)):
            peep.append(1000+random.randint(0,50))
    tmp = Promotion("Promo %d" % i, random.randint(1,99), peep)
    if i < REPS-1:
        print tmp.toJSON()+","
    else:
        print tmp.toJSON()
print "]}"
