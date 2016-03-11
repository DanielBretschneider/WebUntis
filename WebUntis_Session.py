#!/usr/bin/env python3

"""
__author__ = "Daniel Bretschneider"
__version__ = "1.0.1"
__email__ = "dani.bretschneider@gmail.com"
__status__ = "Finished"
"""

#
# This file specifies the interface to the webuntis database, which will be used everytime data will be requested.
#

import webuntis

# WebUntis Session Object

def open_session():
    """
    __init__(): opens up the webuntis session.
    :return:
    """
    session = webuntis.Session(
        username='htl3r',
        password='htl3r',
        server='https://urania.webuntis.com',
        school='htl3r',
        useragent='Webuntis Test'
    ).login()

    return session

def close_session(session):
    """
    close_session: closes the webuntis session, as the name says already.
    :return:
    """
    session.login()

