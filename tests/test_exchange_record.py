"""检查交换数据中用于回查的事实。"""
import unittest

import numpy as np

from fractional_exposure_input import load_record


class ExchangeRecordTests(unittest.TestCase):
    def test_exchange_contract(self):
        record = load_record()
        self.assertTrue(any(0 in k[2] for k in record["knots"]) and record["knots"][1][1][1] == 0)
        self.assertTrue(record["clock"][0]["points"][1] != record["clock"][1]["points"][1])
        self.assertTrue(record["exposures"][1]["window"][0] < record["clock"][0]["points"][1][0] < record["exposures"][1]["window"][-1])
        self.assertTrue(record["events"][1][0] == "lock" and record["events"][-1][0] == "gap_after")
