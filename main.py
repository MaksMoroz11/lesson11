class Human:
    def __init__(self, name: str, age: int):
        """
        New human
        :param name: My name is... Who? My name is... What? My name is Chiki Chiki Slame Shady!
        :param age: I'm seriously! My age 18!
        """
        self.__name = name
        self.__age = age

    def info(self):
        print(f'Name: {self.__name}\nAge: {self.__age}')

    @property
    def age_category(self) -> str:
        if self.__age < 14:
            return 'Child'
        elif self.__age < 18:
            return 'Teenager'
        elif self.__age < 33:
            return 'Young'
        elif self.__age >= 33:
            return 'Adult'


if __name__ == '__main__':
    humans = [
        Human('Misha', 12),
        Human('Oleg', 16),
        Human('Anna', 15)
    ]

    for human in humans:
        human.info()
        print()
