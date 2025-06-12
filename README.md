# 📺 YouTube Video Manager App

A simple Python + SQLite command-line app to manage YouTube video entries — add, update, delete, and view videos.

---

## 🔧 Features

- 📋 List all YouTube videos
- ➕ Add a new video (title and time)
- ✏️ Update video details
- ❌ Delete a video by ID
- 💾 Data stored in a local SQLite database (`yt_manager.db`)

---

## 🗂 Project Files

yt_video_manager/
├── yt_manager.py # Main Python script
├── yt_manager.db # SQLite database file (auto-created)
└── README.md # Project documentation

---

## ▶️ How to Run

1. Make sure Python is installed on your system.  
   [Download Python here](https://www.python.org/downloads/)

2. Run the script:

```bash
python yt_manager.py
Choose from the options displayed in the terminal.

📋 Menu Preview
mathematica
Copy
Edit
YouTube Manager App
1. List all YouTube videos
2. Add a YouTube Video
3. Update a YouTube Video
4. Delete a YouTube Video
5. Exit App
Enter your choice:
🛠 Database Structure
The videos table has the following structure:

Column	Type	Description
id	INTEGER	Primary Key (auto-increment)
name	TEXT	Video title
time	TEXT	Video duration or time

📌 Notes
The database is created automatically on the first run.

You must enter the correct video ID to update or delete a record.

👨‍💻 Author
Made with 💻 by Dhairya Gupta

📄 License
Free to use for learning and personal projects.
