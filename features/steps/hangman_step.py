from hangman import *
from behave import *
from splinter import Browser
browser = Browser('flask',app=app)

@given(u'juego ejecutandose')
def step_impl(context):
	browser.visit('http://127.0.0.1:5000')

@then(u'juego muestra {gameName}')
def step_impl(context, gameName):
    	assert gameName in browser.html
