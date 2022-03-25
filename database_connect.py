import pandas as pd
import shortuuid
from sqlalchemy import create_engine
import asyncio
import psycopg2
from tabulate import tabulate

#engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
#conn = engine.connect()


class Connection:
    def __init__(self, test_file: str,
                 standard_file: str, result_file: str,
                 specification_file: str,
                 #conn='dbname=postgres user=postgres password=postgres'
                  ):
        self.specification_file = specification_file
        self.conn = psycopg2.connect('host=localhost dbname=postgres user=bairamkulov_dd password=23456asd')
        #self.engine = engine
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
        with open(self.specification_file) as ____:
            specification = pd.read_table(self.specification_file)
        await result.to_sql('results', con=self.engine, index=True, index_label='id', if_exists='replace')
        await test.to_sql('tests', con=self.engine, index=True, index_label='id', if_exists='replace')
        await standard.to_sql('standards', con=self.engine, index=True, index_label='id', if_exists='replace')
        await specification.to_sql('specifications', con=self.engine, index=True, index_label='id', if_exists='replace')

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
        df_tests_stand = df_tests_stand.rename(columns={0: 'id',
                                                        1: 'test_id',
                                                        2: 'instrument',
                                                        3: 'data',
                                                        4: 'time',
                                                        5: 'standard',
                                                        6: 'concentration',
                                                        7: 'mass_mode',
                                                        8: 'polarity',
                                                        9: 'scan_type',
                                                        10: 'scan_rate',
                                                        11: 'n_scans',
                                                        12: 'id',
                                                        13: 'standard',
                                                        14: 'polarity',
                                                        15: 'target_mass',
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
        df_result = df_result.rename(columns={
                                                0: 'id',
                                                1: 'target_mass',
                                                2: 'visible_mass',
                                                3: 'intensity',
                                                4: 'width',
                                                5: 'mass_shift',
                                                6: 'uuid'
                                                })
        #df_result = df_result.set_index('uuid')
        return df_result

    def select_test(self):
        select_tests = 'SELECT * FROM tests'
        self.cursor.execute(select_tests)
        data_tests = self.cursor.fetchall()
        df_tests = pd.DataFrame(data_tests)
        #print(tabulate(df_tests, headers = 'keys'))
        df_tests = df_tests.rename(columns = {
             0: 'id',
             1: 'instrument',
             2: 'time',
             3: 'standards',
             4: 'concentrations',
             5: 'mass_mode',
             6: 'polarity',
             7: 'scan_type',
             8: 'scan_rate',
             9: 'n_scans',
             10: 'uuid',
         })
       # df_tests = df_tests.set_index('uuid')
        df_tests['n_scans'] = pd.to_numeric(df_tests['n_scans'])
        df_tests['scan_rate'] = pd.to_numeric(df_tests['scan_rate'])
        df_tests['concentrations'] = pd.to_numeric(df_tests['concentrations'])


        return df_tests

    def create_df_specification(self):
        select_specification = 'SELECT * FROM specifications'
        self.cursor.execute(select_specification)
        data_specification = self.cursor.fetchall()
        df_specification = pd.DataFrame(data_specification)
        #print(df_specification)
        #print(df_specification)
        df_specification = df_specification.rename(columns={
              1: 'id',
              2: 'standard',
              3: 'concentration',
              4: 'mass_mode',
              5: 'polarity',
              6: 'scan_type',
              7: 'scan_rate',
              8: 'n_scans',
              9: 'target_mass',
              10: 'min_intensity',
              11: 'min_width',
              12: 'max_width',
              13: 'max_abs_mass_shift',
              14: 'min_abs_shift'
         })
        df_specification = df_specification.drop(columns=[0, 'id'])
        df_specification = df_specification.loc[:, ~df_specification.columns.duplicated()]
        return df_specification

    """
    Create merge df 
    """

    def create_merge(self):
        df_test = connect.select_test()
        df_results = connect.create_df_result()
        df_test = df_test.set_index('uuid')
        df_test = df_test.drop('id', axis=1)
        df_results = df_results.set_index('uuid')
        df_results = df_results.drop('id', axis=1)
        df_merge = pd.merge(df_test, df_results, left_index=True, right_index=True)
        return df_merge


        #print(tabulate(pd.concat(frame), headers='keys'))



        #merge_result_test_stand = pd.merge(df_test_stand, df_result)


        #merge_result_test_stand = merge_result_test_stand.loc[:,~merge_result_test_stand.columns.duplicated()]
        #return #merge_result_test_stand


"""
    Create DataFrame
"""
connect = Connection('tests.txt', 'standards.txt', 'results.txt', 'specifications.txt')
df_merge = connect.create_merge()
df_specification = connect.create_df_specification()

