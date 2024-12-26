import sqlite3
from typing import List, Tuple, Optional
from db_manager.db_tool import RatingOptionsDatabase
import json
class RatingOptionsDatabaseSQLite(RatingOptionsDatabase):
    def __init__(self, db_name: str = "ratings.db"):
        """
        Initialize the SQLite connection and create the table if it doesn't exist.
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self):
        """
        Create the table for storing ratings and options.
        """
        create_table_query = """
        CREATE TABLE IF NOT EXISTS rating_options (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rating INTEGER NOT NULL,
            options TEXT NOT NULL
        );
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def insert_record(self, rating: int, options):
        """
        Insert a new record into the SQLite database.
        :param rating: An integer rating.
        :param options: A list of options as strings.
        """
        options_str = json.dumps(options,ensure_ascii=False)  # Store options as a comma-separated string
        insert_query = "INSERT INTO rating_options (rating, options) VALUES (?, ?);"
        self.cursor.execute(insert_query, (rating, options_str))
        self.connection.commit()

    def fetch_all_records(self) -> List[Tuple[int, int, List[str]]]:
        """
        Fetch all records from the SQLite database.
        :return: A list of tuples containing (id, rating, options).
        """
        select_query = "SELECT id, rating, options FROM rating_options;"
        self.cursor.execute(select_query)
        rows = self.cursor.fetchall()
        return [(row[0], row[1], row[2].split(",")) for row in rows]

    def fetch_record_by_id(self, record_id: str) -> Optional[Tuple[int, int, List[str]]]:
        """
        Fetch a specific record by its ID.
        :param record_id: The ID of the record to fetch.
        :return: A tuple containing (id, rating, options) or None if not found.
        """
        select_query = "SELECT id, rating, options FROM rating_options WHERE id = ?;"
        self.cursor.execute(select_query, (record_id,))
        row = self.cursor.fetchone()
        return (row[0], row[1], row[2].split(",")) if row else None

    def delete_record(self, record_id: str):
        """
        Delete a specific record by its ID.
        :param record_id: The ID of the record to delete.
        """
        delete_query = "DELETE FROM rating_options WHERE id = ?;"
        self.cursor.execute(delete_query, (record_id,))
        self.connection.commit()

    def close(self):
        """
        Close the SQLite database connection.
        """
        self.connection.close()
# Example Usage
if __name__ == "__main__":
    db = RatingOptionsDatabaseSQLite()

    # Insert records
    db.insert_record(5, ["option1", "option2", "option3"])
    db.insert_record(3, ["optionA", "optionB"])

    # Fetch all records
    records = db.fetch_all_records()
    print("All Records:", records)

    # Fetch a specific record
    record = db.fetch_record_by_id(1)
    print("Record with ID 1:", record)

    # Delete a record
    db.delete_record(1)

    # Fetch all records again
    records = db.fetch_all_records()
    print("All Records after deletion:", records)

    # Close the database
    db.close()
