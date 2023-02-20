import urllib

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')

except:
    print('O site Pudim não está disponivel no momento')

else:
    print('O site pudim está disponivel')
    # print(site.read())
