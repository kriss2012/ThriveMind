import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

c.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='CBT_cbt_therapy'")
original_schema = c.fetchone()[0]
print("ORIGINAL SCHEMA:")
print(original_schema)

# Create a new table without UNIQUE constraints on user_id and therapist_id
# assuming they are currently defined as UNIQUE.
new_schema = original_schema.replace(' UNIQUE', '')

print("NEW SCHEMA:")
print(new_schema)

c.execute(f"CREATE TABLE CBT_cbt_therapy_new {new_schema.split('CBT_cbt_therapy', 1)[1]}")
c.execute("INSERT INTO CBT_cbt_therapy_new SELECT * FROM CBT_cbt_therapy")
c.execute("DROP TABLE CBT_cbt_therapy")
c.execute("ALTER TABLE CBT_cbt_therapy_new RENAME TO CBT_cbt_therapy")

conn.commit()
print("Database fixed successfully.")
conn.close()
