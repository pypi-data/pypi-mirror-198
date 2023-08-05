import sys
import threading
import time
from colorama import Fore, Style

class Loader:
    def __init__(self, message, total_steps):
        self.message = message
        self.total_steps = total_steps
        self.stop_flag = None
        self.loader_thread = None
        self.progress = 0

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
            sys.stdout.write(f"\r{self.message} [{progress_bar}]")
            sys.stdout.flush()
            time.sleep(0.1)

    def progress_bar(self, bar_length=30):
        percent = int((self.progress / self.total_steps) * 100)
        filled = int(self.progress / self.total_steps * bar_length)
        empty = bar_length - filled
        filled_bar = Fore.RED + '-' * filled + Style.RESET_ALL
        empty_bar = Fore.LIGHTBLACK_EX + '-' * empty + Style.RESET_ALL
        if self.progress == self.total_steps and filled < bar_length:
            filled_bar = Fore.RED + '-' * (filled - 1) + '/' + Style.RESET_ALL
        return f"{filled_bar}{empty_bar}"

def process(func):
    def wrapper(*args, **kwargs):
        loader = Loader("Loading...", total_steps=100)
        loader.start()
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            loader.stop()
            raise e
        else:
            loader.stop()
            return result
    return wrapper
