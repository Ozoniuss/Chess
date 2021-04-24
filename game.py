class Game:

    # will have the id of the game
    def __init__(self, id):

        self.id = id # id of the game
        self.turn = None
        self.ready = False
        self.moves= [None, None]

    def get_player_move(self, player):
        return self.moves[player]

    def connected(self):
        return self.ready