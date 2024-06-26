
'''while True:
    cpf_digitado = input('Digite seu CPF: ')
    nove_digitos = cpf_digitado[:9]
    multiplicador_regressivo_1 = 10
    multiplicador_regressivo_2 = 11

    if len(cpf_digitado) > 11:
            print('CPF inválido, tente novamente.')
            continue

    resultado_1 = 0
    for digito in nove_digitos:
        resultado_1 += int(digito) * multiplicador_regressivo_1
        multiplicador_regressivo_1 -= 1
    
    digito_1 = (resultado_1 * 10) % 11
    digito_1 = digito_1 if digito_1 < 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    
    resultado_2 = 0
    for digito in dez_digitos:
         resultado_2 += int(digito) * multiplicador_regressivo_2
         multiplicador_regressivo_2 -= 1
    
    digito_2 = (resultado_2 * 10) % 11
    digito_2 = digito_2 if digito_2 > 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    #print(digito_1)
    #print(digito_2)

    if cpf_digitado == cpf_gerado_pelo_calculo:
        print(f'{cpf_digitado} é válido')
    else:
        print('CPF inválido')
   ''' 
import re
import sys

while True:
    entrada = input('Digite seu CPF: ')
    cpf_enviado_usuario = '084.311.285-93'
    cpf_enviado_usuario = re.sub(r'[^0-9]', '', entrada)

    entrada_e_sequencial = entrada == entrada[0] * len(entrada)

    if entrada_e_sequencial:
        print('Você enviou dados sequenciais, tente novamente')
        continue

    nove_digitos = cpf_enviado_usuario[:9]
    contador_regressivo_1 = 10

    resultado_digito_1 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
        print(f'{cpf_enviado_usuario} é válido')
        break
    else:
        print('CPF inválido')
        continue
