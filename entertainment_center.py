import media
import engine

# Instantiate movies with titles, links to posters, and links to trailers.
maldives = media.Movie(
                            "Anxiety Treatment: Maldives",
                            "https://i.ytimg.com/vi/U50o92vADOg/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLCGInbF_gv9AgWKrYY867ZWbtc_Aw",
                            "https://www.youtube.com/watch?v=U50o92vADOg"
                        )

thailand = media.Movie(
                            "Life Rhythm In Southeast Asia",
                            "https://i.ytimg.com/vi/jZStK7nfYYo/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAbUiooSjew67RdeBproi-iCslsUw",
                            "https://www.youtube.com/watch?v=jZStK7nfYYo"
                        )

saipan = media.Movie(
                           "Meditation: Saipan In 4K",
                           "https://i.ytimg.com/vi/FOr7NvXxQQs/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLDD3sASab0XevNtdbOBhmlOzLQrkw",
                           "https://www.youtube.com/watch?v=FOr7NvXxQQs&t=2s"
                    )

everest = media.Movie(
                           "Flying above Mount Everest",
                           "https://i.ytimg.com/vi/P3sr9xLQpWQ/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLB4ApPYNz208YnqmcFWrWPbXXvR2w",
                           "https://www.youtube.com/watch?v=P3sr9xLQpWQ"
                    )

panda = media.Movie(
                          "Animal Kingdom: Cute Pandas",
                          "https://i.ytimg.com/vi/gTY16FDO-BQ/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAa-IL5gkE8NxGalvTRJxIp6T48Rg",
                          "https://www.youtube.com/watch?v=gTY16FDO-BQ"
                    )

crab = media.Movie(
                          "Animal Kingdom: Hermit Crabs",
                          "https://i.ytimg.com/vi/tBzgT5godVA/hqdefault.jpg?sqp=-oaymwEXCNACELwBSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLAFEI13SBwFxmrmQumgz7Vu7G2YYA",
                          "https://www.youtube.com/watch?v=tBzgT5godVA&t=10s"
                  )
# Construct an array to hold all instances of movies.
movies = [
            maldives,
            thailand,
            saipan,
            everest,
            panda,
            crab
         ]

# Open the result in a browser.
engine.open_movies_page(movies)
