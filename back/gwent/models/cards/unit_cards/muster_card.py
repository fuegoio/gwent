from gwent.models.cards.unit_cards.unit_card import UnitCard


class MusterCard(UnitCard):
    def __init__(self, id: str, name: str, img_name: str, agile: bool, hero: bool, faction: str, power: int, row: int):
        super().__init__(id, name, img_name, agile, hero, faction, power, row)
        self.type = 'muster'

    def apply_abilities(self, board, adversary_board, player, adversary, target):
        for card in player.deck:
            if card.id.split('_')[0] == self.id.split('_')[0]:
                player.deck.remove(card)
                card.place_card(board, adversary_board, player, adversary, target)
