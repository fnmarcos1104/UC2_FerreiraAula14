# import pandas as pd
import polars as pl
import numpy as np
from datetime import datetime
import os
import gc
from matplotlib import pyplot as plt


ENDERECO_DADOS = r'./Dados/'

try:
    print('\nIniciando leitura do arquivo parquet...')

    inicio = datetime.now()

    # df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    df_bolsa_familia_plan = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    df_bolsa_familia = df_bolsa_familia_plan.collect()

    print(df_bolsa_familia)

    fim = datetime.now()

    print(f'Tempo de execução para leitura do parquet: {fim - inicio}')
    print('\nArquivo parquet lido com sucesso!')

except ImportError as e:
    print('Erro ao ler dados do parquet', e)


try:
    print('Visualizando a distribuição dos valores das parcelas em um boxplot...')

    hora_inicio = datetime.now()

    array_valor_parcela = np.array(df_bolsa_familia['VALOR PARCELA'])

    plt.boxplot(array_valor_parcela, vert=False)
    plt.title('Distribuição dos valores das parcelas')

    hora_fim = datetime.now()

    plt.show()

    print(f'Tempo de execução: {hora_fim - hora_inicio}')

except ImportError as e:
    print('Erro ao ler boxplot', e)


# try:
#     print('Obtendo dados...')
   
#     inicio = datetime.now()

#     lista_arquivos = []

#     lista_dir_arquivos = os.listdir(ENDERECO_DADOS)
 
#     # print(f'Tempo de execução: {hora_impressao - inicio}')

#     for arquivo in lista_dir_arquivos:
#         if arquivo.endswith('.csv'):
#             lista_arquivos.append(arquivo)

#     # print(lista_arquivos)

#     for arquivo in lista_arquivos:
#         print(f'Processando arquivo {arquivo}')

#         df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')

#         if 'df_bolsa_familia' in locals():
#             df_bolsa_familia = pl.concat([df_bolsa_familia, df])
#         else:
#             df_bolsa_familia = df
        
#         del df

#         print(df_bolsa_familia.head())

#         gc.collect()

#         print(f'Arquivo {arquivo} processados com sucesso!')

        

#     df_bolsa_familia.write_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

#     del df_bolsa_familia

#     gc.collect()

#     fim = datetime.now()
    
#     print(f'Tempo de execução: {fim - inicio}')



 
# except ImportError as e:
#     print('Erro ao obter dados', e)