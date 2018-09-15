from behave import *
from norm_csv import *

@given('an {infile} and {outfile} are received')
def step_impl(context, infile, outfile):
    context.normalize = Normalize(infile, outfile)

#@when('the timestamp read "4/1/11 11:00:00 AM"')
