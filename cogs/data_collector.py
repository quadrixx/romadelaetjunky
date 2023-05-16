import random

from Demotivor import Demotivator


class Static:
    def __init__(self, msg_rdy: bool, url_rdy: bool, lom, lou):
        self.msg_rdy = msg_rdy
        self.url_rdy = url_rdy
        self.lom = lom
        self.lou = lou

    def update(self, msg, url, lom, lou):
        self.msg_rdy = msg
        self.url_rdy = url
        self.lom = lom
        self.lou = lou
        print(self.lom)
        print(self.lou)
        if self.msg_rdy == True and self.url_rdy == True:
            print(self.lom)
            print(self.lou)
            self.create_demo(self.shuffle(self.lom, self.lou))

    def create_demo(self, lst):
        dem = Demotivator(*lst)

    def shuffle(self, lom: list, lou: list) -> list:
        for_dem = []
        for i in range(2):
            a = random.randint(0, len(lom))
            for_dem.append(lom[a])
        a = random.randint(0, len(lou))
        for_dem.append(lou[a])





