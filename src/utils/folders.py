import os, sys
import pandas as pd


class Folders:
    """
    This class is used to manage folder structures and appending paths to make workflow easier.
    """
    @staticmethod
    def read_json(fullpath):
        """
        Reads json file and returns it.
        Parameters:
            - fullpath: the desired path

        Returns:
            - json_readed = the desired json
        """
        with open(fullpath, "r") as json_file_readed:
            json_readed = json.load(json_file_readed)
        return json_readed

    @staticmethod
    def get_current_path(file=False):
        """
        Shows current path:
        Parameters:
            - file: if True, shows current working directory
                    if False, shows the directory that contains the file
        """
        if file:
            return os.getcwd()
        else:
            return os.path.dirname(os.getcwd())

    @staticmethod
    def add_path(num, jupyter=True):
        '''
        Adds a path to sys.
        Args:
            - num: number of times to get the dirname until reaching the rootpath.
        
        Returns:
            - dirpath: the desired path
        '''
        if jupyter:
            dirpath = os.getcwd()
        else:
            dirpath = __file__ # en caso de jupyter se usa os.getcwd()
        for i in range(num):
            dirpath = os.path.dirname(dirpath)
        sys.path.append(dirpath)

        return dirpath

    @staticmethod
    def append_path(path=os.path.dirname(os.getcwd()), jupyter=True):
        """
        Appends path to sys    
        Returns:
            - dirpath: the desired path
        """  
        if jupyter:
            path = os.getcwd()
        else:
            path = __file__ # en caso de jupyter se usa os.getcwd()

        path = sys.path.append(path)

        return path


    @staticmethod
    def read_directory_data(path):
        """
        This method reads directory data and assigns variables to it
        Parameters:
            - path: the path of the directory that is going to be read.
        """
        files_dict = {'csv': [], 'xlsx': []}
        variable_dict = {}
        list_csv = []
        list_xlsx = []

        for pos, file in enumerate(os.listdir(path)):
            if file.endswith('.csv'):
                filename = file.split('.')[0]
                filename_str = str(filename)
                list_csv.append(filename)
                filename = pd.read_csv(f"{path}{file}")
                variable_dict[filename_str] = filename

            elif file.endswith('.xlsx'):
                filename = file.split('.')[0]
                filename_str = str(filename)
                list_xlsx.append(filename)
                filename = pd.read_excel(f"{path}{file}", engine='openpyxl')
                variable_dict[filename_str] = filename

        files_dict['csv'].append(list_csv)
        files_dict['xlsx'].append(list_xlsx)
        print(f"The following variables are now ready to be used:\n{files_dict}")

        return variable_dict

class Saver:
    """
    This class is used for saving files
    """
    @staticmethod
    def save_output_file(df, filename, path):
        """
        This function saves data files to csv and places them in the output folder
        Parameters:
        - df: a pandas Dataframe
        - filename: the name of the file
        - path: the path in which the file will be saved
        """
        doc_name = path + filename + '.csv'  
        df.to_csv(doc_name, index=False)
        print(f"The following file has been saved:\n{filename}")
        print(f"\nYou can find it here: {doc_name}")