from cs5278_assignment_4.live6.data_and_position import DataAndPosition
from cs5278_assignment_4.live6.example.building import Building
from cs5278_assignment_4.live6.position import Position
from cs5278_assignment_4.live6.proximity_db import ProximityDB
from cs5278_assignment_4.live6.proximity_db_factory import ProximityDBFactory


class TestProximityDB:
    factory: ProximityDBFactory = ProximityDBFactory()

    def test_simple_insert(self):
        bits_of_precision = 16
        db: ProximityDB[Building] = self.factory.create(bits_of_precision)

        db.insert(DataAndPosition.with_coordinates(0, 0, Building("test")))

        for i in range(bits_of_precision):
            assert db.contains(Position.with_coordinates(0, 0), i)

    def test_simple_delete(self):
        bits_of_precision = 16
        db: ProximityDB[Building] = self.factory.create(bits_of_precision)

        db.insert(DataAndPosition.with_coordinates(0, 0, Building("test")))

        db.delete(Position.with_coordinates(0, 0))

        for i in range(bits_of_precision):
            assert not db.contains(Position.with_coordinates(0, 0), i)

    def test_zero_bits(self):
        db: ProximityDB[Building] = self.factory.create(16)

        db.insert(DataAndPosition.with_coordinates(0, 0, Building("test")))
        db.insert(DataAndPosition.with_coordinates(90, 180, Building("test")))
        db.insert(DataAndPosition.with_coordinates(-90, -180, Building("test")))
        db.insert(DataAndPosition.with_coordinates(-90, 180, Building("test")))
        db.insert(DataAndPosition.with_coordinates(90, -180, Building("test")))

        assert 5 == len(db.nearby(Position.with_coordinates(0, 0), 0))

    def test_zero_bits_delete(self):
        db: ProximityDB[Building] = self.factory.create(16)

        db.insert(DataAndPosition.with_coordinates(0, 0, Building("test")))
        db.insert(DataAndPosition.with_coordinates(90, 180, Building("test")))
        db.insert(DataAndPosition.with_coordinates(-90, -180, Building("test")))
        db.insert(DataAndPosition.with_coordinates(-90, 180, Building("test")))
        db.insert(DataAndPosition.with_coordinates(90, -180, Building("test")))

        db.delete(Position.with_coordinates(0, 0), 0)

        assert 0 == len(db.nearby(Position.with_coordinates(0, 0), 0))

    def test_insert_delete_series(self):
        db: ProximityDB[Building] = self.factory.create(16)

        db.insert(DataAndPosition.with_coordinates(0, 0, Building("test")))
        db.insert(DataAndPosition.with_coordinates(90, 180, Building("test")))
        db.insert(DataAndPosition.with_coordinates(-90, -180, Building("test")))
        db.insert(DataAndPosition.with_coordinates(-90, 180, Building("test")))
        db.insert(DataAndPosition.with_coordinates(90, -180, Building("test")))

        assert db.contains(Position.with_coordinates(0, 0), 16)
        assert db.contains(Position.with_coordinates(90, 180), 16)
        assert db.contains(Position.with_coordinates(-90, -180), 16)
        assert db.contains(Position.with_coordinates(-90, 180), 16)
        assert db.contains(Position.with_coordinates(90, -180), 16)
        assert db.contains(Position.with_coordinates(90.5, -180.5), 16)
        assert not db.contains(Position.with_coordinates(1, -1), 16)
        assert not db.contains(Position.with_coordinates(45, -45), 16)

        db.delete(Position.with_coordinates(90, -180))

        assert not db.contains(Position.with_coordinates(90, -180), 16)

        db.delete(Position.with_coordinates(1, 1), 1)

        assert db.contains(Position.with_coordinates(-90, -180), 16)
        assert not db.contains(Position.with_coordinates(90, 180), 16)

        db.insert(DataAndPosition.with_coordinates(90, 180, Building("test")))

        assert db.contains(Position.with_coordinates(90, 180), 16)
