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
        ("\n""Take me home, I'm fallin'", 0.11),
        ("Love me long I'm rollin'", 0.10),
        ("Losing control, body and soul", 0.11),
        ("Mind too for sure, I'm already yours", 0.11),
        ("\n""Take me home, I'm fallin'", 0.12),
        ("Love me long I'm rollin'", 0.11),
        ("Losing control, body and soul", 0.10),
        ("Mind too for sure, I'm already yours""\n", 0.09),
    ]
    delays = [0.2, 3.5, 6.6, 9.6, 13.6, 17.7, 21.4, 25.0]
    
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
