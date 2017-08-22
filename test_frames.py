import unittest
from unittest.mock import patch
import pandas as pd
from pandas import DataFrame
from tmocking.frames import H5Cols

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                  'D': ['D0', 'D1', 'D2', 'D3']},
                      index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])


df_list = [df1, df2, df3]
df_all = DataFrame(df1, df2, df3)

class TestDataFrame(unittest.TestCase):

    @patch.object(H5Cols, 'return_list_obj')    
    def test_return_list_obj(self, mock_return_list_obj):
        mock_return_list_obj.return_value = 'hi'

        h5_cols = H5Cols(df_list)
        result = h5_cols.print_frames()

        self.assertEqual(result,'hi')

        

if __name__ == '__main__':
    test_classes_to_run = [TestDataFrame]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)
