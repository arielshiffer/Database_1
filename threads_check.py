"""
Author : Ariel Shiffer
Program name : threads_check
Description : This program is
checking different situation
and overloading the data base with
threading.
Date : 18.1.23
"""

# Imports

from threading import *
import logging
from synchronization import \
    Syncronazation
import Writing_Functions

# Consts

LOG_FILE_NAME = 'thread_check.log'
CHECK_FILE_NAME = 'thread_pickle_checker.bin'


def main():
    """
    This function simulates different
    types of
    situations and overloading the
    database.
    :return:Nothing.
    """
    # writing without interrupting check
    threads = []
    db = Writing_Functions.\
        WritingFunctions(CHECK_FILE_NAME)
    s = Syncronazation(db, True)
    logging.debug("checking simple writing")
    writing_check(s, 1)
    logging.debug("The check has been completed "
                  "\r\n")

    logging.debug("checking simple reading")
    reading_check(s, 1)
    logging.debug("The check has been completed "
                  "\r\n")

    logging.debug("checking reading while writing")
    r = Thread(target=reading_check, args=(s, 1))
    w = Thread(target=writing_check, args=(s, 1))
    r.start()
    w.start()
    r.join()
    w.join()
    logging.debug("The check has been completed "
                  "\r\n")

    logging.debug("checking writing while reading")
    w = Thread(target=writing_check, args=(s, 1))
    r = Thread(target=reading_check, args=(s, 1))
    w.start()
    r.start()
    w.join()
    r.join()
    logging.debug("The check has been completed "
                  "\r\n")

    logging.debug("checking multiple options")
    for i in range(20):
        r = Thread(target=reading_check, args=(s, i))
        r.start()
        threads.append(r)
    for i in range(10):
        w = Thread(target=writing_check, args=(s, i))
        w.start()
        threads.append(w)
    for i in threads:
        i.join()
    logging.debug("The check has been completed")


def writing_check(list_of_threads, thread_number):
    """
    This function overload the database and writes
    to it 1000 times.
    :param list_of_threads: A synchronization object.
    :param thread_number: The number of thread writing
    to the database.
    Just for logging use.
    :return: Nothing, just checks the functions,
    if there is an error it will pop up.
    """
    logging.debug('starting writing check. Thread {}'
                  .format(thread_number))
    for i in range(1, 1000):
        assert list_of_threads.set_value(i, i)


def reading_check(list_of_threads, thread_number):
    """
    This function overload the database and reads
    from it 1000 times.
    :param list_of_threads: A synchronization object.
    :param thread_number: The number of thread reading
    from the database.
    Just for logging use.
    :return: Nothing, just checks the functions,
    if there is an error it will pop up.
    """
    logging.debug('starting reading check. Thread {}'
                  .format(thread_number))
    for i in range(1, 1000):
        assert (i == list_of_threads.get_value(i))


if __name__ == '__main__':
    logging.basicConfig(filename=LOG_FILE_NAME, level=logging.DEBUG,
                        format='%(asctime)s:%(message)s')
    main()
