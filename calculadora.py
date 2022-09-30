largura_garagem = float(input("Entre com a largura da garagem em metros :"))
profundidade_garagem = float(input("Entre com a profundidade da garagem em metros :"))
#abaixo, cálculo da largura garagem * profundidade garagem
area_garagem = largura_garagem * profundidade_garagem
largura_terreno = float(input("Entre com a largura do terreno em metros :"))
profundidade_terreno = float(input("Entre com a profundidade do terreno :"))
#abaixo,cálculo da área do terreno * profundidade terreno
area_terreno = largura_terreno * profundidade_terreno
#agora, cálculo do percentual de ocupação 
percentual = ((area_garagem)/(area_terreno))*100
print("Resultado é ",percentual)
answer = input("Projeto finalizado : ") 
if answer == "sim": 
    # Do this.
  print("Parabéns")
elif answer == "não": 
    # Do that. 
  print("Então, bora terminar")
else: 
    print("Apenas sim ou não.")
