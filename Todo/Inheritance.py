def eat():
    print("Eating...")


class Bird:

    def sleep(self):
        print("Sleeping...")

    def walk(self):
        print("Walking...")


class Penguin(Bird):
    def fly(self):
        print("Can't Fly!!!!")


class Eagle(Bird):
    def fly(self):
        print("Can Fly!!!")


pen = Penguin()
eag = Eagle()

pen.fly()
