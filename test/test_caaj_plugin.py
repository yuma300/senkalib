import unittest
from decimal import Decimal
from typing import List, Union

from senkalib.caaj_journal import CaajJournal
from senkalib.caaj_plugin import CaajPlugin
from senkalib.platform.transaction import Transaction


class SampleCaajPlugin(CaajPlugin):
    @classmethod
    def can_handle(cls, transaction: Union[Transaction, str]) -> bool:
        return True

    @classmethod
    def get_caajs(
        cls, address: str, transaction: Union[Transaction, None]
    ) -> List[CaajJournal]:
        jounal = CaajJournal(
            "2022-01-01 00:00:00",
            "platform",
            "application",
            "service",
            "0x00000000",
            "3232-543543-5435443-543453",
            "deposit",
            Decimal("0.005147"),
            "juno",
            "ibc/46B44899322F3CD854D2D46DEEF881958467CDD4B3B10086DA49296BBED94BED",
            "3a2570c5-15c4-2860-52a8-bff14f27a236",
            "0xaaaaa",
            "0xbbbbb",
            "hello world",
        )
        return [jounal]


class TestCaajPlugin(unittest.TestCase):
    def test_cat_handle(self):
        result = SampleCaajPlugin.can_handle("XXXXXXXXXXXXXXXXXXXXXXX")
        assert result is True

    def test_get_caajs(self):
        result = SampleCaajPlugin.get_caajs("0x1111111111111111", None)
        assert type(result[0]) == CaajJournal


if __name__ == "__main__":
    unittest.main()
