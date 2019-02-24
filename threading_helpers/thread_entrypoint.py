#!/usr/bin/env python3
"""
    Purpose:
        Entrypoint Function for Threads. This will wrap any created thread
        and allow for a simple way of logging execution, handling critical
        exceptions, and more.
"""

# Python Library Imports
import logging
import threading
import time


###
# Thread Entrypoint
###


def thread_entrypoint(thread_callable, *callable_args, **callable_kwargs):
    """
    Purpose:
        Act as a wrapper for threads to handle thread exceptions, signal handeling,
        etc.
    Args:
        thread_callable (Python Callable): Callable to run
        callable_args (Tuple): Tuple to pass Callable as args
        callable_kwargs (Dict): Dict to pass the Callables as Kwargs
    Return:
        N/A
    """

    current_thread_obj = threading.currentThread()

    func_start = time.time()
    try:
        thread_callable(*callable_args, **callable_kwargs)
    except Exception as err:
        logging.exception(f"Exception in {current_thread_obj.name}: {err}")
        raise err
    finally:
        execution_time = time.time() - func_start
        logging.info(
            f'Execution Time of {current_thread_obj.name}: {execution_time:.2f} Seconds'
        )
