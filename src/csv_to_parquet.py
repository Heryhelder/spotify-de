import pyarrow.csv as pv
import pyarrow.parquet as pq
import os

def csv_to_parquet():
    CSV_PATH = "./Data/csv/"
    PARQUET_PATH = "./Data/parquet/"

    if not os.path.exists(PARQUET_PATH):
        os.makedirs(PARQUET_PATH)

    if os.path.exists(CSV_PATH):
        for file in os.listdir(CSV_PATH):
            if file.endswith(".csv") and not os.path.exists(PARQUET_PATH + file.replace(".csv", ".parquet")):
                table = pv.read_csv(CSV_PATH + file, parse_options=pv.ParseOptions(delimiter=","))
                pq.write_table(table, PARQUET_PATH + file.replace(".csv", ".parquet"))

if __name__ == "__main__":
    csv_to_parquet()