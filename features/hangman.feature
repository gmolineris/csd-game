Feature: Hangman game init

Scenario: Usuario inicia Hangman
	Given juego ejecutandose
	Then juego muestra Hangman

Scenario: Usuario descubre la letra
	Given juego ejecutandose
    When usuario ingresa la letra a
    Then sistema indica OOOOOO

Scenario: Usuario pierde el juego
	Given juego ejecutandose
    When usuario ingresa la letra i
    Then sistema indica XOOOOO

#Scenario: Descubre una letra de una palabra
#    Given juego ejecutandose
#    When usuario ingresa la palabra li
#    Then sistema indica XXXXXX

#Scenario: Descubre la palabra completa
#    Given juego ejecutandose
#    When usuario ingresa la palabra palabra
#    Then sistema indica OOOOOO
#    And sistema muestra la palabra pacial palabra
