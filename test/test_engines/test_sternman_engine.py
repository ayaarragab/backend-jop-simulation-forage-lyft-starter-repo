from unittest import TestCase
from engine.sternman_engine import SternmanEngine
class TestWilloughbyEngine(TestCase):
    def setUp(self):
        self.engine1 = SternmanEngine(warning_light_is_on=True)
        self.engine2 = SternmanEngine(warning_light_is_on=False)
    def test_current_mileage(self):
        self.assertTrue(self.engine1.warning_light_is_on)
        self.assertFalse(self.engine2.warning_light_is_on)
    def test_need_service(self):
        self.assertTrue(self.engine1.need_service())
        self.assertTrue(not self.engine2.need_service())