from abc import ABC
from enum import Enum, auto
from typing import List


class ListStrategy(ABC):
    def start(self, buffer:List):pass
    def end(self, buffer:List):pass
    def add_item(self, item:str, buffer:List): pass


class MarkdownListStrategy(ListStrategy):

    def add_item(self, item:str, buffer: List):
          buffer.append(f"* {item}\n")


class HtmlListStrategy(ListStrategy):

    def start(self, buffer: List):
        buffer.append("<ul>\n")

    def end(self, buffer: List):
        buffer.append('</ul>\n')

    def add_item(self, item:str, buffer: List):

          buffer.append(f'<li> {item} </li>\n')


class Strategy(Enum):
    Html=auto()
    Markdown=auto()


class TextProcessor:
    def __init__(self, strategy=HtmlListStrategy()):
        self.strategy=strategy
        self.buffer=[]

    def set_strategy_method(self,method:Strategy):
        if method == Strategy.Html:
            self.strategy=HtmlListStrategy()
        elif method == Strategy.Markdown:
            self.strategy=MarkdownListStrategy()
    def add_items(self, items: List[str]):
         self.strategy.start(self.buffer)
         for item in items:
             self.strategy.add_item(item, self.buffer)
         self.strategy.end(self.buffer)

    def __str__(self):
        return "".join(self.buffer)



if __name__ == '__main__':
    l= ["me","him", "her"]
    tp = TextProcessor()
    tp.set_strategy_method(Strategy.Markdown)
    tp.add_items(l)
    print(tp)

