# -*- coding: utf-8 -*-
import pymongo
from pymongo import connection
import datetime


def process_command(user_input, **kwargs):

    if 'mongo' not in kwargs or not kwargs['mongo']:
        return 'No database connection available.'
    else:
        db = kwargs['mongo'].kvstore

    if len(user_input) < 4:
        return 'Usage: Igor store <get|save|remove> <name> <value>'

    if user_input[2] == 'get':
        posts = db.posts
        post = posts.find_one({'name': user_input[3]})
        if post is not None:
            return 'Master, %s told me on %s that the value of %s is %s' % (post['added_by'], post['added'], user_input[3], post['value'])
        else:
            return 'Sorry master, I could not find a match in the library.'

    elif user_input[2] == 'remove':
        posts = db.posts
        post = posts.find_one({'name': user_input[3]})

        if post is not None:
            posts.remove({'name': post['name']})
            return 'I have removed the specified item from the library Master.'
        else:
            return 'Sorry master, I could not find a match in the library.'

    elif user_input[2] == 'save':
        if len(user_input) < 5:
            return 'Master you need to tell me the value of your item.'

        posts = db.posts
        post = posts.find_one({'name': user_input[3]})

        if post is None:
            new_pw = {
                'name': user_input[3],
                'value': user_input[4],
                'added_by': kwargs['author'],
                'added': datetime.datetime.now()
            }
            posts.save(new_pw)
        else:
            post['value'] = user_input[4]
            post['added_by'] = kwargs['author']
            post['added'] = datetime.datetime.now()
            posts.update({'name': post['name']}, post)

        return 'Ok master, I have stored this in the library.'