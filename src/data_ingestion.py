import pyarrow.parquet as pq
import psycopg

print(pq.read_table("./Data/parquet/1746154800000 data.parquet").to_pandas()["track.album.artists"][0])

print(pq.read_table("./Data/parquet/1746154800000 data.parquet").to_pandas()["track.artists"][0])

# with psycopg.connect("host=localhost port=5432 user=postgres password=mysecretpassword dbname=postgres connect_timeout=10") as conn:
#     with conn.cursor() as cur:
#         cur.execute("""
#             DROP TABLE IF EXISTS raw.listen_history, raw.track;
#         """)

#         cur.execute("""
#             DROP SCHEMA IF EXISTS raw;
#         """)

#         cur.execute("""
#             CREATE SCHEMA raw AUTHORIZATION pg_database_owner;
#         """)

#         cur.execute("""
#             CREATE TABLE IF NOT EXISTS raw.listen_history (
#                 played_at timestamp PRIMARY KEY)
#             """)
        
#         cur.execute("""
#             CREATE TABLE IF NOT EXISTS raw.track (
#                 id text,
#                 name text,
#                 PRIMARY KEY (id, played_at),
#                 played_at timestamp REFERENCES listen_history(played_at))
#             """)
        
#         cur.executemany(
#             """
#                 INSERT INTO raw.listen_history (played_at) values (%s)
#             """,
#             [tuple(r) for r in pq.read_table("./Data/parquet/1746154800000 data.parquet").to_pandas()[["played_at"]].to_numpy()])

#         cur.executemany(
#             """
#                 INSERT INTO raw.track (id, name, played_at) values (%s, %s, %s)
#             """,
#             [tuple(r) for r in pq.read_table("./Data/parquet/1746154800000 data.parquet").to_pandas()[["track.id", "track.name", "played_at"]].to_numpy()])

#         conn.commit()