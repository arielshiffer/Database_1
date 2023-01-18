"""
Author : Ariel Shiffer
Program name : process_check
Description : This program is checking different situation
and overloading the data base with processes.
Date : 18.1.23
"""
# Imports

from multiprocessing import *
import logging
from synchronization import Syncronazation
import Writing_Functions

# Consts

LOG_FILE_NAME = 'process_check.log'
CHECK_FILE_NAME = 'process_pickle_checker.bin'


def main():
    """
    This function simulates different types of
    situations and overloading the database.
    :return:Nothing.
    """
    ps = []
    db = Writing_Functions.WritingFunctions(CHECK_FILE_NAME)
    s = Syncronazation(db, False)
    logging.debug("checking simple writing")
    writing_check(s, 1)
    logging.debug("The check has been completed \r\n")

    logging.debug("checking simple reading")
    reading_check(s, 1)
    logging.debug("The check has been completed \r\n")

    logging.debug("checking reading while writing")
    r = Process(target=reading_check, args=(s, 1))
    w = Process(target=writing_check, args=(s, 1))
    r.start()
    w.start()
    r.join()
    w.join()
    logging.debug("The check has been completed \r\n")

    logging.debug("checking writing while reading")
    w = Process(target=writing_check, args=(s, 1))
    r = Process(target=reading_check, args=(s, 1))
    w.start()
    r.start()
    w.join()
    r.join()
    logging.debug("The check has been completed \r\n")

    logging.debug("checking multiple options")
    for i in range(20):
        r = Process(target=reading_check, args=(s, i))
        r.start()
        ps.append(r)
    for i in range(10):
        w = Process(target=writing_check, args=(s, i))
        w.start()
        ps.append(w)
    for i in ps:
        i.join()
    logging.debug("The check has been completed")


def writing_check(list_of_processes, process_number):
    """
    This function overload the database and writes to it 1000 times.
    :param list_of_processes: A synchronization object.
    :param process_number: The number of process writing to the database.
    Just for logging use.
    :return: Nothing, just checks the functions, if there is an error it will pop up.
    """
    logging.debug('starting writing check. Process {}'.format(process_number))
    for i in range(1, 1000):
        assert list_of_processes.set_value(i, i)


def reading_check(list_of_processes, process_number):
    """
    This function overload the database and reads from it 1000 times.
    :param list_of_processes: A synchronization object.
    :param process_number: The number of thread reading from the database.
    Just for logging use.
    :return: Nothing, just checks the functions, if there is an error it will pop up.
    """
    logging.debug('starting reading check. Process {}'.format(process_number))
    for i in range(1, 1000):
        assert (i == list_of_processes.get_value(i))


if __name__ == '__main__':
    logging.basicConfig(filename=LOG_FILE_NAME, level=logging.DEBUG, format='%(asctime)s:%(message)s')
    main()
