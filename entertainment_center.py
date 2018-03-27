import media
import fresh_tomatoes

# Define Favorite movies using Movie Class
super_troopers = media.Movie(
    "Super Troopers",
    "Always looking for action, five over-enthusiastic but under-stimulated Vermont State Troopers raise hell on the highway, keeping motorists anxiously looking in their rear-view mirrors.",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcS5B3MYcNqFg4jd0Z-H8z-vYmFYhWWJCCI-GHem3OVcdO-F-1JG",
    "https://www.youtube.com/watch?v=v4AE-ZoZarc")

super_troopers_2 = media.Movie(
    "Super Troopers 2",
    "Five wacky troopers must set up a new highway patrol station as the United States and Canada dispute the location of the border.",
    "https://ia.media-imdb.com/images/M/MV5BNDFiOTAxZmQtMGNmZS00OTM3LWE3YzUtNjYzNmU5NDE0ZGUwXkEyXkFqcGdeQXVyNjcxMDU4Nzk@._V1_.jpg",
    "https://www.youtube.com/watch?v=eEed-o8fVpM")

goodwill_hunting = media.Movie(
    "Good Will Hunting",
    "Will Hunting (Matt Damon) has a genius-level IQ but chooses to work as a janitor at MIT. When he solves a difficult graduate-level math problem, his talents are discovered by Professor Gerald Lambeau (Stellan Skarsgard), who decides to help the misguided youth reach his potential. When Will is arrested for attacking a police officer, Professor Lambeau makes a deal to get leniency for him if he will get treatment from therapist Sean Maguire (Robin Williams).",
    "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png",
    "https://www.youtube.com/watch?v=ReIJ1lbL-Q8")
toy_story = media.Movie(
    "Toy Story",
    "Woody (Tom Hanks), a good-hearted cowboy doll who belongs to a young boy named Andy (John Morris), sees his position as Andy's favorite toy jeopardized when his parents buy him a Buzz Lightyear (Tim Allen) action figure. Even worse, the arrogant Buzz thinks he's a real spaceman on a mission to return to his home planet. When Andy's family moves to a new house, Woody and Buzz must escape the clutches of maladjusted neighbor Sid Phillips (Erik von Detten) and reunite with their boy.",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# Define favorite movies in an array [add or remove ]
movies = [super_troopers, super_troopers_2, goodwill_hunting, toy_story]

# Run Website Application by calling fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
