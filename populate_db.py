'''
Created on Jul 21, 2012

@author: fabiosl
'''
# -*- coding: utf-8 -*-

import os
import sys, datetime

## Setup to import models from Django app ##
sys.path.append(os.path.abspath('..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'DealScore.settings'

from DealScore import settings
from dealapp.models import *
from django.core.management import setup_environ

setup_environ(settings)

Category.objects.all().delete()
Deal.objects.all().delete()


print "Creating categories" 
men = Category(name="Men")
women = Category (name = "Women")
clothes = Category (name = "Clothes")
shoes = Category(name = "Shoes")
food = Category (name = "Food")

men.save();
women.save();
shoes.save();
food.save();

print "Creating deals" 
deal = Deal (
             business_name="Armani",
             location="West Edmonton Mall", 
             description="60% off on all ties", 
             price = 15, 
             deadline=datetime.datetime.today(), 
             picture_url = "http://www.safestchina.com/products_image/hot-sale-classic-armani-tie-accept-papal-payment-115230.jpg",
             positive_votes = 10,
             negative_votes = 1)
deal.save();


deal = Deal (
             business_name="Abercrombie",
             location="West Edmonton Mall", 
             description="80% off on all Women's Tee's ", 
             price = 20, 
             deadline=datetime.datetime.today(), 
             picture_url = "http://www.bridgat.com/files/Mens_Abercrombie_Tee.jpg",
             positive_votes = 2,
             negative_votes = 10)

deal.save();
