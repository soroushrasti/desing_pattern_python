from time import sleep, time

def time_it(func):
    def wrapper():
        start=time()
        func()
        end=time()
        print(f"it took {end-start} seconds")
    return wrapper
@time_it
def some_op():
    sleep(1)
    print("finished")

if __name__=="__main__":
    # time_it(some_op)()
    some_op()