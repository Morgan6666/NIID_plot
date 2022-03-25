import os
import uuid
from os import listdir
import psycopg2
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from dateutil import parser
import dateutil
import glob
from tabulate import tabulate
from standards import data
import asyncio
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

"""
    Upload to result
    
"""

class Upload:
    def __init__(self, path: str, specification):
        self.path = path
        self.specification =specification

    def add_file(self):
        res_clean = []
        res_data = []
        filenames = glob.glob(self.path + '\*.txt')
        max_file = max(filenames, key=os.path.getctime)
        res_clean.append(os.path.basename(max_file).replace('.txt', '').split('_'))
        res_data.append(parser.parse(res_clean[0][1]))
        date = pd.DataFrame(res_clean).sort_values(by=[1])
        date['uuid'] =  date.apply(lambda _: uuid.uuid4(), axis=1)
        data = pd.read_table(max_file)
        data['uuid'] = pd.Series([date['uuid'][0] for x in range(len(data.index))])
        date.to_sql('tests', con = engine, index = True, index_label = 'id', if_exists = 'replace')
        data.to_sql('results', con=engine, index=True, index_label='id', if_exists='replace')


    def add_specification(self):
         self.specification.to_sql('specifications', con = engine, index = True,  if_exists='replace')



upl = Upload('C:\\Users\\Huawei\\PycharmProjects\\Masspectrum\\PPG_Deniska', data)

upl.add_file()


#max_file = max(files, key=os.path.getctime)
#print(max_file)


        #print(tabulate(date, headers='keys'))
