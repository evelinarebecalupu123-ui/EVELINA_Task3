import duckdb

con = duckdb.connect("skyroute.duckdb")

con.execute("""
    CREATE OR REPLACE TABLE deliveries AS
    SELECT *
    FROM read_csv_auto('cleaned_output.csv')
""")

print("DuckDB connected successfully!")

print("\nTotal records:")
print(con.execute(
    "SELECT COUNT(*) FROM deliveries"
).fetchone()[0])

print("\nFirst five records:")
print(con.execute(
    "SELECT * FROM deliveries LIMIT 5"
).fetchdf())

con.close()
print("\nDuckDB practical completed successfully!")