import schedule
import time
import webbrowser

def open_link(link):
    webbrowser.open(link)

def intro2python():
    webbrowser.open("https://dfa.zoom.us/j/96815350328")

def elvis_room():
    webbrowser.open()
# schedule.every().monday.at("10:30").do(intro2python)
# schedule.every().tuesday.at("14:05").do(intro2python)
# schedule.every().wednesday.at("10:30").do(intro2python)
# schedule.every().thursday.at("10:33").do(intro2python)

while True:
    schedule.run_pending()
    print("Not yet...")
    time.sleep(30)