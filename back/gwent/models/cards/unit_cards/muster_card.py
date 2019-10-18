from gwent.models.cards.unit_cards.unit_card import UnitCard


class MusterCard(UnitCard):
    def apply_abilities(self, board, adversary_board, player, adversary, target):
        for card in player.deck:
            if card.img_name.split('_')[0] == self.img_name.split('_')[0]:
                player.deck.remove(card)
                card.place_card(board, adversary_board, player, adversary, target)
