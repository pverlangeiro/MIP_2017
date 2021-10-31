import os
import pandas as pd
import numpy as np


df = pd.read_excel('teste_1.xlsx')
matrix = df[['primario', 'secundario','terciario']]
x = df['x']
matrix_coef_tecnico = pd.DataFrame()

for i in range(0, 3):
    df_temp = matrix.iloc[0:3, i]/x[i]
    matrix_coef_tecnico = pd.concat([matrix_coef_tecnico, df_temp], axis=1)

matrix_coef_tecnico.to_excel('matrix_coef_tecnico.xls')

matrix_coef_tecnico = np.array(matrix_coef_tecnico)
matrix_identidade = np.identity(3)

matrix_i_menos_A = matrix_identidade - matrix_coef_tecnico
leontief = np.linalg.inv(matrix_i_menos_A)
leontief_2 = leontief
