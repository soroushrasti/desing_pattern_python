from enum import Enum, auto


class State(Enum):
    LOCKED= auto()
    UNLOCKED=auto()
    FAILED=auto()

if __name__ == '__main__':
    state=State.LOCKED
    code='1234'
    entry=''

    while True:
        if state == State.LOCKED:
            entry+=input(entry)

            if entry== code:
                state=State.UNLOCKED

            if not code.startswith(entry):
                state=State.FAILED

        elif state == State.FAILED:
             print("Failed")
             entry=""
             state=State.LOCKED

        elif state == State.UNLOCKED:
              print("Unlocked")
              state=State.UNLOCKED
              break






