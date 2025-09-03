import eyed3
import os

def generate_playlist(mood):
    mood_songs = {
        "happy": ["song1.mp3", "song2.mp3"],
        "sad": ["song3.mp3", "song4.mp3"],
        "chill": ["song5.mp3", "song6.mp3"]
    }
    playlist = mood_songs.get(mood, [])
    print("Your playlist for mood:", mood)
    for song in playlist:
        print(f"- {song}")

if __name__ == "__main__":
    mood = input("Enter your mood (happy, sad, chill): ").strip().lower()
    generate_playlist(mood)
