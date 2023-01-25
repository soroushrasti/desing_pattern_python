from typing import TextIO


class Test:
    A=5
    F=6
    def __init__(self):
        self.B=2

    def __getattr__(self, item):
        print(f"fetting atrr for {item}")
        return item

    def __setattr__(self, key, value):
        self.__dict__[key]=value

class LogFile:
    def __init__(self, file):
        self.file=file

    def writelines(self, strings):
        print(type(self.file))
        self.file.writelines(strings)
        print(f"Wrote {len(strings)} to file")

    def __getattr__(self, item):
        return getattr(self.file, item)

    def __delattr__(self, item):
        delattr(self.file, item)

    def __setattr__(self, key, value):
      if key=="file":
          self.__dict__["file"]=value
      else:
          setattr(self.file, key, value)

    def __iter__(self):
        return self.file.__iter__()

    def __next__(self):
        return self.file.__next__()




if __name__ == '__main__':
    a=open("test.txt", "w")
    print(type(a))
    file=LogFile(a)
    file.writelines(["Hellow", "World"])
    file.write("another line")
    file.close()
    file.b=3
    print(file.__dict__['file'])
    print(file.file)

