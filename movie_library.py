import random
from datetime import date  

class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.streams = 0

    def __str__(self):
        return f'{self.title} ({self.year}) {self.streams}\n'

    def play(self):
        self.streams +=1
        return f'{self.streams}'


class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f'{self.title} S{self.season:02d}E{self.episode:02d} {self.streams}\n'    
    
    def play(self):
        self.streams +=1
        return f'{self.streams}'


movie1 = Movie(title="'The Unforgivable'", year = 2021, genre = "'Drama/Thriller'")
movie2 = Movie(title="'The Blind Side'", year = 2009, genre = "Sport/Drama")
movie3 = Movie(title="Titanic", year = 1997, genre = "Catastrophic")
movie4 = Movie(title="The Proposal", year = 2009, genre = "Romance/Comedy")
movie5 = Movie(title="The Pursuit of Happyness", year = 2006, genre = "Drama")
movie6 = Movie(title="Spider-Man: Bez drogi do domu", year = 2021, genre = "Action / Sci-Fi")
movie7 = Movie(title="Jurassic World", year = 2015, genre = "Science fiction action film ")
movie8 = Movie(title="The Lion King", year = 1994, genre = " Animated musical drama")


Series1 = Series(title="The Crown", year = 2016, genre = "Drama", season = 1, episode = 1)
Series2 = Series(title="The Crown", year = 2016, genre = "Drama", season = 1, episode = 2)
Series3 = Series(title="The Crown", year = 2016, genre = "Drama", season = 1, episode = 3)
Series4 = Series(title="Death in Paradise", year = 2011, genre = "British–French crime comedy drama", season = 1, episode = 9)
Series5 = Series(title="Death in Paradise", year = 2011, genre = "British–French crime comedy drama", season = 1, episode = 10)
Series6 = Series(title="Death in Paradise", year = 2016, genre = "British–French crime comedy drama", season = 8, episode = 5)
Series7 = Series(title="Death in Paradise", year = 2016, genre = "British–French crime comedy drama", season = 8, episode = 6)

one_list = [movie1, movie2, movie3, movie4, movie5, movie6, movie7, movie8, Series1, Series2, Series3, Series4, Series5, Series6, Series7]

filtered_list = []


def get_movies():
    for i in one_list:
        if isinstance(i,Series)!= True:
            filtered_list.append(i)
        else:
            pass
    by_title_asc = sorted(filtered_list, key=lambda m: m.title)
    return by_title_asc


def get_Series():
    for i in one_list:
        if isinstance(i,Series)== True:
            filtered_list.append(i)
        else:
            pass
    by_title_asc = sorted(filtered_list, key=lambda m: m.title)
    return by_title_asc


def search(title):    
    searched =[]
    for i in one_list:
        if title == i.title:
            searched.append(i)
            return i
        else:
            pass
    if len(searched)==0:
            print('No such title in the library!')


def generate_views():
    i = random.choice(one_list)
    i.streams = random.choice(range(1,101))
    return i


def run_generate_views():
    for i in range(9):
        generate_views()



def top_titles(top_number, content_type):
  
    for i in one_list:
        i.streams = random.choice(range(1,101))
    if content_type == "Movie":
        get_movies()
    elif content_type == "Series":
        get_Series()
    else:
        print('Choose a Movie or Series!')
        exit(1)


    by_popularity = sorted(filtered_list, key=lambda i: i.streams, reverse = True)
    today = date.today().strftime("%d.%m.%Y")
    text = f'The film and Seriess of the day {today}:\n'

    return text,*by_popularity[0:top_number]


def main():
    result = "Films Library\n"
    result2 = top_titles(3, "Movie")
    print(result, *result2)

if __name__ == "__main__":
    main()