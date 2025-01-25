import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\n""Made it out alive, but I think I lost it", 0.05),
        ("Said that I was fine, I said it from the coffin", 0.045),
        ("Remember how I died when you started walkin'?", 0.045),
        ("That's my life, that's my life", 0.06),
        ("I'll put up a fight, taking out my earrings", 0.05),
        ("Don't you know the vibe? Don't you know the feeling?", 0.04),
        ("You should spend the night, catch me on your ceiling", 0.04),
        ("That's your prize, that's your prize", 0.06),
        ("Well Hmmmmmmmmmmmm""\n", 0.12),
    ]
    delays = [0.2, 2.5, 4.2, 6.8, 8.7, 10.9, 12.9, 14.4, 17.9]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
