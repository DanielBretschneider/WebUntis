#! /usr/bin/env python3
# coding: utf8

"""
__author__ = "Daniel Bretschneider"
__version__ = "1.0.1"
__email__ = "dani.bretschneider@gmail.com"
__status__ = "(More or less) Finished."
"""

#
# This program starts the sequence:
#   - looks up upon substitutions
#   - if one or more were found -> generate new DB
#   - send email to concerning teacher(s)
#

import WebUntis_Notification

def checkSubsitutions():
    """
    checkSubsitutions(): responsible for the tasks as defined above.
    """
    # does the first task
    WebUntis_Notification.check_for_changes()

    # generate the database, with the new information

checkSubsitutions()

