


class Buffer:
    def __init__(self, high=10, width=20):
        self.buffer=" "* (high* width)

    def write(self, string):
        self.buffer+=string

    def __getattr__(self, item):
        return self.buffer.__getitem__(item)

class Viewport:
    def __init__(self, buffer: Buffer):
        self.buffer=buffer
        self.margin=0

    def get_char_at(self, index):
        return self.buffer[index +self.margin]

# facade
class Console:
    def __init__(self):
        b= Buffer()
        vp=Viewport(b)
        self.viewports=[vp]
        self.buffers=[b]
        self.current_viewport=vp

    def write(self, text):
       self.current_viewport.buffer.write(text)





