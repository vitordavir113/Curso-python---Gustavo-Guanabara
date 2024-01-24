Salario = int(input('Insira o salario do funcionario'))
Porcentagem = int(input('Insira o valor do aumento em formato de porcentagem'))
valormp = Salario*Porcentagem/100 + Salario
print('O novo salario do funcionario e igual a {}',format(valormp))