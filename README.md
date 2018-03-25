# Fresh Tomatoes Movie Trailers
Fresh Tomatoes Movie Trailer is server side code written in python that displays your favorite movie details along with a description, box art, and a link to the movie trailer.

## Installation
To run:
* Navigate to the root directory in `terminal`
* Run `python entertainment_center.py`

## Customization
To customize your own list of movies:
* Open `entertainment_center.py`
* Define a new Media class by invoking `media.Movie`
* The class `Movie` takes in 4 parameters:
1. `title` - String of the Movie Title (e.g. Toy Story)
2. `storyline` - String of the Storyline (e.g. "A movie about a boy and his toys")
3. `poster_image_url` - String of the movie's poster image location (e.g. "https://www.google.com/img.png")
4. `trailer_youtube_url` - String of the movie's youtube trailer link, NOTE: you must use a Youtube link (e.g. "https://www.youtube.com/watch?v=v4AE-ZoZarc")
* Add the class into the `movies` array located on `Line 25` of `entertainment_center.py`
