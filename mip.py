import pandas as pd
import numpy as np
import os
os.getcwd()
os.chdir('/home/luizneto/Documents/invest_ml')

df_1 = pd.read_excel('tab1_recursos.xlsx', sheet_name='producao')
df_2 = pd.read_excel('tab1_recursos.xlsx', sheet_name='importacao')

df_2.columns

df_2.columns = ['codigo', 'produto', 'importacao_bens']

df_2['importacao_servicos'] = df_2['importacao_bens']

df_2['importacao_servicos'][df_2['codigo']  < 40000] = 0
df_2['importacao_bens'][df_2['codigo']  > 40000] = 0

df_ajuste_CIF_FOB = pd.DataFrame(np.zeros((len(df_1), 1)))
df_1['ajuste_CIF_FOB'] = df_ajuste_CIF_FOB[0]

df_1['importacao_servicos'] = df_2['importacao_servicos']
df_1['importacao_bens'] = df_2['importacao_bens']

df_1['total_importacoes'] = df_1['importacao_bens'] + df_1['importacao_servicos']
df_1['oferta_global'] = df_1['total_importacoes'] + df_1['Total\ndo produto']

df_1.to_excel('recursos.xlsx')
