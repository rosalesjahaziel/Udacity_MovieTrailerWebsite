import media
import fresh_tomatoes   #Library to create movie trailers
import game_tomatoes    #Library to create game trailers

"""
Movies init information
 'instance_name' = media.Movie('movie_name','cover_url','trailer_url')
"""  

donnie_darko = media.Movie("donnie darko",
                        "https://upload.wikimedia.org/wikipedia"+
                        "/en/d/db/Donnie_Darko_poster.jpg",
                        "https://www.youtube.com/watch?v=ZZyBaFYFySk")

lala_land = media.Movie("La La Land",
                   "https://consequenceofsound.files.wordpress.com"+
                   "/2016/12/la-la-land1.jpg?quality=80&w=380&h=380&crop=1",
                   "https://www.youtube.com/watch?v=0pdqf4P9MB8")

watchmen = media.Movie("Watchmen",
                    "https://upload.wikimedia.org/wikipedia/commons"+
                    "/thumb/6/65/Watchmen-cover.svg/2000px-Watchmen-cover.svg.png",
                    "https://www.youtube.com/watch?v=PVjA0y78_EQ")

logan = media.Movie("Logan",
                  "http://cdn2-www.comingsoon.net/assets/uploads"+
                  "/gallery/untitled-wolverine-sequel/loganposter2.jpg",
                  "https://www.youtube.com/watch?v=gbug3zTm3Ws")

spirited_away = media.Movie("Spirited Away",
                      "http://covers.box.sk/newsimg/dvdmov"+
                      "/max1133777176-front-cover.jpg",
                      "https://www.youtube.com/watch?v=ByXuk9QqQkk")

"""
Games init information
 'instance_name' = media.Games('game_name','cover_url','trailer_url')
"""  

the_last_of_us = media.Games("The last of us",
                    "https://upload.wikimedia.org/wikipedia/"+
                    "en/4/46/Video_Game_Cover_-_The_Last_of_Us.jpg",
                    "https://www.youtube.com/watch?v=OQWD5W3fpPM")

super_meat_boy = media.Games("super meat boy",
                      "https://upload.wikimedia.org/wikipedia"+
                      "/en/a/aa/SuperMeatBoy_cover.png",
                      "https://www.youtube.com/watch?v=snaionoxjos")   

the_last_guardian = media.Games("The last guardian",
                        "https://static.raru.co.za/cover/"+
                        "2016/07/06/4836926-l.jpg?v=1467791908",
                        "https://www.youtube.com/watch?v=Kew-LgiyfN4" )    

overwatch = media.Games("Overwatch",
              "http://www.posterparty.com/images/fp4276.jpg",
              "https://www.youtube.com/watch?v=IBIwGKDwnWY" )    

#Create list of trailers
movies = [donnie_darko, lala_land, watchmen, logan, spirited_away]
games = [the_last_of_us, super_meat_boy, the_last_guardian, overwatch]

#send the lists to the library
game_tomatoes.open_movies_page(games)
fresh_tomatoes.open_movies_page(movies)


