from collections.abc import Collection

from cs5278_assignment_4.live6.data_and_position import DataAndPosition
from cs5278_assignment_4.live6.example.building import Building
from cs5278_assignment_4.live6.position import Position
from cs5278_assignment_4.live6.proximity_db import ProximityDB


class VanderbiltBuildings:
    @staticmethod
    def main() -> None:
        """
        The idea behind the ProximityDB is that we can store arbitrary
        objects in it at a location. For example, the database could store
        the locations of buildings on Vanderbilt's campus. The type of
        object should be up to the user and is thus a type parameter.
        You could just as easily store RealEstateListing objects, Maps, etc.

        It is important to note that the DataAndPosition objects that the database
        holds are containers for associating a position with the type of data that
        you want to store. Although the ProximityDB[T] is parameterized by T,
        internally it stores objects of type DataAndPosition[T].
        """

        kirkland_hall: Building = Building("Kirkland Hall")
        fgh: Building = Building("Featheringill Hall")
        esb: Building = Building("Engineering Sciences Building")

        db: ProximityDB[Building] = None  # Replace with a new instance of your ProximityDB impl.

        db.insert(DataAndPosition.with_coordinates(36.145050, 86.803365, fgh))
        db.insert(DataAndPosition.with_coordinates(36.148345, 86.802909, kirkland_hall))
        db.insert(DataAndPosition.with_coordinates(36.143171, 86.805772, esb))

        # Find all the other buildings near a location
        buildings_near_fgh: Collection[DataAndPosition[Building]] = \
            db.nearby(Position.with_coordinates(36.145050, 86.803365), 28)

        for building_and_pos in buildings_near_fgh:
            building = building_and_pos.get_data()

            print(f"{building.getName()} is located at "
                  f"{building_and_pos.get_latitude()}, "
                  f"{building_and_pos.get_longitude()}")
