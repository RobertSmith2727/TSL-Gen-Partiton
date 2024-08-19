import unittest

from credit_card_validator import credit_card_validator


class Testshw1(unittest.TestCase):
    """
    Test credit card validator
    """

# ---------------------------prefix tests----------------------------

    #             -----invalid prefix and valid length----
    def test1(self):
        """Verifies if Visa with invalid prefix (visa length 16)
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("3475818283847901"))

    def test2(self):
        """Verifies if Visa/Mastercard with invalid prefix prefix
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("5072648520234853"))

    def test3(self):
        """Verifies if MasteCard with invalid prefix
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("5675848134039332"))

    def test4(self):
        """Verifies if MasteCard with invalid prefix
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("2220578293491014"))

    def test5(self):
        """Verifies if MasteCard with invalid prefix
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("2721689293483927"))

    def test6(self):
        """Verifies if AMEX with invalid prefix
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("335728293482039"))

    def test7(self):
        """Verifies if AMEX with invalid prefix
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("385728293482039"))

# --------------------valid prefix and invalid length-------------------
    def test8(self):
        """Verifies if Visa with valid prefix and invalid length 15
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("457393422940293"))

    def test9(self):
        """Verifies if Visa with valid prefix and invalid length 17
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("45739342294029357"))

    def test10(self):
        """Verifies if MC with invalid prefix prefix and length 15
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("517264852023485"))

    def test11(self):
        """Verifies if MC with invalid prefix prefix and length 15
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("557264852023485"))

    def test12(self):
        """Verifies if MC with invalid prefix prefix and length 17
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("51726485202348548"))

    def test13(self):
        """Verifies if MC with invalid prefix prefix and length 17
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("55726485202348548"))

    def test14(self):
        """Verifies if MasteCard with valid prefix and length 15
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("222157829349101"))

    def test15(self):
        """Verifies if MasteCard with valid prefix and length 15
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("272057829349101"))

    def test16(self):
        """Verifies if MasteCard with valid prefix and length 17
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("22215782934910134"))

    def test17(self):
        """Verifies if MasteCard with valid prefix and length 17
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("27205782934910134"))

    def test18(self):
        """Verifies if AMEX with valid prefix and length 14
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("34572829348203"))

    def test19(self):
        """Verifies if AMEX with valid prefix and length 16
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("3457282934820390"))

    def test20(self):
        """Verifies if AMEX with valid prefix and length 14
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("37572829348203"))

    def test21(self):
        """Verifies if AMEX with valid prefix and length 16
        returns False
        Picked using Category Partition Testing"""
        self.assertFalse(credit_card_validator("3757282934820390"))

# --------------------valid card (prefix and length) test------------------
    def test22(self):
        """Verifies if Visa with valid prefix and length
        returns False
        Picked using Category Partition Testing"""
        self.assertTrue(credit_card_validator("4457282934820345"))

    def test23(self):
        """Verifies if MC with valid prefix and length
        returns False
        Picked using Category Partition Testing"""
        self.assertTrue(credit_card_validator("5157282934820345"))

    def test24(self):
        """Verifies if MC with valid prefix and length
        returns False
        Picked using Category Partition Testing"""
        self.assertTrue(credit_card_validator("55557282934820345"))

    def test25(self):
        """Verifies if MC with valid prefix and length
        returns False
        Picked using Category Partition Testing"""
        self.assertTrue(credit_card_validator("2221282934820345"))

    def test26(self):
        """Verifies if MC with valid prefix and length
        returns False
        Picked using Category Partition Testing"""
        self.assertTrue(credit_card_validator("2720282934820345"))

    def test27(self):
        """Verifies if AMEX with valid prefix and length
        returns False
        Picked using Category Partition Testing"""
        self.assertTrue(credit_card_validator("345728293482034"))

    def test28(self):
        """Verifies if AMEX with valid prefix and length
        returns False
        Picked using Category Partition Testing"""
        self.assertTrue(credit_card_validator("375728293482034"))

# ----------------------- common errors------------------
    def test29(self):
        """Verifies if Visa with valid prefix and repeating numbers
        returns False
        Picked using common errors"""
        self.assertFalse(credit_card_validator("4444444444444444"))

    def test30(self):
        """Verifies if MC with valid prefix and repeating numbers
        returns False
        Picked using common errors"""
        self.assertFalse(credit_card_validator("5555555555555555"))

    def test31(self):
        """Verifies if MC with valid prefix and repeating numbers
        returns False
        Picked using common errors"""
        self.assertFalse(credit_card_validator("2222222222222222"))

    def test32(self):
        """Verifies if AMEX with valid prefix and repeating numbers
        returns False
        Picked using common errors"""
        self.assertFalse(credit_card_validator("343434343434343"))

    def test33(self):
        """Verifies if Visa/MC with repeating numbers 0's
        returns False
        Picked using common errors"""
        self.assertFalse(credit_card_validator("0000000000000000"))

    def test34(self):
        """Verifies if AMEX with repeating numbers 0's
        returns False
        Picked using common errors"""
        self.assertFalse(credit_card_validator("000000000000000"))

    def test35(self):
        """Verifies if All with empty card
        returns False
        Picked using common errors"""
        self.assertFalse(credit_card_validator(""))

    def test36(self):
        """Verifies if V/MC with 1234 common card demo number
        returns False
        Picked using common errors"""
        self.assertFalse(credit_card_validator("1234567890123456"))

    def test37(self):
        """Verifies if MC with 1234 common card demo number
        returns False
        Picked using common errors"""
        self.assertFalse(credit_card_validator("123456789012345"))

    def test38(self):
        """Verifies if Visa with Luhn algorithm error
        returns False
        Picked using common errors"""
        self.assertFalse(credit_card_validator("4012888888881882"))

    def test39(self):
        """Verifies if Visa with space error but valid length
        (16 including the space)
        returns False
        Picked using common errors"""
        self.assertFalse(credit_card_validator("40128888 8881881"))

    def test40(self):
        """Verifies if MC with space error but valid length
        (16 including the space)
        returns False
        Picked using common errors"""
        self.assertFalse(credit_card_validator("55128888 8881881"))

    def test41(self):
        """Verifies if MC with space error but valid length
        (16 including the space)
        returns False
        Picked using common errors"""
        self.assertFalse(credit_card_validator("22218888 8881881"))

    def test42(self):
        """Verifies if AMEX with space error but valid length
        (15 including the space)
        returns False
        Picked using common errors"""
        self.assertFalse(credit_card_validator("35218888 888188"))


if __name__ == '__main__':
    unittest.main(verbosity=2)
