from lettuce import *
from nose.tools import assert_equals
from app import norm_csv

@step(u'I am using a csv file with broken content')
def reformat_timestamp(step):
    print ('attempting to use normalizer...')
    world.reformat = Normalize()
