#!/usr/bin/env python3
"""
lists all documents in a mongodb collection:
"""

import pymongo

def list_all(mongo_collection):
    """ lists all documents """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
