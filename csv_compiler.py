# compile csv
import datetime, shutil, os
from glob import glob
import pandas as pd

def createCSV(team):
    temp_files = '/home/pi/Downloads/'
    path = f'/home/pi/Desktop/Command/Reports/{team}/'
    data_path =f'/home/pi/Desktop/Command/Reports/{team}/DATA/'

    # create team folder
    if not os.path.exists(path):
        os.makedirs(path)
        os.makedirs(data_path)

    os.chdir(temp_files)
    list_of_files = [file for file in glob('*.csv')]

    # move data files to new location
    print('Moving data files...')
    for f in list_of_files:
        shutil.copy(f'{temp_files}{f}', data_path)
        os.remove(f'{temp_files}{f}')
    print('Done.')

    # change into data directory
    os.chdir(data_path)
    
    # Good idea... not working.
#     print('Looking for duplicates...')
#     for i,_ in enumerate(list_of_files):
#     while i < len(list_of_files):
#         df1 = pd.read_csv(list_of_files[i])
#         df2 = pd.read_csv(list_of_files[i+1])
#         if df1.equals(df2):
#             print(f'{list_of_files[i]} duplicate of {list_of_files[i+1]}')
#     print('Done.')
    
    # create dataframe by combining files
    df = pd.concat((pd.read_csv(f, header=[0,1]) for f in list_of_files))
    
    file_name = f'{team} Contact List ({df.shape[0]}) - {datetime.date.today()}'
    
    # save to csv
    df.to_csv(f'{path}{team}{file_name}.csv', index=False)

    # finish    
    print('{file_name} created. Done!')
