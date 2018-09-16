from behave import *
from norm_csv import *

@given('an {infile} and {outfile} are received')
def step_impl(context, infile, outfile):
    context.normalize = Normalize(infile, outfile)

@when('the user enters the file names')
def step_impl(context):
    context.normalize = Normalize(infile, outfile)

@then('the input file will be normalized')
def step_impl(context):
    context.normalize = Normalize(infile, outfile)
