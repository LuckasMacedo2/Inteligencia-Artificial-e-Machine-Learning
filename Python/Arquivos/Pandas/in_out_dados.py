# -------------------- Entrada e saida de dados ---------------------------

import numpy as np
import pandas as pd

# Metodo: read_csv('caminho_do_arquivo', sep = ';')
# Parametro 1: O caminho em que o arquivo se encontra.
# Parametro sep: O separador, que separa os elementos.

# Metodo: df.to_csv('caminho_do_arquivo', sep = ';')
# Transforma o data frame em um arquivo csv.

# Metodo: pd.read_excel ('caminho_do_arquivo', sheetname = 'sheet1')
# Permite ler os dados da planilha do excel.
# Parametro 1: O caminho em que o arquivo se encontra.
# sheetname: Aba da planilha que sera lida.

# Metodo: df.to_excel('caminho_do_arquivo', sheet_name = 'sheet1')
# Parametro 1: O caminho em que o arquivo se encontra.
# sheet_name: Nomeia a aba.

# Metodo: pd.read_html('link do site')
# Permite transformar dados html em um data frame.

df = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
print (df)
