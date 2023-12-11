import numpy as np
import pandas as pd

def find_optimal_data_types(df):
  """
  Finds the optimal data type for each variable in a DataFrame. The 'np.iinfo(), np.finfo()' functions are used to obtain the minimum and maximum values for the data types accurately, ensuring better compatibility across different systems.

  Args:
    df: A pandas DataFrame.

  Returns:
    A DataFrame containing the optimal data type for each variable.
  """

  data_types_dict = {}
  for column in df.columns:
    # Get the data type of the column.
    column_type = df[column].dtype

    # Determine the optimal data type for the column.
    if column_type in ('int8', 'int16', 'int32' , 'int64', 'uint8', 'uint16' , 'uint32', 'uint64', 'float16', 'float32', 'float64'):
      # Calculate the minimum and maximum values of the column.
      min_value = df[column].min()
      max_value = df[column].max()

      # Determine the optimal data type for the column based on the minimum and maximum values.
      if isinstance(min_value, (int, np.integer)):
        if min_value < 0:
          # The column contains negative values, so we need to use a signed data type.
          if max_value < np.iinfo(np.int8).max:
            data_types_dict[column] = np.int8
          elif max_value < np.iinfo(np.int16).max:
            data_types_dict[column] = np.int16
          elif max_value < np.iinfo(np.int32).max:
            data_types_dict[column] = np.int32
          else:
            data_types_dict[column] = np.int64
        else:
          # The column contains only non-negative values, so we can use an unsigned data type.
          if max_value < np.iinfo(np.uint8).max:
            data_types_dict[column] = np.uint8
          elif max_value < np.iinfo(np.uint16).max:
            data_types_dict[column] = np.uint16
          elif max_value < np.iinfo(np.uint32).max:
            data_types_dict[column] = np.uint32
          else:
            data_types_dict[column] = np.uint64
      elif isinstance(min_value, float):
        if max_value < np.finfo(np.float16).max:
          data_types_dict[column] = np.float16
        elif max_value < np.finfo(np.float32).max:
          data_types_dict[column] = np.float32
        else:
          data_types_dict[column] = np.float64
    else:
      pass

  return df.astype(data_types_dict)