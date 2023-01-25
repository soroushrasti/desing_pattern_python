from typing import Optional


class Bitmap:
    def __init__(self, filename: str):
        self.filename = filename
        print("Loading the file")

    def draw(self):
        print("Staring drawing")
        print("Drawing image")
        print("Finished drawing")

class LazyBitmap:
    def __init__(self, filename:str):
        self.filename=filename
        self.bitmap: Optional[Bitmap]=None

    def draw(self):
        if not self.bitmap:
            self.bitmap=Bitmap(self.filename)
        self.bitmap.draw()

if __name__ == '__main__':
    bt= LazyBitmap("Newfile.jpg")
    bt.draw()
    bt.draw()
