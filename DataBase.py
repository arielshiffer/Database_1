"""
Author: Ariel Shiffer
Program name: DataBase
Description: This program builds
the initial dictionary
and contains functions that can add a
value to the dictionary,
get a value from the dictionary,
delete a value and get a description
of the dictionary status.
Date: 18.1.23
"""

# Imports

import logging


class DataBase:
    def __init__(self):
        """
        This function builds the initial dictionary
        and gives it no keys or values.
        :param: Self is the object.
        :return: Nothing.
        """
        self.dictionary = {}

    def set_value(self, key, value):
        """
        This function gets a key and a value and adds it to the
        dictionary.
        :param key: A string that we want to add to the
        dictionary as a key.
        :param value: A string that we want to add to the dictionary
        as a value to the key we got.
        :return: If the key and value-added
        successfully -> True if not -> False.
        """
        logging.debug('Adding key and value to the dictionary')
        self.dictionary[key] = value
        if self.dictionary[key] == value:
            return True
        logging.debug("Couldn't add the key and value")
        return False

    def get_value(self, key):
        """
        This function gets a key name and gets the
        value from the key.
        :param key: The name of the key we want to get
        the value from. String.
        :return: Returns the value from the certain key.
        String.
        """
        logging.debug('Getting a value from the dictionary')
        return self.dictionary.get(key)

    def delete_value(self, key):
        """
        This function gets a key name and gets
        the value from the key.
        Then deletes the key and value from the dictionary.
        :param key: The name of the key we want
        to get the value from and
        then remove from the dictionary. String.
        :return: Returns the value from the certain key.
        String.
        """
        logging.debug('Deleting a key from the dictionary and getting'
                      'The value of it')
        if key in list(self.dictionary.keys()):
            removed_value = self.dictionary.pop(key)
            return removed_value
        return None

    def __str__(self):
        """
        This function makes a description of the dictionary.
        :return: A String that resembles the status of the
        dictionary.
        """
        return 'The dictionary : {}'.format(self.dictionary)
