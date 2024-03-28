class Robot():
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print(f'My name is {self.name}')

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print(f'New position is {self.position}')


class Robot_Dog(Robot):
    def make_noise(self):
        print('Woof!')


my_robot_dog = Robot_Dog('Buddy')

        
my_robot = Robot('test_bot')
my_robot.walk(110)
my_robot_dog.make_noise()