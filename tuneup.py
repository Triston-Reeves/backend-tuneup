__author__ = "Triston Reeves"

import cProfile
import pstats
import functools
import io
import timeit

def profile(fnc):
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval
    return inner 

def read_movies(src):
    """Returns a list of movie titles."""
    movieDic = {}
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        for movie in f.read().splitlines():
            if movie not in movieDic:
                movieDic[movie] = 1
            else: 
                movieDic[movie] += 1
    print(movieDic)
    return movieDic

@profile

def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    duplicates = []
    for movie in movies:
        if movies[movie] == 2:
            duplicates.append(movie)
    return duplicates

def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    t = timeit.Timer(stmt="main()", setup ="import tuneup")
    res = t.repeat(repeat=3, number=3)
    return res

def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))
    timeit_helper()

if __name__ == '__main__':
    main()