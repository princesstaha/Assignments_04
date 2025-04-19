import time
import sys

def countdown_timer(minutes, seconds):
    total_seconds = minutes * 60 + seconds
    while total_seconds:
        mins, secs = divmod(total_seconds, 60)
        timer_format = '{:02d}:{:02d}'.format(mins, secs)
        # Print on the same line
        sys.stdout.write('\r' + timer_format)
        sys.stdout.flush()
        time.sleep(1)
        total_seconds -= 1
    sys.stdout.write('\rTime is up!\n')

if __name__ == '__main__':
    try:
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        if minutes < 0 or seconds < 0:
            print("Please enter non-negative values.")
        elif minutes == 0 and seconds == 0:
            print("Please enter a time greater than 0.")
        else:
            countdown_timer(minutes, seconds)
    except ValueError:
        print("Please enter valid numbers for minutes and seconds.")