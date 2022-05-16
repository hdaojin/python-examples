from pathlib import Path
import time
import platform
import winsound

# third party modules
# from playsound import playsound
from tqdm import tqdm


# base_dir = Path(__file__).resolve().parent 
# sound_file = base_dir / 'alarm.wav'

sound_file = 'alarm.wav'

def play_sound(sound_file):
    if platform.system() == 'Windows':
        winsound.PlaySound(sound_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
    if platform.system() == 'Linux':
        pass
    else:
        pass
# scale = 50

# def progress_bar(scale):
#     start = time.perf_counter()
#     for i in range(scale + 1):
#         a = "#" * i 
#         b = "_" * (scale - i)
#         c = (i/scale) * 100
#         dur = time.perf_counter() - start
#         print("\r{:3.0f}%[{}{}]{:.2f}s".format(c, a, b, dur), end="")
#         # \r用来在每次输出完成后，将光标移至行首，这样保证进度条始终在同一行输出，即在一行不断刷新的效果；{:^3.0f}，输出格式为居中，占3位，小数点后0位，浮点型数，对应输出的数为c；{}，对应输出的数为a；{}，对应输出的数为b；{:.2f}，输出有两位小数的浮点数，对应输出的数为dur；end=''，用来保证不换行，不加这句默认换行。
#         time.sleep(time_interval/scale)
#     print()

def progress_bar(scale):
    with tqdm(total=scale, desc="Alarm clock", unit="sec", unit_scale=True, leave=True) as pbar:
        for i in range(1, scale + 1):
            # pbar.set_description(str(i))
            time.sleep(1)
            pbar.update(1)


time_interval = int(input("Enter time interval in seconds: "))
alarm_count = 0

while True:
    alarm_count += 1
    time_now = time.localtime()
    time_next = time.localtime(time.time() + time_interval)
    print(f"{alarm_count} times to alarm.")
    print("The current time is:   ", time.strftime("%Y-%m-%d %H:%M:%S", time_now))
    print("The next alarm time is:", time.strftime("%Y-%m-%d %H:%M:%S", time_next))
    # time.sleep(time_interval)
    progress_bar(time_interval)
    play_sound(sound_file)
