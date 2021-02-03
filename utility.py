def check_columns(df, head_rows=5):
    """
    :param df: pandas dataframe
    :param head_rows: integer, the number of row to display
    :return: None
    """

    for column in df.columns:
        srs = df[column].value_counts()
        print("=" * 60)
        print(f"Column: {column}")
        print("-" * 20)
        print(f"--- Total Unique Values: {len(srs)} ---")
        print(srs.head(head_rows).to_string())
        print(f"Min: {srs.index.min()},  Max: {srs.index.max()}")


