from stadium import *
from court import *


def main() -> None:
    court_1: Court = Court(address='Słoneczna 10, 10-100 Olsztyn.',
                           year_built=1999)
    print(court_1)
    court_2: Court = Court(500, 500, 'Słoneczna 10, 10-100 Olsztyn.', 1999)
    print(court_2)
    court_3: Court = Court(50, 100, "Słoneczna 10, 10-100 Olsztyn.", 1999)
    print(court_3)
    print(court_1.length)
    court_1.year_built = 1990
    print(court_1)
    print(court_1.area())
    court_1.year_built = 2030
    print(court_1)

    stadium_1: Stadium = Stadium(address="Słoneczna 10, 10-100 Olsztyn.",
                                 name="Słoneczny stadion", common_name="Słoneczko",
                                 capacity=10000, year_built=1999)
    print(stadium_1)
    stadium_2: Stadium = Stadium(50, 100, "Słoneczna 10, 10-100 Olsztyn",
                                 1999, "Słoneczny stadion",
                                 capacity=10000)
    print(stadium_2)
    assert stadium_1.year_built == 1999
    print(stadium_1.__eq__(stadium_2))
    stadium_1.width = 50
    stadium_1.length = 100
    print(stadium_1.__eq__(stadium_2))
    print(stadium_1.__ne__(stadium_2))
    stadium_1.capacity = 500
    print(stadium_1.__eq__(stadium_2))


if __name__ == "__main__":
    main()
