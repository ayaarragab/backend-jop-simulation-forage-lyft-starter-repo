from unittest import TestCase
from engine.willoughby_engine import WilloughbyEngine
class TestWilloughbyEngine(TestCase):
    def setUp(self):
        self.engine1 = WilloughbyEngine(70000, 10000)
        self.engine2 = WilloughbyEngine(70000, 90000)
    def test_current_mileage(self):
        self.assertEqual(self.engine1.current_mileage, 70000)
        self.assertEqual(self.engine2.current_mileage, 70000)
    def test_last_mileage(self):
        self.assertEqual(self.engine1.last_service_mileage, 10000)
        self.assertEqual(self.engine2.last_service_mileage, 90000)
    def test_need_service(self):
        self.assertTrue(self.engine1.need_service())
        self.assertTrue(not self.engine2.need_service())