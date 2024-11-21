import sqlite3

con = sqlite3.connect('twitter.db')

cur = con.cursor()
tweetsData = [
    (2, "bob", "Loving React so far!", 10, "4h"),
    (3, "charlie", "This is a great project for learning.", 3, "1d"),
    (4, "dave", "Anyone else excited for the new React features?", 12, "3d"),
    (5, "eve", "I love creating mock data. 😊", 8, "5d"),
    (6, "frank", "Trying out some cool CSS animations today!", 7, "6h"),
    (7, "grace", "JavaScript is tricky, but I'm getting the hang of it!", 15, "8h"),
    (8, "hannah", "Any tips for optimizing React apps?", 6, "12h"),
    (9, "ivan", "Finally nailed that bug in my code. Feels great!", 11, "1d"),
    (10, "julia", "React Hooks make life so much easier!", 20, "2d"),
    (11, "kevin", "Working on my first JavaScript game!", 9, "1h"),
    (12, "laura", "Frontend development is so rewarding.", 14, "1d"),
    (13, "mike", "Struggling a bit with Redux... any resources?", 5, "3d"),
    (14, "nina", "Exploring async functions in JavaScript.", 7, "4d"),
    (15, "owen", "Taking my coding skills to the next level!", 12, "5d")
]

cur.executemany("INSERT INTO tweet VALUES (?,?,?,?,?)", tweetsData)

con.commit()

