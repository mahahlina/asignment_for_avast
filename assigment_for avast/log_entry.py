import datetime


class LogEntry:
    def __init__(self, timestamp, logger_name, severity, message):
        self.timestamp = datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S,%f')
        self.severity = severity
        self.logger_name = logger_name
        self.message = message

    def __str__(self):
        return str(self.timestamp) + " " + str(self.severity) + " " + self.logger_name + " " + self.message








