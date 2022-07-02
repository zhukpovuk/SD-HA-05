class Philosopher(Thread):

    def __init__(self, table, seat):
        self.table_ = table
        self.seat_ = seat
        self.left_chopstick_ = self.table_.left_chopstick(seat)
        self.right_chopstick_ = self.table_.right_chopstick(seat)
        self.meals_ = 0

    def eat(self):
        self.__acquire_chopsticks()
        self.__eat_with_chopsticks()
        self.__release_chopsticks()

    def think(self):
        time.sleep(random.random() * 5)  # think 0-5 seconds

    def run(self):
        while True:
            self.eat()
            self.think()

    def __acquire_chopsticks(self):
        self.forks[philosopher].acquire()
        self.forks[(philosopher + 1) % 5].acquire()


    def __eat_with_chopsticks(self):
        time.sleep(random.random() * 5)  # eat 0-5 seconds
        self.meals_ += 1

    def __release_chopsticks(self):
        self.forks[philosopher].release()
        self.forks[(philosopher + 1) % 5].release()
