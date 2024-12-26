from pymongo import MongoClient
from typing import List, Tuple, Optional
from db_tool import RatingOptionsDatabase

class RatingOptionsDatabaseMongo(RatingOptionsDatabase):
    def __init__(self, db_name: str = "ratings_db", collection_name: str = "rating_options"):
        """
        Initialize the MongoDB connection and create the collection if it doesn't exist.
        """
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_record(self, rating: int, options: List[str]):
        """
        Insert a new record into the MongoDB collection.
        :param rating: An integer rating.
        :param options: A list of options as strings.
        """
        record = {
            "rating": rating,
            "options": options
        }
        self.collection.insert_one(record)

    def fetch_all_records(self) -> List[Tuple[int, int, List[str]]]:
        """
        Fetch all records from the MongoDB collection.
        :return: A list of tuples containing (id, rating, options).
        """
        records = self.collection.find()
        return [(str(record["_id"]), record["rating"], record["options"]) for record in records]

    def fetch_record_by_id(self, record_id: str) -> Optional[Tuple[int, int, List[str]]]:
        """
        Fetch a specific record by its ID.
        :param record_id: The ID of the record to fetch.
        :return: A tuple containing (id, rating, options) or None if not found.
        """
        record = self.collection.find_one({"_id": record_id})
        if record:
            return (str(record["_id"]), record["rating"], record["options"])
        return None

    def delete_record(self, record_id: str):
        """
        Delete a specific record by its ID.
        :param record_id: The ID of the record to delete.
        """
        self.collection.delete_one({"_id": record_id})

    def close(self):
        """
        Close the MongoDB connection.
        """
        self.client.close()
if __name__ == "__main__":
    db = RatingOptionsDatabaseMongo()

    # Insert records
    db.insert_record(5, ["option1", "option2", "option3"])
    db.insert_record(3, ["optionA", "optionB"])

    # Fetch all records
    records = db.fetch_all_records()
    print("All Records:", records)

    # Fetch a specific record by ID (use first record's ID for example)
    first_record_id = records[0][0]  # Getting the first record's ID
    record = db.fetch_record_by_id(first_record_id)
    print("Record with ID:", first_record_id, ":", record)

    # Delete a record
    db.delete_record(first_record_id)

    # Fetch all records again
    records = db.fetch_all_records()
    print("All Records after deletion:", records)

    # Close the database
    db.close()