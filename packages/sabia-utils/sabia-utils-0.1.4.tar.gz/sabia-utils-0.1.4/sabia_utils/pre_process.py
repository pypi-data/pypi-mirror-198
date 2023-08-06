import glob
import os

from sabia_utils.utils.preprocess_utils import read_parquet_files


class Processing:
    def __init__(self):
        self.method = ''

    def apply_to_df(self, df, column):
        pass


def pre_process_parquets(
        folder_path, column_to_pre_process, pre_processed_column, processor):

    parquet_files = glob.glob(os.path.join(folder_path, "*.parquet"))

    processed_df_list = read_parquet_files(
        parquet_files, column_to_pre_process, pre_processed_column, processor)

    for df, f in processed_df_list:
        df.to_parquet(f)
