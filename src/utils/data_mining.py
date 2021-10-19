import pandas as pd
import numpy as np


class DataAnalyzer:
    """
    This class is used for Data Mining tasks
    """

    @staticmethod
    def df_info(df):
        '''
        @leosanchezsoler
        The function provides all the relevant info of a pandas.DataFrame
            Arguments:
                - df: a pandas.Dataframe
            Prints:
                - df.shape[0]: number of rows
                - df.shape[1]: number of columns
                - df.columns: the name of the dataset columns'
                - df.info(): basic info about the dataset
                - df.isna().sum(): NaN values per column
        '''
        print('####\nDATAFRAME INFO\n####')
        print('\nNumber of rows:', df.shape[0])
        print('Number of columns:', df.shape[1])
        print('\n#### DATAFRAME COLUMNS ####\n', df.columns, '\n')
        print('### DATAFRAME COLUMN TYPES ###\n')
        print('\n', df.info(verbose=True)) 
        print('\n### TOTAL NaN VALUES ###\n')
        print('\n', df.isna().sum()) 
        print(f"\n### CHECKING DUPLICATES ###\n {df.duplicated().values.any()}: {df.duplicated().sum()}")

    @staticmethod
    def remove_cols(df, cols):
        '''
        This function removes specific columns from a dataframe
        Parameters:
            - df: a pandas Dataframe
        Returns:
            - cols: a list with the columns that will be dropped
            - df: the same dataframe with removed columns
        '''
        df.drop(columns=cols, inplace=True)
        return f'The following columns have been removed from your DataFrame: {cols}'

    @staticmethod
    def apply_function_to_cols(df, cols, function):
        '''
        This function is used to apply functions to specific columns in a dataframe
        Parameters:
            - df: a pandas DataFrame
            - cols: a list of columns
            - function: the function that will be applied
        Returns:
            - df: a Dataframe with the applied function
        '''
        for i in cols:
            df[i] = df[i].apply(function)

    @staticmethod
    def cols_to_lowercase(df):
        """
        This function converts all column names into lowercase
        Parameters:
            - df: a pandas DataFrame
        """
        df = df.rename(columns=str.lower)
        return df
    
    @staticmethod
    def split_df_column(df, cols, sep=" ", n=1):
        """
        This function splits a dataframe column based on a separator
        Parameters:
            - df: a pandas DataFrame
            - sep: a separator (DEFAULT: ' ')
            - cols: a DataFrame column or list of columns
            - n: an integerspecifying the amount of strips (DEFAULT: 1)
        """
        df[cols] = df[cols].str.split(sep, n=n, expand=True)

    @staticmethod
    def strip_df_column(df, cols, strip, to_float=False):
        """
        This function strips a value from a dataframe column
        Parameters:
            - df: a pandas DataFrame
            - cols: a DataFrame column or list of columns
            - strip: the string that will be stripped.
            - to_float: if True, the column datatype will be float
        """
        df[cols] = df[cols].str.strip(strip)
        if to_float:
            df[cols] = df[cols].astype(float)

    @staticmethod
    def get_df_value_counts(df):
        """
        This function checks how many different values are in each column of a Dataframe
        Parameters:
            - df: a pandas DataFrame
        """
        print(f"###### DATAFRAME VALUE COUNTS ######\n")
        for pos, column in enumerate(df.columns):
            print(F"{column}: {len(df[column].value_counts())}")

    @staticmethod
    def check_data_percentage(df, subset):
        """
        This function swhows the percentage of a dataframe slicing
        Parameters:
            - df: a pandas Dataframe
            - subset: the specific slice of the dataframe
        """
        percentage = round((subset.shape[0] * 100) / df.shape[0], 4)
        print(f"The percentage of the subset data in the data overall is: {percentage}%")

    @staticmethod
    def less_zero_units(df, col):
        '''
        This function checks if a column has zero or less than zero values
        Parameters:
            - df: a pandas DataFrame
            - col: a column of that DataFrame

        Returns:
            - zero_df: the df masked with the values of the column that are equal to zero
            - less_zero_df: the df masked with the values of the column that are less than zero
        '''
        zero_df = df[df[col] == 0]
        less_zero_df = df[df[col] < 0]
        print(f"Total rows with no units in {col} column: {zero_df.shape[0]}")
        print(f"Total rows with less than 0 units in {col} column: {less_zero_df.shape[0]}")

        return zero_df, less_zero_df

    @staticmethod
    def check_data_distribution(df, col):
        '''
        This function check how values are distributed
        Parameters:
            - df: a pandas Dataframe
            - col: a DataFrame column
        '''
        x = df[col]

        percentile_25 = np.percentile(x, 25)
        percentile_50 = np.percentile(x, 50)
        percentile_75 = np.percentile(x, 75)

        print(f"The {col} column has the this data distribution:")
        print("Percentile 25: {percentile_25}")
        print("Percentile 50: {percentile_50}")
        print("Percentile 75: {percentile_75}")