

class TextFormatting:
    def __init__(self, text):
        self.text = text
        self.formatting=[]

    class Formatting:
        def __init__(self, start, end, capitalize=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        def covers(self, i):
          return  self.start <= i <= self.end

    def get_range(self, start, end):
        range=self.Formatting(start, end)
        self.formatting.append(range)
        return range



    def __str__(self):
       result=[]
       for i,c in enumerate(self.text):
          for f in self.formatting:
              if f.covers(i):
                  c=c.upper()
              result.append(c)
       return "".join(result)


class BetterTextFormatting:
    def __init__(self, text):
        self.text = text
        self.formatting=[]

    class Formatting:
        def __init__(self, start, end, capitalize=False):
            self.start = start
            self.end = end
            self.capitalize = capitalize

        def covers(self, i):
            return  self.start <= i <= self.end and self.capitalize

    def get_range(self, start, end):
        range=self.Formatting(start, end)
        self.formatting.append(range)
        return range

    def __str__(self):
       result=[]
       for i,c in enumerate(self.text):
          for f in self.formatting:
              if f.covers(i):
                  c=c.upper()
              result.append(c)
       return "".join(result)

if __name__ == '__main__':
    text="This is a new text"
    tf=BetterTextFormatting(text)
    tf.get_range(2,3).capitalize=True
    print(tf)