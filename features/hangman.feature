Feature: Hangman game init

Scenario: Usuario inicia Hangman
	Given juego ejecutandose
	Then juego muestra Hangman

Scenario: Usuario descubre la letra
	Given juego ejecutandose
    When usuario ingresa la letra i
    Then sistema indica juego exitoso

Scenario: Usuario pierde el juego
	Given juego ejecutandose
    When usuario ingresa la letra A
    Then sistema indica juego fallido
