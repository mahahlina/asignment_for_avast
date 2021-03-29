from log_entry_processor import LogEntryProcessor
from severity import Severity

test = LogEntryProcessor("C:\sample.log")
test.parse()

list = test.get_entries()
list1 = test.get_entries_by_severity(Severity.INFO)
list2 = test.get_entries_with_substring_in_message("Execution")
list3 = test.get_entries_by_logger_name("mf")
list4 = test.get_newer_entries("2021-03-19 11:39:38,918")

for log_entry in list:
    print(log_entry)
