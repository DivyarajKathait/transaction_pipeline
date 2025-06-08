import psycopg2
import json
import time
import os

DATA_FILE = "data/transactions.json"
LAST_LINE_FILE = "data/last_line.txt"

def get_last_processed_line():
    if not os.path.exists(LAST_LINE_FILE):
        return 0
    with open(LAST_LINE_FILE, "r") as f:
        return int(f.read())

def set_last_processed_line(line_num):
    with open(LAST_LINE_FILE, "w") as f:
        f.write(str(line_num))

def load_new_transactions():
    conn = psycopg2.connect(
        dbname="transaction_db",
        user="postgres",
        password="postgres",  # Replace if needed
        host="localhost"
    )
    cur = conn.cursor()

    last_line = get_last_processed_line()
    with open(DATA_FILE, "r") as f:
        lines = f.readlines()

    new_lines = lines[last_line:]
    print(f"⏳ Found {len(new_lines)} new transactions...")

    for line in new_lines:
        r = json.loads(line)
        try:
            is_anomaly = r["amount"] > 450 or r["status"] == "FAILED"
            cur.execute("""
                        INSERT INTO transactions (transaction_id, user_id, amount, timestamp, location, status, is_anomaly)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT DO NOTHING
                        """, (
                        r["transaction_id"], r["user_id"], r["amount"],
                        r["timestamp"], r["location"], r["status"], is_anomaly
                        ))
        except Exception as e:
            print("❌ Error inserting:", e)

    conn.commit()
    cur.close()
    conn.close()
    print("✅ Transactions loaded into DB.")
    set_last_processed_line(last_line + len(new_lines))


# 🔁 Main loop
if __name__ == "__main__":
    while True:
        load_new_transactions()
        time.sleep(5)  # check every 5 seconds
