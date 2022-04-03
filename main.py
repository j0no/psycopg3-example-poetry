from dotenv import load_dotenv
import psycopg

import os
load_dotenv()

DB_URL = os.environ["DB_URL"]

with psycopg.connect(DB_URL) as conn:
    with conn.cursor() as cur:
        cur.execute("select \'ok\'")
        print(cur.fetchone())