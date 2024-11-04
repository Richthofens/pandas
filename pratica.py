import pandas as pd
from IPython.display import display

vendas_pd = pd.read_excel('Vendas.xlsx')

# display(vendas_pd[['ID Loja', 'Produto', 'Quantidade', 'Valor Final']])   #Mostrando as colunas especificas

vendas_pd['Total Vendas'] = vendas_pd['Quantidade'] * vendas_pd['Valor Unitário']
# display(vendas_pd[['Quantidade', 'Valor Unitário', 'Total Vendas']])   #Adicionando uma nova com coluna, somando o valor total das vendas

# ven_cam = vendas_pd.loc[vendas_pd['Produto'] == 'Camiseta']    #Procurar linhas aonde só tenha 'Camiseta'
# tot_cam = ven_cam['Total Vendas'].sum()    #Pegando o valor total da soma de todas as 'Camisetas'
# print(f"Total geral de vendas de camisetas: {tot_cam}R$")

total_por_produto = vendas_pd.groupby('Produto')['Total Vendas'].sum()
print(total_por_produto.head(50))