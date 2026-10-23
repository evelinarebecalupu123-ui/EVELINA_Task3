
from prefect import flow, task
import duckdb

@task
def check_database():
    con = duckdb.connect("skyroute.duckdb")
    count = con.execute(
        "SELECT COUNT(*) FROM deliveries"
    ).fetchone()[0]
    con.close()
    print(f"Records verified: {count}")
    return count

@flow(name="SkyRoute Data Pipeline")
def skyroute_pipeline():
    total = check_database()
    print(f"Pipeline completed. Total records: {total}")
    return total

if __name__ == "__main__":
    skyroute_pipeline()
