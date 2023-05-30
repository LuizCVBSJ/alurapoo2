class Media():
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

    def __str__(self):
        return f'Title: {self._name} | Year: {self.year} | Likes: {self.likes}'


class Movie(Media):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'Title: {self._name} | Year: {self.year} | Duration: {self.duration} min | Likes: {self.likes}'


class Show(Media):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'Title: {self._name} | Year: {self.year} | Seasons: {self.seasons} | Likes: {self.likes}'


class Playlist():
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __len__(self):
        return len(self._programs)

    def __getitem__(self, item):
        return self._programs[item]

    def duration(self):
        movie_duration = 0
        show_seasons = 0
        for PROGRAM in self._programs:
            if isinstance(PROGRAM, Movie):
                movie_duration += PROGRAM.duration
            elif isinstance(PROGRAM, Show):
                show_seasons += PROGRAM.seasons
        return '{} Minutes of Movies and {} Seasons of Shows'.format(movie_duration, show_seasons)


avengers = Movie('avengers - infinity war', 2018, 160)
star_wars = Movie('star wars - the last jedi', 2017, 150)
scary_movie = Movie('scary movie', 2000, 90)

atlanta = Show('friends', 1994, 10)
games_of_thrones = Show('games of thrones', 2011, 7)

avengers.add_likes(787433)
star_wars.add_likes(123123)
scary_movie.add_likes(123)
atlanta.add_likes(53843)
games_of_thrones.add_likes(100000)

movies_and_shows = [avengers, star_wars, scary_movie, atlanta, games_of_thrones]

weekend_playlist = Playlist('weekend playlist', movies_and_shows)

print('------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------')
print(f'Playlist length: {len(weekend_playlist)}, Duration: {weekend_playlist.duration()}')
print('------------------------------------------------------------------------------------')
for program in weekend_playlist:
    print(program)
print('------------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------------')
