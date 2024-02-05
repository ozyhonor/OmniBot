import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    gpt TEXT DEFAULT 'You have to compress texts to 100-150 characters revealing the main essence. Always give answers in Russian. No need to write what you did, just give me a compressed text in response.',
    degree FLOAT CHECK (degree >= 0 AND degree <= 1) DEFAULT 0,
    synthes_voice TEXT CHECK (synthes_voice IN ('alloy', 'echo', 'fable', 'onyx', 'nova', 'shimmer')) DEFAULT 'nova',
    synthes_speed FLOAT CHECK (synthes_speed >= 0.25 AND synthes_speed <= 4.0) DEFAULT 1,
    access BOOLEAN DEFAULT 0
)
""")

conn.commit()
conn.close()
