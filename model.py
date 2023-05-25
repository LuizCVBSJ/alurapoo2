class Media:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def add_likes(self, likes=1):
        self._likes += likes

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


class Movie(Media):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def print(self):
        print(f'Title: {self._name} | Year: {self.year} | Duration: {self.duration} min | Likes: {self.likes}')


class Show(Media):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def print(self):
        print(f'Title: {self._name} | Year: {self.year} | Seasons: {self.seasons} | Likes: {self.likes}')


avengers = Movie('avengers - infinity war', 2018, 160)
atlanta = Show('friends', 1994, 10)
avengers.add_likes(787433)

atlanta.add_likes(53843)

movies_and_shows = [avengers, atlanta]

for program in movies_and_shows:
    print('------------------')
    program.print()
    print('------------------')