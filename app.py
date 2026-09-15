def calcular_salario(valor_hora, horas_trabalhadas):
    if valor_hora < 0 or horas_trabalhadas < 0:
      ValueError('Não pode ser negativo')
    return valor_hora * horas_trabalhadas
valor_hora = float(input('Digite quanto voce ganha por hora: '))
horas = float(input('Digite quantas horas voce trabalha no mês: '))
        
salario = calcular_salario(valor_hora, horas)
print(f'Seu salário do mês é: R${salario}')