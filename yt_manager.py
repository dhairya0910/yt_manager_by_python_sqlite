import sqlite3
con = sqlite3.connect("yt_manager.db")
cursor=con.cursor()

cursor.execute('''
 CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
               )             
''')
# Triple string k andr jo bhi value dete hai unki formatting same rehti hai mtlb jo dete hai wai jaati hai!!


def list_all_videos():
    cursor.execute("SELECT * FROM VIDEOS")# Isse hmaare pass ek tuple return aaega
    for row in cursor.fetchall():
        print(row)


   
def add_video(name,time):
   
    cursor.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    con.commit()

def update_video(new_name, new_time, video_id):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE id =?",(new_name, new_time, video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,)) # Isme ek comma dena hii hota hai tbhi ye tuple mein jaaega
    con.commit()



def exit_app():
    pass



def main():
    while True :
        print("Youtube Manager App| Choose One among options which are getting printed")
        print("1.List all youtube videos")
        print("2. Add a Youtube Video")
        print("3. Update a youtube video Details")
        print("4.Delete A Youtube Video")
        print("5. Exit this bullshit App")
        choice = input("Enter ur choice: ")
        print()

        # NEW SYNTAX ALERT
        match choice:
            case "1":
                list_all_videos()
            
            case "2":
                name=input("Enter the video name: ")
                time=input("Enter the video time: ")
                add_video(name,time)

            case "3":
                video_id=int(input("Enter video Id: "))
                new_name=input("Enter the video name: ")
                new_time=input("Enter the video time: ")
                update_video(new_name, new_time, video_id)

            case "4":
                video_id=int(input("Enter video Id: "))
                delete_video(video_id)

            case "5":
                break
            case _:
                print("Invalid Response")
    
    con.close()

     

if __name__== "__main__":
  main()
