from faker import Faker
import random
import time
import json
import os

fake = Faker()
os.makedirs("data", exist_ok=True)

def generate_transaction():
    return {
        "transaction_id": fake.uuid4(),
        "user_id": random.randint(1, 100),
        "amount": round(random.uniform(10, 500), 2),
        "timestamp": fake.date_time_this_year().isoformat(),
        "location": fake.city(),
        "status": random.choice(["SUCCESS", "FAILED", "PENDING"])
    }

while True:
    with open("data/transactions.json", "a") as f:
        f.write(json.dumps(generate_transaction()) + "\n")
    print("Generated a transaction...")
    time.sleep(1)
