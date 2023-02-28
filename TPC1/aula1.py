# ZEP -> E*
# E -> EC
#    | ER
# EC -> num pals pos CORPO
# CORPO -> area LINGUAS
# LINGUAS -> pt pals
#          | en pals
#          | es pals
# ER -> pals VID
# VID -> Vid.- pals

import re

texto = open('medicina.xml', 'r').read()

def remove_fontspec(texto):
    texto = re.sub(r'\t<fontspec.*>', r'', texto)
    return texto

texto = remove_fontspec(texto)


def remove_header_footer(texto):
    texto = re.sub(r'<text.* font="1">ocabulario.*</text>', r'###', texto)
    texto = re.sub(r'.*\n###\n.*\n', r'___', texto)
    texto = re.sub(r'<page.*\n|</page>\n', r'', texto)
    
    return texto

texto = remove_header_footer(texto)

def marcaLinguas(texto):
    texto = re.sub(r'<text.* width\=\"24\".*> *(es|pt|la|en) *<\/text>\n<text.*><i>(.*)<\/i><\/text>', r'@ \1 \2', texto)
    # @
    return texto

texto = marcaLinguas(texto)



# dicionario

def marcaEC(texto):
    texto = re.sub(r'<text.* font="3"><b>\s*(\d+.*)</b></text>', r'## \1', texto)
    return texto

def marcaER(texto):
    texto = re.sub(r'<text.* font="3"><b>\s*(\S.*)</b></text>', r'### \1', texto)
    return texto

texto = marcaEC(texto)
texto = marcaER(texto)

def simpletext(texto):
    texto = re.sub(r'<text.*> *; *<\/text>', r'', texto)
    texto = re.sub(r'<text.* width\=\"24\".*> *(.*) *<\/text>', r'\1', texto)
    texto = re.sub(r'<text.*><i>? *(.*)<\/i>?<\/text>', r'\1', texto)
    texto = re.sub(r'<text.*>(<b>)? *(<\/b>)?<\/text>', r'', texto)
    texto = re.sub(r'<text.*> *(.+)<\/text>', r'\1', texto)
    return texto


texto = simpletext(texto)

def remove_empty(texto):
    texto = re.sub(r'<text.*>(<b>)? *(<\/b>)?<\/text>', r'', texto)
    return texto

texto = remove_empty(texto)

file = open('medicina2.txt', 'w')

file.write(texto)