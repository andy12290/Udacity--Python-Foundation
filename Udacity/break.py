import time
import webbrowser


# This is module to open the web browser after 10 sec. time break
i=1

while i < 4:
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    i += 1
