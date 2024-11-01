import pandas as pd
from IPython.display import display

# vendas = {
#     'data': ['15/02/2021', '10/02/2021'],
#     'valor': ['500', '320'],
#     'produto': ['feijão', 'arroz'],
#     'qtde': ['50', '70']
# }

# vendas_df = pd.DataFrame(vendas)

# print(vendas_df)
# display(vendas_df)


# # #Trabalhando com tabela real
vendas_df = pd.read_excel('Vendas.xlsx')    #Adicionar a tabela à uma variavel
# display(vendas_df) #Mostra a tabela

# display(vendas_df.head(10))   #Mostra o topo da tabela
# print(vendas_df.shape)            #Mostra quantidade de linhas e colunas da tabela
# display(vendas_df.describe())         #Mostra uma descrição da tabela



# #Mostrar uma coluna especifica
# produtos = vendas_df['Produto']   #Quando for só uma coluna é uma Serie
# produtos = vendas_df[['Produto', 'ID Loja']]    #Mostrando duas colunas
# display(produtos)   #Não é um DataFrame, sim uma tabale da Tabela principal


# #Metodo Loc
display(vendas_df.loc[1])   #Mostra uma linha especifica a partir do indíce

# #Pegar linha que corresponde a uma condição
# display(vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping'])    #Usar o display ja com a condição

# vendas_norteshopping = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping']    #Armazena a variavel da loja com a condição
# display(vendas_norteshopping)   #Mostrar a variavel com a condição


# #Pegar varias linhas e colunas com o loc
# vendas_norteshopping = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ['ID Loja', 'Produto', 'Quantidade']]  #Pegando linha e coluna especifica
# display(vendas_norteshopping)

# #Pegar valor especifico
cam = vendas_df.loc[vendas_df['Produto'] == 'Camiseta', ['ID Loja', 'Quantidade']]  #Com a variavel
display(cam)

print(vendas_df.loc[1, 'Produto'])  #Buscando direto com Indíce e nome da coluna, irá retornar 'Camiseta'