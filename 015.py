km = float(input('quantos km foram rodados pelo o carro'))
dias = int(input('quantos dias o carro ficou com o cliente'))
vf = dias * 60 + km * 0.15
print('O valor a ser pago pelo o cliente e igual a {:.2f}'.format(vf))
