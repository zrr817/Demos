# This is a toolkit for combining excel files
# Given a directory, uses pandas to combine everything into a single file

import argparse
import os
import pandas as pd

# Define arguments
parser = argparse.ArgumentParser()
parser.add_argument("--build-path", type=str, help="Gives the path to use for the excel files. Default is current directory.", default="")
parser.add_argument("--output", type=str, help="Gives the type of file to output the combined excel file as. Default is csv", default="csv")
parser.add_argument("--input", type=str, help="Gives the type of file used for input files. Default is csv", default="csv")
args = parser.parse_args()

def build_file_list(build_path, file_type):
    '''
    Builds a list of files by walking the file path
    Uses a relative path to where Le's code outputs the files
    At some point, might want to be able to choose which files to include or not
    '''
    file_list = []

    # Walk the data directory and grab all output files (not dirs)
    for root, dirs, files in os.walk(build_path):
        for name in files:
            fid = os.path.join(root, name)
            if name.endswith(file_type):
                file_list.append(fid)
    return file_list

def build_dataframe(file_list):
    '''
    Parameters
    ----------
    file_list : list
        A set of excel files to combine into one

    Returns
    -------
        df: dataframe, a combined dataframe containing all of the files

    '''
    df = pd.concat((pd.read_csv(fid) for fid in file_list), ignore_index=True)
    return df


if __name__ == '__main__':
    # Global arguments
    input_file_type = args.input
    output_file = 'combined_sheet.' + args.output
    #build_path = r'C:\Users\zrr81\source\repos\qa\DataValidation\order_regression'
    build_path = args.build_path
    
    # Get list of files to use and build into dataframe
    file_list = build_file_list(build_path, input_file_type)
    df = build_dataframe(file_list)
   
    # Write final output file
    df.to_csv(build_path + '/' + output_file)
    print(f'Combined file {output_file} written at {build_path}!')