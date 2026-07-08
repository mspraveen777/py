""" Create the list of 5 movies. Print first, last and middle movie using both 
 -ve and +ve indexing """

movies = ["Pirates of the Caribein", "From", "Game of Thr   ones", "Kings", "Marvels"]
n = len(movies)
print(f" First movie: {movies[0]}")
print(f" Middle movie: {movies[n//2]}")
print(f"Last movie: {movies[n-1]}")