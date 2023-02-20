t=('Corithians','Sao Paulo','palmeiras','Santos','Juventude','Flamengo','Atletico-MG','Gremio','Vasco'
'Fluminense','Chapecoense','Bahia','Cuiaba','Curitiba','Cruzeiro','Gremio','Internacional','Bragantino','Portuguesa','Atletico')

print(f'Lista de time {t}')
print('-'*30)
print(f'Os primeiros 5 colocados são {t[0:5]}')
print('-'*30)
print(f'Esse são os 4 ultimos {t[-4:]}')
print('-'*30)
print(f'Essa é a lista em ordem alfabetica {sorted(t)}')
print('-'*30)
print(f'O time Chapecoense está na posição {t.index("Chapecoense") + 2}')#Não consegui