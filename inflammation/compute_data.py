"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os


class CSVDataSource:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.csv'))
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data CSV files found in path {self.dir_path}")
        data = map(models.load_csv, data_file_paths)
        return list(data) # Return the list of 2D NumPy arrays with inflammation data

class JSONDataSource:
    """
    Loads patient data with inflammation values from JSON files within a specified folder.
    """ 
    def __init__(self,dir_path):
        self.dir_path = dir_path

    def load_inflammation_data(self):
        data_file_paths = glob.glob(os.path.join(self.dir_path, 'inflammation*.json')) 
        if len(data_file_paths) == 0:
            raise ValueError(f"No inflammation data JSON files found in path {self.dir_path}")
        data = map(models.load_json, data_file_paths)
        return list(data)
 