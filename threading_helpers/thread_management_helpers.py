#!/usr/bin/env python3
"""
    Purpose:
        Helper Library for building, managing, starting, and stopping threads.
"""

# Python Library Imports
import logging
import threading

# Local Library Imports
from threading_helpers.thread_entrypoint import thread_entrypoint


###
# Building Threads
###


def build_thread(
    thread_name, thread_callable, callable_args=(), callable_kwargs={}, is_daemon=True
):
    """
    Purpose:
        Create the Thread object and pass it the required args
    Args:
        thread_name (String): Name of the Tread
        thread_callable (Python Callable): Callable to run in Thread (Will pass the
            callable to the entrypoint for more control through a kwarg)
        callable_args (Tuple): Tuple to pass Callable as args
        callable_kwargs (Dict): Dict to pass the Callables as Kwargs
        is_daemon (Boolean): daemon flag to set in threadable
    Return:
        thread_obj (threading.Thread Obj): The thread object created
    """
    logging.info(f"Building {thread_name} Thread")

    thread_obj = None
    try:
        thread_obj = threading.Thread(
            args=(thread_callable,) + callable_args,
            daemon=is_daemon,
            kwargs=callable_kwargs,
            name=thread_name,
            target=thread_entrypoint,
        )
    except Exception as err:
        logging.exception(f"Error Building {thread_name} Thread: {err}")
        raise err

    return thread_obj


###
# Starting Threads
###


def start_thread(thread_obj):
    """
    Purpose:
        Start the Thread Obj. If it is already running, raise an exception.
    Args:
        thread_obj (threading.Thread Obj): The thread object to start
    Return:
        N/A
    """
    logging.info(f"Starting {thread_obj.name} Thread")

    if thread_obj.isAlive():
        raise Exception(f"Cannot Start {thread_obj.name}, it is already alive")

    try:
        thread_obj.start()
    except Exception as err:
        logging.exception(f"Error Starting {thread_name} Thread: {err}")
        raise err


def start_all_threads(thread_objs):
    """
    Purpose:
        Start All Worker Threads Required By Script
    Args:
        thread_objs (List of Thread Objs): List of threads that need to be started
    Return:
        N/A
    """

    for thread_obj in thread_objs:
        start_thread(thread_obj)


###
# Joining/Completing/Stopping Threads
###


def wait_for_all_threads_to_complete(thread_objs, timeout=300):
    """
    Purpose:
        Wait for All Threads to Complete
    Args:
        thread_objs (List of Thread Objs): List of threads that need to be completed
            to move on
        timeout (Int): Number of seconds to give each thread to timeout
    Return:
        N/A
    """

    for thread_obj in thread_objs:
        logging.info(f"Waiting for Thread to Complete: {thread_obj.name}")
        try:
            thread_obj.join(timeout)
        except Exception as err:
            logging.info(f"Timeout Failure Waiting for {thread_obj.name}")
            raise err
        logging.info(f"Thread Complete: {thread_obj.name}")
