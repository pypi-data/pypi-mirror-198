import sys
import threading
import time
from colorama import Fore, Style

class Loader:
    def __init__(self, bar_length=30):
        self.stop_flag = None
        self.loader_thread = None
        self.progress = 0
        self.bar_length = bar_length

    def start(self):
        self.stop_flag = False
        self.loader_thread = threading.Thread(target=self.loader)
        self.loader_thread.start()

    def stop(self):
        self.stop_flag = True
        self.loader_thread.join()

    def loader(self):
        while not self.stop_flag:
            progress_bar = self.progress_bar()
            sys.stdout.write(f"\r[{progress_bar}]")
            sys.stdout.flush()
            if self.progress >= self.bar_length:
                break
            time.sleep(0.1)
            self.progress += 1

        if not self.stop_flag:
            self.animate()

    def progress_bar(self, bar_length=30):
        filled = int(self.progress / bar_length * bar_length)
        empty = bar_length - filled
        filled_bar = Fore.RED + '-' * filled + Style.RESET_ALL
        empty_bar = Fore.LIGHTBLACK_EX + '-' * empty + Style.RESET_ALL
        # Eğer bar dolarsa animasyon başlat
        if self.progress >= bar_length:
            animation = "/" if self.progress % 2 == 0 else "\\"
            progress_bar2 = f"{progress_bar[2:]}[{Fore.YELLOW}{animation}{Style.RESET_ALL}]"
            return progress_bar2
        else:
            progress_bar = f"{filled_bar}{empty_bar}"
            return progress_bar
        
        





    
class Process:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        loader = Loader()
        loader.start()
        result = self.func(*args, **kwargs)
        loader.stop()
        return result

def process(func):
    return Process(func)
