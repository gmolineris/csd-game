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

@when(u'usuario ingresa la letra {letra}')
def step_impl(context, letra):
    browser.fill('word',letra)
    browser.find_by_id('checkButton')[0].click()    

@then(u'sistema indica juego exitoso')
def step_impl(context):
    assert 'True' in browser.html

@then(u'sistema indica juego fallido')
def step_impl(context):
    assert 'False' in browser.html
