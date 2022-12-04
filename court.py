from __future__ import annotations
from datetime import date


class Court:
    __width: float
    __length: float
    __address: str
    __year_built: int

    def __init__(self, width: float = 68, length: float = 150,
                 address: str = None, year_built: int = 1) -> None:
        if 45 <= width <= 90 <= length <= 120:
            self.__width = width
            self.__length = length
        else:
            self.__width = 68
            self.__length = 150
        self.__address = address
        self.__year_built = year_built

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, value: float) -> None:
        if 45 <= value <= 90:
            self.__width = value

    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, value: float) -> None:
        if 90 <= value <= 120:
            self.__length = value

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value: str) -> None:
        self.__address = value

    @property
    def year_built(self) -> int:
        return self.__year_built

    @year_built.setter
    def year_built(self, value: int) -> None:
        self.__year_built = value

    def area(self) -> float:
        return self.width * self.length

    @staticmethod
    def validate(court):
        curr_year = date.today().year
        if curr_year < court.year_built or court.year_built < 0:
            court.year_built = curr_year

    def __str__(self) -> str:
        return f"Boisko wybudowane w roku {self.year_built}, o długości {self.length} " \
               f"metrów i szerokości {self.width} metrów.\n" \
               f"Pole powierzchni: {self.area()} mkw. \n"\
               f"Adres: {self.address}\n."

    def __eq__(self, other: Court) -> bool:
        return self.area() == other.area()

    def __ne__(self, other: Court) -> bool:
        return self.area() != other.area()
