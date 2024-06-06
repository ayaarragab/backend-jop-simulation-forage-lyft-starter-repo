from unittest import TestCase
from battery.nubbin import NubbinBattery
from datetime import date
class TestNubbinBattery(TestCase):
    def setUp(self):
        self.battery1 = NubbinBattery(date(2019, 8, 1), date.today())
        self.battery2 = NubbinBattery(date(2023, 8, 1), date.today())
    def test_last_service_date(self):
        self.assertEqual(self.battery1.last_service_date, date(2019, 8, 1))
        self.assertEqual(self.battery2.last_service_date, date(2023, 8, 1))
    def test_current_date(self):
        self.assertEqual(self.battery1.current_date, date.today())
        self.assertEqual(self.battery2.current_date, date.today())
    def test_need_service(self):
        self.assertTrue(self.battery1.need_service())
        self.assertTrue(not self.battery2.need_service())