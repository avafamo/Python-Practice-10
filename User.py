

class User:
    def __init__(self,userName):
        self.userName = userName
        self._password = "123"
        self.__message = "i love python"


class Person:

    def __init__(self):
        self.__message = "test message"

    # def login(self,gotPassword):
    #     if self._password == gotPassword:
    #         print("login user")
    #     else:
    #         print('you are not logged in')

me = User('Ava')
you = Person()

you._Person__message
me._User__message

# print(dir(me))