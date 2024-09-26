from abc import ABC, abstractmethod
from collections.abc import Collection
from typing import TypeVar, Generic

from multimethod import multimethod

from cs5278_assignment_4.live6.data_and_position import DataAndPosition
from cs5278_assignment_4.live6.position import Position

T = TypeVar("T")


class ProximityDB(ABC, Generic[T]):
    """
    Create an implementation of the ProximityDB.

    The ProximityDB maps data items to coordinates and
    allows searching for nearby data items using geohashes.

    You are free to adapt your GeoDB implementation. However, please make
    sure that your implementation of ProximityDB is in this package so that
    it is easy for your peers and the instructor to find.

    There will be ambiguous requirements. Use your best judgement in determining
    an appropriate interpretation. Keep these ambiguities in mind when you code
    review others' solutions later in class.

    The type parameter T is the type of data stored in the database. For example,
    to map strings to coordinates, you would use something like the below code:
    ProximityDBImpl(lat, lon, "string"): ProximityDBImpl[str]

    See the example package for a sample application
    that stores Building objects in the database
    """

    @abstractmethod
    def insert(self, data: DataAndPosition[T]) -> None:
        """
        Inserts a data item into the database at the specified location.
        You SHOULD preserve duplicate data items.
        """

        raise NotImplementedError

    @abstractmethod
    @multimethod
    def delete(self, pos: Position) -> Collection[DataAndPosition[T]]:
        """
        Deletes the all data items at the specified
        location from the database.

        Returns the list of data items that were deleted.
        """

        raise NotImplementedError

    @abstractmethod
    @multimethod
    def delete(self, pos: Position, bits_of_precision: int) -> Collection[DataAndPosition[T]]:
        """
        Deletes all data items from the database that
        match the provided latitude and longitude
        up to the specified number of bits of precision
        in their geohashes.

        Returns the list of deleted data items.
        """

        raise NotImplementedError

    @abstractmethod
    def contains(self, pos: Position, bits_of_precision: int) -> bool:
        """
        Returns true if the database contains at least one data item that
        matches the provided latitude and longitude
        up to the specified number of bits of precision
        in its geohash.
        """

        raise NotImplementedError

    @abstractmethod
    def nearby(self, pos: Position, bits_of_precision: int) -> Collection[DataAndPosition[T]]:
        """
        Returns all data items in the database that
        match the provided latitude and longitude
        up to the specified number of bits of precision
        in their geohashes.
        """

        raise NotImplementedError
