import pandas as pd
from IPython.display import display

vendas_pd = pd.read_excel('Vendas.xlsx')

# display(vendas_pd[['ID Loja', 'Produto', 'Quantidade', 'Valor Final']])   #Mostrando as colunas especificas


# vendas_pd['Total Vendas'] = vendas_pd['Quantidade'] * vendas_pd['Valor Unitário']   #Adicionando a culuna 'Total Vendas' (quantidade x valor unitário)
# display(vendas_pd[['Quantidade', 'Valor Unitário', 'Total Vendas']])   #Adicionando uma nova com coluna, somando o valor total das vendas


# ven_cam = vendas_pd.loc[vendas_pd['Produto'] == 'Camiseta']    #Procurar linhas aonde só tenha 'Camiseta'
# tot_cam = ven_cam['Total Vendas'].sum()    #Pegando o valor total da soma de todas as 'Camisetas'
# print(f"Total geral de vendas de camisetas: {tot_cam}R$")


# total_por_produto = vendas_pd.groupby('Produto')['Total Vendas'].sum()
# print(total_por_produto.head(15))    #Calculando o valor total de todos os Produtos


# loja_esp = vendas_pd.loc[vendas_pd['ID Loja'].isin(['Iguatemi Esplanada', 'Norte Shopping'])]   #Filtrando para que mostre somente as vendas de duas lojas
# display(loja_esp)   #O Isin faz com que verifique se o iten está na lista, como o loc não pode receber uma lista com argumento


# #Filtrando vendas por mês e ano
# vendas_pd['Data'] = pd.to_datetime(vendas_pd['Data'])   #Adicionando a culuna de data


#vendas de janeiro de 2019
# jan_2019 = vendas_pd.loc[(vendas_pd['Data'].dt.month == 1) & (vendas_pd['Data'].dt.year == 2019)] 
# display(jan_2019)   #Filtrando as vendas de mês e ano com 'pd.to_datetime'


vendas_loja = vendas_pd['ID Loja'].value_counts()
display(vendas_loja)