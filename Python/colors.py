#style          text         background
#0 = none       30 = white   40 = white
#1 = bald       31 = red     41 = red
#4 = underlined 32 = green   42 = green
#7 = negative   33 = yellow  43 = yellow
#               34 = blue    44 = blue
#               35 = purple  45 = purple
#               36 = cyan    46 = cyan
#               37 = grey    47 = grey

print("\033[0;30;40mOlá, Mundo!\033[m")
print("\033[1;30;40mOlá, Mundo!\033[m")
print("\033[4;30;40mOlá, Mundo!\033[m")
print("\033[7mOlá, Mundo!\033[m")

print("\033[30;41mOlá, Mundo!\033[m")
print("\033[31;42mOlá, Mundo!\033[m")
print("\033[32;43mOlá, Mundo!\033[m")
print("\033[33;44mOlá, Mundo!\033[m")
print("\033[34;45mOlá, Mundo!\033[m")
print("\033[35;46mOlá, Mundo!\033[m")
print("\033[36;47mOlá, Mundo!\033[m")
print("\033[37;40mOlá, Mundo!\033[m")

a = 3
b = 5
name = 'Saulo'
colors = {'clean':'\033[m',
          'azul':'\033[34m',
          'amarelo':'\033[33m',
          'preto e branco':'\033[7:30m'}

print(f"Olá! Muito prazer em te conhecer, {colors['amarelo']}{name}{colors['clean']}!!!")

print(f'Os valores são \033[31;40m{a}\033[m e \033[32;40m{b}\033[m.')
