import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:

    right_chars = all(c.isalpha() or c == "_" for c in new_column)

    tokens = re.findall(r'[a-zA-Z_]+|[0-9]*\.?[0-9]+|[+*-]', role)

    right_role = bool(tokens) and "".join(tokens) == re.sub(r"\s+", "", role)

    for token in tokens:
        right_role = (right_role and (
                (token in df.columns and token.islower())
                or token in ["*", "+", "-"]
                or (token.replace(".", "", 1).isnumeric() and token != ".")
                or token.replace("-", "", 1).isnumeric()
                )
            )

    if  right_chars and right_role:
        try:
            df[new_column] = df.eval(role)
        except:
            return pd.DataFrame([])
        return df
    else:
        return pd.DataFrame([])