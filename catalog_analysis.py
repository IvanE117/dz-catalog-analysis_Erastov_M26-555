import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },  # noqa: E501
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


# ----------------- Этап 1. Разминка: переменные, числа, math -----------------
def average_rating(movies):
    """Функция возвращает среднюю оценку по каталогу"""
    ratings = [movie["rating"] for movie in movies]
    return round(sum(ratings) / len(ratings), 1)


def catalog_age_stats(movies, current_year=2026):
    """
    Функция возвращает кортеж (самый старый фильм в годах,
    самый новый фильм в годах, среднее).
    """
    release_years = [current_year - movie["year"] for movie in movies]
    release_years.sort(reverse=True)
    return (
        release_years[0],
        release_years[-1],
        math.ceil(sum(release_years) / len(release_years)),
    )


def duration_in_hours(minutes):
    return f"{minutes // 60}ч {minutes % 60}м"


# ----------------- Этап 2. Условия и match -----------------
def rating_tier(rating):
    """Функция, которая по оценке возвращает категорию."""
    if rating >= 9:
        return "шедевр"
    elif 7 <= rating < 9:
        return "хорошо"
    else:
        return "средне" if 5 <= rating < 7 else "слабо"


def decade_label(year):
    """Функция, которая возвращает метку "новые", "недавние" или "старые"."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _ if year < 2015:
            return "старые"


# ----------------- Этап 3. Строки ---------------------
def for_and_while_cycles(movies):
    """Демонстрация работы с for, while и управляющими конструкциями циклов."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])

    i = 0
    while i < len(movies):
        if movies[i]["rating"] > 9:
            print(movies[i]["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    """
    Функция, которая с накопительной переменной считает количество фильмов
    длиннее threshold минут.
    """
    counter = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            counter += 1
    return counter


# ----------------- Этап 4. Циклы ---------------------
def normalize_title(title):
    """Функция, которая приводит строку к формату Title Case."""
    return " ".join([word[0].upper() + word[1:] for word in title.lower().split()])


def make_slug(title):
    """
    Функция, которая превращает нормализованное название в «слаг» вида
    the-quiet-algorithm.
    """
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    """Функция, возвращающая единую строку с описанием фильма."""
    return (
        f'"{movie["title"]}" ({movie["year"]}) — '
        f"{movie['rating']}/10, "
        f"{duration_in_hours(movie['duration_min'])}, "
        f"жанры: {', '.join(sorted(movie['genres']))}"
    )

def format_report_line_for_report(movie):
    """Функция, возвращающая единую строку с описанием фильма."""
    return (
        f'"{normalize_title(movie["title"])}" ({movie["year"]}) — '
        f"{movie['rating']}/10, "
        f"{duration_in_hours(movie['duration_min'])}, "
        f"жанры: {', '.join(sorted(movie['genres']))}"
    )


# ----------------- Этап 5. Списки ---------------------
def sorted_movie_title_and_rating(movies):
    title_and_rating = [[movie["title"], movie["rating"]] for movie in movies]
    return sorted(title_and_rating, key=lambda movie: movie[1], reverse=True)


def titles_sorted_by_rating(movies):
    """
    Функция, возвращающая список названий фильмов, отсортированных по убыванию рейтинга.
    """
    return [title for title, _ in sorted_movie_title_and_rating(movies)]


def top_n_by_rating(movies, n=3):
    """Функция, возвращающая список из n кортежей (title, rating) — топ по рейтингу."""
    return [tuple(movie) for movie in sorted_movie_title_and_rating(movies)][:n]


# ----------------- Этап 6. Словари ---------------------
def count_by_genre(movies):
    """Функция, возвращающая словарь {жанр: количество фильмов}."""
    all_genres_dict = dict()
    for movie in movies:
        for genre in movie.get("genres", []):
            all_genres_dict[genre] = all_genres_dict.get(genre, 0) + 1
    return all_genres_dict


def actor_filmography(movies):
    """Функция, возвращающая словарь {актер: [список названий фильмов]}."""
    all_actors_dict = dict()
    for movie in movies:
        for actor in movie.get("actors", []):
            if actor not in all_actors_dict:
                all_actors_dict[actor] = []
            all_actors_dict[actor].append(movie["title"])
    return all_actors_dict


def dict_comprehension(movies):
    """
    Функция, возвращающая словарь {title: rating} только для фильмов с рейтингом
    выше среднего.
    """
    avrg = average_rating(movies)
    return {
        movie["title"]: movie["rating"] for movie in movies if movie["rating"] > avrg
    }


# ----------------- Этап 7. Множества ---------------------
def all_genres(movies):
    """Функция, возвращающая множество всех уникальных жанров каталога."""
    result = set()
    for movie in movies:
        result.update(movie["genres"])
    return result


def common_actors(movie1, movie2):
    """Функция, возвращающая множество актеров, снимавшихся в обоих фильмах."""
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    """
    Функция, которая возвращает жанры, встречающиеся в movies_a,
    но не встречающиеся в movies_b.
    """
    set_movies_a = set.union(*[movie["genres"] for movie in movies_a])
    set_movies_b = set.union(*[movie["genres"] for movie in movies_b])
    return set_movies_a - set_movies_b


# ----------------- Этап 8. Итераторы и генераторы ---------------------
def iter_high_rated(movies, min_rating=8.0):
    """
    Функция-генератор, которая через yield лениво отдает фильмы с рейтингом
    не ниже min_rating.
    """
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def generator_example(movies):
    return sum(movie["duration_min"] for movie in movies if movie["rating"] > 7)


# ----------------- Этап 9. Итоговый отчет ---------------------
def build_report(movies):
    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет")

    print()
    print("Топ-3 фильма:")
    for title, _ in top_n_by_rating(movies):
        for movie in movies:
            if movie.get("title", 0) == title:
                print(f"    {format_report_line_for_report(movie)}")

    print()
    print("Фильмов по жанрам:")
    for genre, film_numbers in sorted(
        count_by_genre(movies).items(), key=lambda item: item[1], reverse=True
    ):
        print(f"    {genre} — {film_numbers}")

    print()
    print(f"Все жанры каталога: {', '.join(sorted(all_genres(movies)))}")


if __name__ == "__main__":
    build_report(movies)
