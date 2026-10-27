import unittest

def is_unsafe(gate_closed, in_danger_zone):
    return bool(gate_closed and in_danger_zone)

class DetectionRuleTests(unittest.TestCase):
    def test_closed_gate_and_danger_zone_triggers_alert(self):
        self.assertTrue(is_unsafe(True, True))

    def test_open_gate_does_not_trigger_alert(self):
        self.assertFalse(is_unsafe(False, True))

    def test_clear_zone_does_not_trigger_alert(self):
        self.assertFalse(is_unsafe(True, False))

    def test_open_gate_and_clear_zone_is_safe(self):
        self.assertFalse(is_unsafe(False, False))

if __name__ == "__main__":
    unittest.main()
