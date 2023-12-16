# ### works in notebook as is
# # dataframe information
# def df_info(dataframes):
#   """
#     Finds some usefull information about all dataframes given in the function.
    
#     Usage: pass a list of dataframes into the function
#     dataframes = [df1,df2,...]
#   """

#   for df in dataframes:
#          # Check if the dataframe has at least one column
#         if not df.empty:
#           # # Use list comprehension to get the name of the dataframe from global variables
#           df_name = [name for name, obj in globals().items() if obj is df][0] # [0] is the name of each dataframe in the list
#           print("----- information for ", df_name, " -----")
#           print(df_name, " : ", df.shape, "(rows, columns)")
#           print(df_name, " : ", df.isna().sum().sum() , "missing values")
#           print(df_name, " : ", df.duplicated().sum() , "duplicated values")
#           #df.describe()
#           #df.info()
          
#           # Identify and count values of the last column
#           last_column = df.columns[-1]
#           value_counts = df[last_column].value_counts()

#           print(df_name, " : Value counts for ", last_column)
#           print(value_counts)
#         else:
#           print(df_name, ': The dataframe is empty.')


def df_info(dataframes):
    """
    Finds useful information about all dataframes given in the function.

    Usage: pass a list of dataframes into the function
    dataframes = [df1, df2, ...]
    """

    for i, df in enumerate(dataframes, start=1):
        df_name = f"df{i}"
        # Check if the dataframe has at least one column
        if not df.empty:
            print("----- information for ", df_name, " -----")
            print(df_name, " : ", df.shape, "(rows, columns)")
            print(df_name, " : ", df.isna().sum().sum(), "missing values")
            print(df_name, " : ", df.duplicated().sum(), "duplicated values")

            # Identify and count values of the last column
            last_column = df.columns[-1]
            value_counts = df[last_column].value_counts()

            print(df_name, " : Value counts for ", last_column)
            print(value_counts)
        else:
            print(df_name, ': The dataframe is empty.')
