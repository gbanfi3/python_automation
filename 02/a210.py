movies_watched = {'The Matrix', "Green Book", "Her"}
user_movie = input("milyen filmet láttál mostanában?: ")

if user_movie in movies_watched:
    print(f"én is láttam a {user_movie} filmet")
else:
    print(f"én még nem láttam a {user_movie} filmet")