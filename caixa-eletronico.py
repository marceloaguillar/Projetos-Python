
#ANALISAR ESTOQUE
caixa = [100,50,20,10,5,2]

#SELECIONAR MENORES NOTAS
def e_caixa(valor):
    saque = {100:0, 50:0, 20:0, 10:0, 5:0, 2:0}
    for i in caixa:
        while i <= valor:
            valor -= i
            saque[i] += 1
            
            if valor <= 0:
                break
                
    
    for chave in list(saque.keys()):
        if saque[chave] == 0:
            del saque[chave]
    return saque
    

#VALOR DESEJADO 
valor = int(input('DIGITE O VALOR QUE DESEJA: '))

#MOSTRAR NOTAS LIBERADAS
print(e_caixa(valor))