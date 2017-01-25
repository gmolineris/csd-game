from hangman import *
from behave import *
from splinter import Browser
browser = Browser('flask',app=app)

@given(u'App is runing')
def step_impl(context):
	browser.visit('http://127.0.0.1:5000')


