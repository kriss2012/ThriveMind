import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

c.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='CBT_cbt_therapy'")
original_schema = c.fetchone()[0]

new_schema = original_schema.replace(' UNIQUE', '')
new_schema = new_schema.replace('"CBT_cbt_therapy"', '"CBT_cbt_therapy_new"')

c.execute(new_schema)
c.execute("INSERT INTO CBT_cbt_therapy_new SELECT * FROM CBT_cbt_therapy")
c.execute("DROP TABLE CBT_cbt_therapy")
c.execute("ALTER TABLE CBT_cbt_therapy_new RENAME TO CBT_cbt_therapy")

conn.commit()
print("Database fixed successfully.")
conn.close()
