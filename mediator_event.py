

class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Game:
    def __init__(self):
        self.events=Event()

    def fire(self, args):
       self.events(args)


class Player:
    def __init__(self, name:str, game:Game):
        self.name = name
        self.game = game
        self.scores=0

    def score(self):
        self.scores+=1
        self.game.fire(GameScoreInfo(self.name,self.scores))



class Coach:
    def __init__(self,game: Game):
        game.events.append(self.congratulate)

    def congratulate(self, args):
        if isinstance(args,GameScoreInfo):
            if args.scores <4:
                print(f"congradualte {args.who_scored} for scoring {args.scores}")




class GameScoreInfo:
    def __init__(self, who_scored: str, scores: int):
        self.scores = scores
        self.who_scored = who_scored



if __name__ == '__main__':
    game=Game()
    coach=Coach(game)

    player=Player("Bak", game)
    player2=Player("Alic", game)

    player2.score()
    player.score()


