import sys
import threading
import time
from colorama import Fore, Style

class Loader:
    def __init__(self, message, steps):
        self.message = message
        self.stop_flag = None
        self.loader_thread = None
        self.progress = 0
        self.steps = steps
        self.bar_length = 30

    def start(self):
        self.stop_flag = False
        self.loader_thread = threading.Thread(target=self.loader)
        self.loader_thread.start()

    def stop(self):
        self.stop_flag = True
        self.loader_thread.join()

    def loader(self):
        # calculate total number of steps
        total_steps = self.steps * 10

        while not self.stop_flag:
            progress_bar = self.progress_bar()
            sys.stdout.write(f"\r{self.message} [{progress_bar}]")
            sys.stdout.flush()
            time.sleep(0.1)
            self.progress += 1

            if self.progress >= total_steps:
                break

        # print full progress bar if completed before bar_length
        sys.stdout.write(f"\r{self.message} [{self.progress_bar()}]\n")
        sys.stdout.flush()

    def progress_bar(self):
        percent = int((self.progress / (self.steps * 10)) * 100)
        filled = int(self.progress / (self.steps * 10) * self.bar_length)
        empty = self.bar_length - filled
        filled_bar = Fore.RED + '-' * filled + Style.RESET_ALL
        empty_bar = Fore.LIGHTBLACK_EX + '-' * empty + Style.RESET_ALL
        return f"{filled_bar}{empty_bar}"
