class Error(Exception):
    pass


class UnauthorizedActionError(Error):
    def __init__(self, message):
        self.message = message


class CardNotFoundError(Error):
    message = None

    def __init__(self, card):
        self.card = card
        self.message = 'Card not found : ' + str(self.card)
