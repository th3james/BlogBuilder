from datetime import datetime
from unittest import TestCase

from blogbuilder.post_repository import Month


class MonthTest(TestCase):
    def test_from_datetime_middle_of_month(self) -> None:
        """
        given a datetime in the middle of the month
        it sets the month to the beginning of the month
        """
        mid_month = datetime.fromisoformat("2021-03-09")
        month_start = datetime.fromisoformat("2021-03-01")
        assert month_start == Month.from_datetime(mid_month).datetime

    def test_name_returns_the_name_and_year(self) -> None:
        """
        given a month
        it returns the month name and year
        """
        assert "March 2021" == Month(datetime.fromisoformat("2021-03-01")).name
        assert "November 2019" == Month(datetime.fromisoformat("2019-11-01")).name
