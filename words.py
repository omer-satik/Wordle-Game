# WORD SET #

import csv


class Words:
    def __init__(self):
        self.file_path = "OPTED-Dictionary.csv"
        self.words_set = self.save_first_elements_to_set(self.file_path)

    def save_first_elements_to_set(self, file_path):
        first_elements_set = set()
        with open(file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                first_element = row[0].strip()
                first_elements_set.add(first_element)
        return first_elements_set
