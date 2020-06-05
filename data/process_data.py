import sys
import pandas as pd
import numpy as np

from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """
    Load csv data
    
    This function loads two files and returns a consolidated pandas dataframe
    
    Arguments:
        messages_filepath: the csv file containing the message text
        categories_filepath: the csv file containing the category types
    Output:
        df: consolidated dataframe
    """
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    
    df = pd.merge(messages, categories, on='id')
    
    return df


def clean_data(df):
    """
    Cleans the dataframe
    
    This functions splits the category types into distinct values, renames the
    columns with the appropriate headers, then removes any duplicate values
    
    Arguments:
        df: raw dataframe
    Output:
        df: cleaned dataframe
    """
    categories = df["categories"].str.split(";", n = 0, expand = True)
    categories.columns = categories.iloc[0].apply(lambda x: x[:(len(x)-2)])
    
    for column in categories:
        categories[column] = categories[column].str[-1:].astype(int)
       
    df = df.drop(['categories'], axis=1)
    df = pd.merge(df, categories, left_index=True, right_index=True)
    df.drop_duplicates(keep = 'first', inplace = True)
    
    return df

def save_data(df, database_filename):
    """
    Saves the dataframe
    
    This function saves the cleaned dataframe into an SQL lite database file
    
    Arguments:
        df: the dataframe for storage
        database_filename: the desired name for the db file
    """
    engine = create_engine('sqlite:///'+database_filename)
    df.to_sql('df', engine, index=False)
    pass


def main():
    """Function to execute all above code"""
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()