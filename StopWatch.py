import time
from datetime import datetime

def stopwatch():

    start_time = time.time()
    try:
        while True:
            elasped_time = int(time.time() - start_time)
            mins, secs = divmod(elasped_time,60)
            hours, mins = divmod(mins,60)
            timer = '{:02d}:{:02d}:{:02d}'.format(hours,mins,secs)
            current_date = datetime.now().strftime('%Y-%m-%d')
            print(f'{current_date} {timer}',end ='\r')
            time.sleep(1)
    except KeyboardInterrupt:
        print('\nStopwatch stopped')
    
def main():
    input('press Enter to start')
    print('Stopwatch Started.please enter clt+c to stop')
    stopwatch()

if __name__ == "__main__":
    main()
    
            