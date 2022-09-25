#!/usr/bin/env python3
""" Function that return all students sorted by average score
"""


def top_students(mongo_collection):
    """ mongo_collection will be the pymongo collection object
    """
    top_st = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_st
