import urllib
import urllib.request
from uteis import cores

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    cores.vermelho('Erro, site não está acessível no momento')
else:
    cores.verde('Tudo ok com o site')

#print(site.read())
#Comando mostra conteudo completo em HTML do site