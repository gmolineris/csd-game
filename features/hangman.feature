
Feature: Hangman game init

Scenario: Usuario inicia Hangman
	Given juego ejecutandose
	Then juego muestra Hangman

Scenario: Usuario ingresa una letra correcta
	Given juego ejecutandose
	And usuario inicia nueva partida
	When ingresa letra A
	Then juego muestra aciertos
