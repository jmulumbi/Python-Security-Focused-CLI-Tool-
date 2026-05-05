from CLI_Final import (verify_credit_card,hash_pin,verify_pin,load_data,show_cards,main)
class TestCreditCardValidation:
    def test_verify_credit_card_known_cards(self):
        card = "1234123412361236"
        result = verify_credit_card(card)
        assert result == True
