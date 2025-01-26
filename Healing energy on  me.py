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
        ("\n""Healing energy on me", 0.11),
        ("Baby, all I really need's one thing", 0.08),
        ("Healing energy on me", 0.11),
        ("Baby, can you make a wish for me?", 0.06),
        ("Healing energy on me", 0.12),
        ("When it's 11:11, I need it", 0.12),

    ]
    delays = [0.2, 3.0, 6.6, 9.6, 12.9, 15.0]
    
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
