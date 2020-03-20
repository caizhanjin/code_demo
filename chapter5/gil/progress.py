import multiprocessing
import glob
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres@localhost:5432/vnpy")


def save_bar(filename):
    vt_symbol = filename.split("_")[0]
    symbol, exchange = vt_symbol.split(".")
    df = pd.read_csv(
        filename,
        compression="gzip",
        parse_dates=True,
        skiprows=1,
        names=[
            "datetime",
            "open_price",
            "high_price",
            "low_price",
            "close_price",
            "volume",
            "open_interest",
        ],
    )
    df["symbol"] = symbol
    df["exchange"] = exchange
    df["interval"] = "1m"
    print(df.head(1))
    df.to_sql("dbbardata", engine, if_exists="append", index=False)


if __name__ == "__main__":
    all_files = glob.glob("*csv.gz")
    pool = multiprocessing.Pool(
        min(len(all_files), multiprocessing.cpu_count()), maxtasksperchild=1
    )
    results = []
    for file_name in all_files:
        res = pool.apply_async(save_bar, args=(file_name,))
        results.append(res)
    [res.get() for r in results]
