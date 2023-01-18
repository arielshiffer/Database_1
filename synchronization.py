"""
Author : Ariel Shiffer
Program name : synchronazation
Description : This program is dealing with the sync of the threads/ processes by using locks.
Date : 18.1.23
"""

# Imports

import threading
import multiprocessing
import logging


class Syncronazation:
    def __init__(self, data_base, mode):
        """
        This function gets the mode of the locke, if True -> threads else -> multiprocessing
        then build the matching set of locks.
        :param data_base: A data base object.
        :param mode: Bool. If True -> threads else -> multiprocessing.
        """
        super().__init__()
        self.mode = mode
        self.dictionary = data_base
        # mode = true -> threads, false -> multiprocessing
        if self.mode:
            self.writing_allowance = threading.Lock()
            self.reading_allowances = threading.Semaphore(10)
        else:
            self.writing_allowance = multiprocessing.Lock()
            self.reading_allowances = multiprocessing.Semaphore(10)

    def set_value(self, key, value):
        """
        This function gets the write lock and all the
        reading locks, then updates the dictionary then
        releasing all the locks.
        :param key: The name of key we want to insert. String.
        :param value: The value we want to insert to the key. String.
        :return: If the key and value added successfully -> True if not -> False.
        """
        logging.debug('Acquiring the writing lock')
        self.writing_allowance.acquire()
        logging.debug('Acquiring all the reading locks')
        for i in range(10):
            self.reading_allowances.acquire()
        result = self.dictionary.set_value(key, value)
        logging.debug('Releasing all the reading locks')
        for i in range(10):
            self.reading_allowances.release()
        logging.debug('Releasing the writing lock')
        self.writing_allowance.release()
        return result

    def get_value(self, key):
        """
        This function gets one reading lock, then
        gets the value from the certain key then release the lock.
        :param key: The key we want to get the value of. String.
        :return: The value of the certain key. String.
        """
        logging.debug('Acquiring a reading lock')
        self.reading_allowances.acquire()
        value = self.dictionary.get_value(key)
        logging.debug('Releasing a reading lock')
        self.reading_allowances.release()
        return value

    def delete_value(self, key):
        """
        This function gets the write lock and all the
        reading locks, then deletes the key and gets its
        value then release all the locks.
        :param key: The certain key we want to get the value of and then delete. String.
        :return: The value of the inserted key. String.
        """
        logging.debug('Acquiring the writing lock')
        self.writing_allowance.acquire()
        logging.debug('Acquiring all the reading locks')
        for i in range(10):
            self.reading_allowances.acquire()
        value = self.dictionary.delete_value(key)
        logging.debug('Releasing all the reading locks')
        for i in range(10):
            self.reading_allowances.release()
        logging.debug('Releasing the writing lock')
        self.writing_allowance.release()
        return value

    def __str__(self):
        """
        This function gets a reading lock then gets a
        description of the status of the database dict,
        then releases the lock.
        :return: The status of the database dict. String.
        """
        self.reading_allowances.acquire()
        result = self.dictionary.__str__()
        self.reading_allowances.release()
        return result

