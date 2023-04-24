print('Turno da criatura atacante')

armadura = 12
destreza = 10
forca = 15
consistencia_criatura = 12

import random

d20_criatura = random.randint(1, 20)

d8_01_criatura = random.randint(1, 8)
d8_02_criatura = random.randint(1, 8)

ataque_criatura = d8_01_criatura + d8_02_criatura

print('Prepare-se, a criatura jogou os dados!')

print('Turno do jogador')

valor_armadura = int(input('Qual seu valor de armadura?'))
valor_destreza = int(input('Qual seu valor de destreza?'))
valor_forca = int(input('Qual seu valor de força?'))
consistencia = int(input('Qual seu valor de consistência? '))
vida = int(input('E qual a sua vida atual?'))

# valor consistência final
if consistencia > 6 and consistencia <= 11:
    consistencia = consistencia + 1
elif consistencia > 11 and consistencia <= 18:
    consistencia = consistencia + 2
elif consistencia > 18:
    consistencia = consistencia + 3
else:
    consistencia = consistencia + 0
    
# valor força final
if valor_forca > 6 and valor_forca <= 11:
    valor_forca = valor_forca + 1
elif valor_forca > 11 and valor_forca <= 18:
    valor_forca = valor_forca + 2
elif valor_forca > 18:
    valor_forca = valor_forca + 3
else:
    valor_forca = valor_forca + 0
    
# valor destreza final
if valor_destreza > 6 and valor_destreza <= 11:
    valor_destreza = valor_destreza + 1
elif valor_destreza > 11 and valor_destreza <= 18:
    valor_destreza = valor_destreza + 2
elif valor_destreza > 18:
    valor_destreza = valor_destreza + 3
else:
    valor_destreza = valor_destreza + 0
    


hipotese_inicial = str(input('você vai receber, esquivar ou contratacar a criatura? '))

print('ok... rolando 1d20')

d20 = random.randint(1, 20)

print(f'Você tirou um {d20} no dado!')

# calcular a tentativa de resistir ao ataque
if hipotese_inicial == 'resistir' or hipotese_inicial == 'defender' or hipotese_inicial == 'receber':
    
    dano_criatura = ataque_criatura - consistencia + valor_armadura
    
    print(f'A criatura tirou {ataque_criatura} no dado...')
    
    print(f'Você recebeu {dano_criatura} de dano!')
    
    if vida <= dano_criatura:
        print('É... ocê morreu')
    elif vida > dano_criatura and vida < 2:
        print('Essa foi por pouco!')
    else:
        print('DAMN!!!')
        

# calcular o contra ataque
elif hipotese_inicial == 'contratacar' or hipotese_inicial == 'revidar':

    dano_criatura = ataque_criatura - consistencia + armadura
    dano_player = consistencia_criatura + armadura - valor_forca
        
    print(f'Você recebeu {dano_criatura} mas causou {dano_player} de dano na criatura!')
    
    if vida <= dano_criatura:
        print('É... ocê morreu')
    elif vida > dano_criatura and vida < 2:
        print('Essa foi por pouco!')
    else:
        print('DAMN!!!')

# calcular o desvio do ataque
elif hipotese_inicial == 'esquivar' or hipotese_inicial == 'desviar':
    
    if valor_destreza >= 20 and d20_criatura < 20:
        dano_criatura = 0
    elif valor_destreza  > 15 and valor_destreza < 20:
        dano_criatura = (ataque_criatura - consistencia + armadura) - 4 + 1
    elif valor_destreza  > 12 and valor_destreza < 15:
        dano_criatura = (ataque_criatura - consistencia + armadura) - 2 + 1
    else:
        dano_criatura = ataque_criatura - consistencia + armadura
        
        print(f'Você não conseguiu desviar... A criatura te acertou e causou {dano_criatura} de dano!')
        
        if vida <= dano_criatura:
            print('É... você morreu')
        elif vida > dano_criatura and vida < 2:
            print('Essa foi por pouco!')
        else:
            print('DAMN!!!')
        
else:
    print('Algo deu errado xd')
