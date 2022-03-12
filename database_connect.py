import pandas as pd
from sqlalchemy import create_engine
import asyncio
import psycopg2
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
conn = engine.connect()
class Connection:
    def __init__(self, engine: str, test_file: str, standard_file: str, result_file:str, conn = 'dbname=postgres user=postgres password=postgres'):
        self.conn = psycopg2.connect(conn)
        self.engine = engine
        self.test_file = test_file
        self.standard_file = standard_file
        self.result_file = result_file
        self.cursor = self.conn.cursor()

    """
    Upload files to database
    """
    async def upload_file(self):
        with open(self.result_file) as _:
            result = pd.read_table(self.result_file)
        with open(self.test_file) as __:
            test = pd.read_table(self.test_file)
            with open(self.standard_file) as ___:
                standard = pd.read_table(self.standard_file)
        await result.to_sql('results', con = self.engine, index = True, index_label = 'id', if_exists='replace')
        await test.to_sql('tests', con = self.engine, index = True, index_label= 'id', if_exists= 'replace')
        await standard.to_sql('standards', con = self.engine, index = True, index_label = 'id', if_exists='replace')

    """
    Run upload_file
    """

    def run_asyncio(self):
        asyncio.run(self.upload_file())

    """
    Create df for test and standards
    """

    def create_df_test_and_standards(self):
        select_test_and_standards = 'SELECT * FROM' \
                                    ' tests, standards;'
        self.cursor.execute(select_test_and_standards)
        data = self.cursor.fetchall()
        df_tests_stand = pd.DataFrame(data)
        df_tests_stand = df_tests_stand.rename(columns={0: 'id', 1: 'test_id',
                                                        2: 'instrument', 3: 'data',
                                                        4: 'time', 5: 'standard',
                                                        6: 'concentration', 7: 'mass_mode',
                                                        8: 'polarity', 9: 'scan_type',
                                                        10: 'scan_rate', 11: 'n_scans',
                                                        12: 'id', 13: 'standard',
                                                        14: 'polarity', 15: 'target_mass',
                                                        })
        df_tests_stand = df_tests_stand.drop('id', axis=1)
        return df_tests_stand

    """
    Create df for result
    
    """

    def create_df_result(self):
        select_results = 'SELECT * FROM results'
        self.cursor.execute(select_results)
        data_results = self.cursor.fetchall()
        df_result = pd.DataFrame(data_results)
        df_result = df_result.rename(columns={0: 'id', 1: 'test_id',
                                              2: 'target_mass', 3: 'visible_mass',
                                              4: 'intensity', 5: 'width',
                                              6: 'mass_shift'
                                              })

        return df_result
    """
    Create merge df 
    """

    def create_merge(self):
        df_test_stand = self.create_df_test_and_standards()
        df_result = self.create_df_result()
        merge_result_test_stand = pd.merge(df_test_stand, df_result)
        return merge_result_test_stand




#
#

# #
