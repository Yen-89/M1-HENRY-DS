import pandas as pd
import numpy as np

import csv
df = pd.read_csv("hospitales2.csv", encoding='utf-8')
tabla = csv.reader(df, delimiter=',')
with open('hosp_salida.csv', 'w', encoding='utf-8') as salida:
    salida_writer = csv.writer(salida)
    next(tabla)
    salida_writer.writerow(['latitude', 'longitude', 'name', 'label'])
