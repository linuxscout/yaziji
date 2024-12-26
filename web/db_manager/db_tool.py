import sqlite3
from typing import List, Tuple, Optional
from abc import ABC, abstractmethod
from typing import List, Tuple, Optional

class RatingOptionsDatabase(ABC):
    """
    Abstract base class for managing Rating and Options in different databases.
    """

    @abstractmethod
    def insert_record(self, rating: int, options: List[str]):
        """
        Insert a new record into the database.
        :param rating: An integer rating.
        :param options: A list of options as strings.
        """
        pass

    @abstractmethod
    def fetch_all_records(self) -> List[Tuple[int, int, List[str]]]:
        """
        Fetch all records from the database.
        :return: A list of tuples containing (id, rating, options).
        """
        pass

    @abstractmethod
    def fetch_record_by_id(self, record_id: str) -> Optional[Tuple[int, int, List[str]]]:
        """
        Fetch a specific record by its ID.
        :param record_id: The ID of the record to fetch.
        :return: A tuple containing (id, rating, options) or None if not found.
        """
        pass

    @abstractmethod
    def delete_record(self, record_id: str):
        """
        Delete a specific record by its ID.
        :param record_id: The ID of the record to delete.
        """
        pass

    @abstractmethod
    def close(self):
        """
        Close the database connection.
        """
        pass
