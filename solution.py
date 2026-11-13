import pandas as pd

def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame:

    is_new = new_column not in df.columns

    right_chars = all(c.isalpha() or c == "_" for c in new_column)

    tokens = role.split()

    right_role = bool(tokens)

    for token in tokens:
        right_role = (right_role and
                      (token in df.columns
                       or token in ["*", "+", "-"]
                       or (token.replace(".", "", 1).isnumeric()) and token != "."))

    if  is_new and right_chars and right_role:
        try:
            df[new_column] = df.eval(role)
        except:
            return pandas.DataFrame([])
        return df
    else:
        return pandas.DataFrame([])