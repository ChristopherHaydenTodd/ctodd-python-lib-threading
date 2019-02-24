#!/usr/bin/env python3
"""
    Purpose:
        Create Threaded Script

    Steps:
        -

    example script call:
        python3 create_threaded_script
"""

# Python Library Imports
import logging
import os
import sys
import time
from argparse import ArgumentParser

# Local Library Imports
from threading_helpers import thread_management_helpers


def main():
    """
    Purpose:
        Create a Threaded Script
    """

    execute_non_threaded()
    execute_threaded()


def execute_non_threaded():
    """
    Purpose:
        Example Non-Threaded
    """
    logging.info("Starting Creation of Non-Threaded Script")

    sleeping_function(sleep_time=1, num_iterations=5)
    sleeping_function(sleep_time=4, num_iterations=2)
    sleeping_function(sleep_time=3, num_iterations=3)
    sleeping_function(sleep_time=5, num_iterations=2)
    sleeping_function(sleep_time=2, num_iterations=6)

    logging.info("Creation of Non-Threaded Script Complete")


def execute_threaded():
    """
    Purpose:
        Example Threaded
    """
    logging.info("Starting Creation of Threaded Script")

    thread_1_obj = thread_management_helpers.build_thread(
        "Thread 1",
        sleeping_function,
        callable_kwargs={
            "sleep_time": 1,
            "num_iterations": 5,
        }
    )
    thread_2_obj = thread_management_helpers.build_thread(
        "Thread 2",
        sleeping_function,
        callable_kwargs={
            "sleep_time": 4,
            "num_iterations": 2,
        }
    )
    thread_3_obj = thread_management_helpers.build_thread(
        "Thread 3",
        sleeping_function,
        callable_kwargs={
            "sleep_time": 3,
            "num_iterations": 3,
        }
    )
    thread_4_obj = thread_management_helpers.build_thread(
        "Thread 4",
        sleeping_function,
        callable_kwargs={
            "sleep_time": 5,
            "num_iterations": 2,
        }
    )
    thread_5_obj = thread_management_helpers.build_thread(
        "Thread 5",
        sleeping_function,
        callable_kwargs={
            "sleep_time": 2,
            "num_iterations": 6,
        }
    )

    thread_objs = [
        thread_1_obj,
        thread_2_obj,
        thread_3_obj,
        thread_4_obj,
        thread_5_obj,
    ]

    thread_management_helpers.start_all_threads(thread_objs)
    thread_management_helpers.wait_for_all_threads_to_complete(thread_objs)

    logging.info("Creation of Threaded Script Complete")


###
# Funcions to Thread
###


def sleeping_function(sleep_time=5, num_iterations=5):
    """
    Purpose:
        Function will Print and Sleep
    Args:
        sleep_time (Int): Time to sleep in seconds each iteration
        num_iterations (Int): Number of times to interate and sleep
    Returns:
        N/A
    """

    for x in range(num_iterations):
        logging.info(f"In Iteration {x+1}; Sleeping for {sleep_time} seconds")
        time.sleep(sleep_time)


if __name__ == "__main__":

    log_level = logging.INFO
    logging.getLogger().setLevel(log_level)
    logging.basicConfig(
        stream=sys.stdout,
        level=log_level,
        format="[create_threaded_script] %(asctime)s %(levelname)s %(message)s",
        datefmt="%a, %d %b %Y %H:%M:%S"
    )

    try:
        main()
    except Exception as err:
        logging.exception(
            "{0} failed due to error: {1}".format(os.path.basename(__file__), err)
        )
        raise err
