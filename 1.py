import time

def calculate_time(func):
    def main(args, **kwargs):
        start_time = time.time()
        func(args, **kwargs)
        time.sleep(2)
        end_time = time.time()
        print("Total time taken in : ", func.name, end_time - start_time)
    return main

@calculate_time
def waste_time():
    x=0
    for i in range(0,1000):
        x+=i

waste_time()