from abc import ABC, abstractmethod
class AbstractParent(ABC):

    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError

    def build_house(self):
        print("Ama building haus")

class Mother(AbstractParent):
    def __init__(self, age):
        self.age = age
        print("mother constructor")

    def build_house(self):
        print("Ama lazy but also building haus")

    def do_work(self):
        print("I'm working")

    def do_house_work(self):
        print("listening music")

class Father(AbstractParent):
    def __init__(self):
        print("father constructor")
    def play_guitar(self):
        print("father is playing guitar")
    def do_house_work(self):
        print("sitting on sofa and drink beer")

class Daughter(Mother,Father):
    def __init__(self, age= 0):
        Mother.__init__(self, age=age)
        Father.__init__(self)
    def hello_friend(self):
        pass

    def do_work(self):
        print("I'm working like a horse")

class Friend:
    pass

def greet_mother(mother: Mother):
    print("hello mother")
    mother.do_work()

def greet_father(father: Father):
    print("time to beer!")
    father.play_guitar()

if __name__ == "__main__":
    daughter = Daughter()
    #mother.do_work()

    # change object class:
    #daughter.__class__ = Friend

    greet_mother(daughter)
    greet_father(daughter)
    daughter.hello_friend()
    daughter.do_house_work()

    #list
    for x in [daughter]:
        x.do_house_work()
    povtorka_list=["math-2","programmming 2","superprise"]
    #tuple
    vasian = ("11 years", 12, 3.14,daughter)

    #set
    my_set = {23,11,10,10,"call"}
    print(my_set)

    #frozen_set(immutable)
    another_set = frozenset(["di_","mi","do"])

    #dictionary(immutable as key)
    my_dict={1:"first","2":123 , (1,2,3):"tuple_as_a_key"}



