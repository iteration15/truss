from lettuce import *
from nose.tools import assert_equals
import app.norm_csv

@step(u'I am using a csv file with broken content')
def reformat_timestamp(step)
    print ('attempting to reformat timestamp...')
    world.reformat = Norm_csv()
