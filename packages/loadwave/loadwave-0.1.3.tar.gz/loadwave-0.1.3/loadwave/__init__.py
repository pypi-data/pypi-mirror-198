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
            self.progress += 1

    def progress_bar(self, bar_length=30):
        percent = int((self.progress / self.total_steps) * 100)
        filled = int(self.progress / self.total_steps * bar_length)
        empty = bar_length - filled
        filled_bar = Fore.RED + '-' * filled + Style.RESET_ALL
        empty_bar = Fore.LIGHTBLACK_EX + '-' * empty + Style.RESET_ALL
        return f"{filled_bar}{empty_bar}"
