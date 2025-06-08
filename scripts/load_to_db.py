import psycopg2
import json

conn = psycopg2.connect(
    dbname="transaction_db",
    user="postgres",
    password="postgres",
    host="localhost"
)

cur = conn.cursor()

with open("data/transactions.json", "r") as f:
    lines = f.readlines()

for line in lines:
    r = json.loads(line)
    try:
        cur.execute("""
            INSERT INTO transactions (transaction_id, user_id, amount, timestamp, location, status)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING
        """, (r["transaction_id"], r["user_id"], r["amount"], r["timestamp"], r["location"], r["status"]))
    except Exception as e:
        print("Error:", e)

conn.commit()
cur.close()
conn.close()
print("✅ Done inserting into database.")
