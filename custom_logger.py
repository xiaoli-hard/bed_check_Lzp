# custom_logger.py
import logging
from datetime import datetime

class CustomLogger:
    def __init__(self):
        self.logs = []

    def log(self, level, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} [{level}] {message}"
        self.logs.append(log_entry)
        print(log_entry)  # 可选：打印到控制台

    def get_logs(self):
        return self.logs

    def clear_logs(self):
        self.logs.clear()
