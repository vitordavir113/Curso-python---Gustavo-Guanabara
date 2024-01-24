preço = int(input('Insira o preço do produto que recebera o desconto'))
porcentagem = int(input('Insira a porcentagem do desconto'))
Pcp = preço*porcentagem/100
pf = preço - Pcp
print('O preço novo e igual a {}'.format(pf))