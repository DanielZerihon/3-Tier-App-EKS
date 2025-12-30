from db import get_connection

def migrate():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    """)

    cur.execute("""
        INSERT INTO users (username, password)
        VALUES (%s, %s)
        ON CONFLICT (username) DO NOTHING;
    """, ("admin", "1234"))

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Migration completed")

if __name__ == "__main__":
    migrate()
