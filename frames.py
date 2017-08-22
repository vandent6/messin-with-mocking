import pandas as pd

class H5Cols:
    def __init__(self, df_list):
        self.df_list = df_list

    def return_list_obj(self, obj=0):
        return self.df_list[obj]

    def print_frames(self):
        return self.return_list_obj()
        
