"""
Author : Ariel Shiffer
Program name : Writing_Functions
Description : This program opens a file and puts information from the database
dictionary into it in pickle encryption and also gets information about the
database dictionary from the file.
Date : 18.1.23
"""

# Imports

from DataBase import *
from pickle import *
import os
import logging


class WritingFunctions(DataBase):
    def __init__(self, file_name):
        """
        This function creates the initial file and puts
        all the information from the data base into it.
        :param file_name: The name we want the file to be called at. String.
        """
        super().__init__()
        self.file = file_name
        if not os.path.isfile(self.file):
            with open(self.file, "wb") as file:
                dump(self.dictionary, file)

    def read_from_file(self):
        """
        This function decrypts all the information from the file and puts it in the data base dictionary.
        :return: If the file exists -> return the new dictionary after it
        updated from the information in the file. Dictionary.
        if the file didn't exist -> return None.
        """
        if os.path.isfile(self.file):
            logging.debug('Opening file to read from it')
            with open(self.file, "rb") as file:
                self.dictionary = load(file)
            return self.dictionary
        return None

    def write_to_file(self):
        """
        This function encrypts all the information from the
        dictionary and writes it to the file.
        :return: Nothing.
        """
        if os.path.isfile(self.file):
            logging.debug('Opening file to write to it')
            with open(self.file, "wb") as file:
                dump(self.dictionary, file)

    def set_value(self, key, value):
        """
        This function reads from the file and then updates
        the values of the dictionary, then writes to the file again.
        :param key: The name of the key we want to add to the dictionary. String.
        :param value: The value we want to put to the certain key.String.
        :return: If the key and value added successfully return True else return False.
        """
        self.read_from_file()
        flag = super().set_value(key, value)
        self.write_to_file()
        return flag

    def get_value(self, key):
        """
        This function reads from the file to update the
        database dict then gets the value of the inserted key from the dict.
        :param key: The key we want to get the value of from the dict.
        :return: The value of the inserted key. String.
        """
        self.read_from_file()
        return super().get_value(key)

    def delete_value(self, key):
        """
        This function reads the file to update the dictionary
        then gets the value from the inserted key and deletes
        the key and value from the data base dict.
        :param key: The key we want to get the value of and delete from the dict. String.
        :return: The value from the key we wanted to delete. String.
        """
        self.read_from_file()
        value = super().delete_value(key)
        self.write_to_file()
        return value
