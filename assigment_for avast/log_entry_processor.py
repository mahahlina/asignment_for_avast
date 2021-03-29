import datetime
import os

from log_entry import LogEntry
from severity import Severity


class LogEntryProcessor:
    def __init__(self, log_file_name):
        self.log_file_name = log_file_name
        self.__log_list = []
        self.__is_parsed = False

    def parse(self):
        try:
            with open(self.log_file_name) as r:
                log_lines = r.read().splitlines()
                for line in log_lines:
                    columns = [col.strip() for col in line.split(' - ') if col]
                    try:
                        datetime.datetime.strptime(columns[0], '%Y-%m-%d %H:%M:%S,%f')
                        log_entry = LogEntry(columns[0], columns[1], Severity[columns[2]], columns[3])
                        self.__log_list.append(log_entry)
                    except ValueError:
                        self.__log_list[-1].message += os.linesep + str(columns[0])

            self.__is_parsed = True
        except Exception as x:
            print(x)

    def get_entries(self):
        if self.__is_parsed:
            print("Hi, good job")
            return self.__log_list
        else:
            raise Exception("Log file is not parsed yet")

    def get_entries_by_severity(self, severity):
        result = []
        for log in self.__log_list:
            if log.severity == severity:
                result.append(log)
        return result

    def get_entries_by_logger_name(self, logger_name):
        result = []
        for log in self.__log_list:
            if log.logger_name == logger_name:
                result.append(log)
        return result

    def get_entries_with_substring_in_message(self, substring):
        result = []
        for log in self.__log_list:
            if substring in log.message:
                result.append(log)
        return result

    def get_newer_entries(self, timestamp):
        result = []
        for log in self.__log_list:
            if log.timestamp > datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S,%f'):
                result.append(log)
        return result
