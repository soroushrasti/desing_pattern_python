from abc import ABC


class Light:
    def __init__(self):
        self.state=SwitchOff()

    def on(self):
        self.state.on(self)

    def off(self):
        self.state.off(self)


class  Switch(ABC):

     def on(self, switch):
         print("Switch is already on")

     def off(self,switch):
         print("Switch is already off")
         return SwitchOff()

class SwitchOff(Switch):

     def on(self,switch:Light):
         print("Switching on")
         switch.state=SwitchOn()


class SwitchOn(Switch):

    def off(self,switch:Light):
        print("Switching off")
        switch.state=SwitchOn()


if __name__ == '__main__':
    l= Light()
    l.off()
    l.on()
    l.on()
    l.off()
    l.off()