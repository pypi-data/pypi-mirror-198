from pandas import DataFrame


def reverse_df_order(transactions: DataFrame) -> DataFrame:
    pass


def get_file_format(filename: str) -> str:
    parts = filename.split(".")
    if len(parts) == 2:
        return parts[1]
    else:
        raise ValueError(f"Unrecognised filename format '{filename}': Unable to split strings")



