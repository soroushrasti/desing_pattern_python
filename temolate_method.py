from abc import ABC


class Game(ABC):
    def __init__(self, number_of_player,name="Game"):
        self.name = name
        self.number_of_player = number_of_player
        self.current_palyer=0

    def start(self):
        print(f"The game {self.name} is started with {self.number_of_player} players")

    def run(self):
        self.start()
        while not self.have_winner:
            self.take_turn()

        print(f"The {self.winning_player} player wins the game")

    def take_turn(self): pass

    @property
    def winning_player(self):
       pass

    @property
    def have_winner(self): pass



class Chess(Game):
    def __init__(self):
        super().__init__(2)
        self.turn=0
        self.max_turns=10

    def start(self):
        super().start()

    def run(self):
        super().run()

    def take_turn(self):
        print(f"Turn {self.turn} is taken by player {self.current_palyer} ")
        self.turn+=1
        self.current_palyer= 1 - self.current_palyer

    @property
    def winning_player(self):
        return self.current_palyer


    @property
    def have_winner(self):
        return self.turn >=self.max_turns


if __name__ == '__main__':
    chess=Chess()
    chess.run()