    #Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    urllib.request.urlopen("https://www.pudim.com.br")
except:
    print("O site não está acessível!")
else:
    print("O site está acessível!")