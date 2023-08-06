#!/usr/bin/env python3
"""Módulo para tokanizar livros"""
__version__ = "0.4"

import sys
import re

output = 'stdout'
input = 'stdin'
has_poems = False
encoding = 'utf8'

def main():

    # Processar argumentos e ver os erros de argumentos
    args = " ".join(sys.argv[1:])
    if '-' in args:
        args = args.split('-')
        tmpInput = args[0]
        args = args[1:]
        flags = []

        #Verificar se existe ficheiro de input
        if(not tmpInput == ''):
            input = tmpInput

        #Verificar flags
        for arg in args:
            flag = arg[0]
            arg = arg[len(flag):]
            if flag in flags: print(f"Error: Duplicated flag: {flag} ")
            else: flags.append(flag)
            if flag == 'p':
                has_poems = True
            elif flag == 'o':
                output = arg.strip()
            elif flag == 'e':
                encoding = arg.strip()
            else:
                print(f'Error: This flag: {flag} do not exist.')
    else:
        input = args   

    text = ""  
    if(input == 'stdin'):
        for line in sys.stdin:
            text+=line
    else:   
        file = open(input,'r',encoding=encoding)
        text = file.read()
        file.close()



    # 0. Tratar poemas

    list_poemas = []

    def save_poems(poema):
        """Saves a poem in a data structure"""
        list_poemas.append(poema[1])
        return f">>{len(list_poemas)}<<"

    if has_poems:
        regex_poema = r'<poem>(.*?)</poem>'
        text = re.sub(regex_poema,save_poems,text,flags=re.S)

    # 1. Quebra de pagina

    regex_nl = r'([a-z0-9,;-])\n\n([a-z0-9,;-])'
    text = re.sub(regex_nl,r'\1\2',text)

    # 2. Marcar capitulos

    regex_cap = r'.*(CAPÍTULO +(\w+|\d+)).*'
    text = re.sub(regex_cap,r'\n# \1',text)

    # 3. Separar paragrafos de linhas pequenas

    regex_par = r'([.!?;])\n(([^.!?;]|[\u00C0-\u017F]))'
    text = re.sub(regex_par,r'\1\n/PAR/ \2',text)

    # 4. Juntar linhas da mesma frase

    regex_line = r'([^.!?])\n+([^.!?])'
    text = re.sub(regex_line,r'\1 \2',text)

    # 5. Separar pontuação das palavras.

    regex_pont = r'([.!,?;:' + r'\"\-\”\–\`()\[\]])?(\w+)([.!,?;:' + r'\"\-\”\–\`()\[\]])'
    text = re.sub(regex_pont,r'\1 \2 \3',text)

    # Save to arquive
    if(output == 'stdout'):
        print(text)
        if(has_poems):
            print('-----POEMS-----')
            for poema in list_poemas:
                print(poema)
                print('-----//-----')

    else:
        file = open(output,'w',encoding="utf-8")
        file.write(text)
        file.close()
        if(has_poems):
            file = open('poems-'+output,'w',encoding="utf-8")
            file.write('-----POEMS-----')
            for poema in list_poemas:
                file.write(poema)
                file.write('-----//-----')