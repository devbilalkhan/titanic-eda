import pandas as pd
from matplotlib.colors import ListedColormap
import seaborn as sns
import matplotlib.pyplot as plt

def print_header(title):
    """
    Prints a header with a given title.

    Parameters:
    title (str): The title to print.
    """
    print("-" * 60)
    print(title)
    print("-" * 60)


def inspect_missing_values(df):
    """
    Generate a DataFrame that provides information about missing values in the given DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame to analyze.
    columns (list): The list of columns in the DataFrame to analyze.

    Returns:
    pandas.DataFrame: A DataFrame where each column corresponds to a column in the original DataFrame,
                      and each row provides information about the total number of values, the percentage of missing values,
                      and the data type of that column.
    """
    index_names = ["Total", "Missing %", "Data type"]
    columns = df.columns
    missing_values_table = pd.DataFrame(index=index_names, columns=columns)
    for col in columns:
        missing_data = df[col].isnull().sum()
        missing_data_percentage = round((missing_data/df.shape[0])*100, 2)
        missing_values_table.loc[index_names[0],col] = df[col].isnull().sum()
        missing_values_table.loc[index_names[1],col] = missing_data_percentage
        missing_values_table.loc[index_names[2],col] = df[col].dtype
    return missing_values_table 

def inspect_frequent_values(df):
    """
    Generate a DataFrame that provides information about the most frequent values in the given DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame to analyze.
    columns (list): The list of columns in the DataFrame to analyze.

    Returns:
    pandas.DataFrame: A DataFrame where each column corresponds to a column in the original DataFrame,
                      and each row provides information about the total number of values, the most frequent value,
                      the count of the most frequent value, and the percentage of the most frequent value.
    """   
    index_names = ["Total", "Freq", "Count", "Freq %"]
    columns = df.columns
    most_frequent_table = pd.DataFrame(index=index_names, columns=columns)
    for col in columns:
        most_frequent_table.loc[index_names[0],col] = df[col].count()
        most_frequent_table.loc[index_names[1],col] = df[col].mode()[0]  
        most_frequent_table.loc[index_names[2],col] = df[col].value_counts().max()
        most_frequent_table.loc[index_names[3],col] = round((df[col].value_counts().max()/df[col].count())*100, 2)

    return most_frequent_table

def inspect_unique_values(df):
    """
    Inspect the unique values in the given DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame to analyze.

    Returns:
    pandas.DataFrame: A DataFrame where each column corresponds to a column in the original DataFrame,
                      and each row provides information about the number of unique values.
    """
    unique_values_table = pd.DataFrame(index=["Unique", "Total"], columns=df.columns)
    for col in df.columns:
        unique_values_table.loc["Count",col] = len(df[col])
        unique_values_table.loc["Unique",col] = df[col].nunique()       
    return unique_values_table

def display_custom_palette(colors):
    custom_cmap = ListedColormap(colors)
    print("Custom Color Palette Display:")
    sns.palplot(sns.color_palette(colors))
    plt.show()

