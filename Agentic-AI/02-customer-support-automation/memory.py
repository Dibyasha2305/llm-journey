import sqlite3

# -------------------------
# Create Database
# -------------------------

conn = sqlite3.connect("memory.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS conversations(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer TEXT,
    query TEXT,
    response TEXT
)
""")

conn.commit()
conn.close()


# -------------------------
# Save Conversation
# -------------------------

def save_conversation(customer, query, response):

    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO conversations(customer, query, response)
        VALUES (?, ?, ?)
    """, (customer, query, response))

    conn.commit()
    conn.close()


# -------------------------
# Retrieve Last Conversation
# -------------------------

def get_last_conversation(customer):

    conn = sqlite3.connect("memory.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT query, response
        FROM conversations
        WHERE customer = ?
        ORDER BY id DESC
        LIMIT 1
    """, (customer,))

    result = cursor.fetchone()

    conn.close()

    return result


# -------------------------
# Test (only when running memory.py)
# -------------------------

if __name__ == "__main__":

    print("Memory database initialized successfully!")

    save_conversation(
        "David",
        "I need a refund.",
        "Your refund request has been received."
    )

    last = get_last_conversation("David")

    print(last)