## Exercicio 314.  Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro ficou alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado. Nilo Ney Coutinho Menezes

Dias = float(input('Por quantos dias o carro ficou alugado? '))
Km = float(input('Quantos quilômetros você rodou com o carro? '))
Preço = (Dias * 60) + (Km * 0.15)
print('Você ficou com nosso carro {} dias e rodou {} quilômetros e deve pagar um valor de R$ {}.'.format(Dias, Km, Preço))