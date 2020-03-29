#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

CREATE_TWEETS_TABLE = '''
    CREATE TABLE IF NOT EXISTS tweets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        repo_url varchar(2048) NOT NULL,
        last_tweeted_on datetime NOT NULL);
'''

class SQLiteDao:

    connection = None
    cursor = None
    

    def prepare_db_connection(self, GOOD_FIRST_DB_COLLECTION):
        """ Creates a SQLite DB connection """

        self.connection = sqlite3.connect(GOOD_FIRST_DB_COLLECTION)
        return self.connection


    def create_tweets_table_if_not_exits(self):
        """ Creates a table if it doesn't exist """

        self.cursor.execute(CREATE_TWEETS_TABLE)


    def acquire_db_connection(self):
        """ Acquires a cursor from the connection """

        self.cursor = self.connection.cursor()
        return self.cursor
    
    def is_repo_tweeted(self, repo_url):
        """
        Returns True if the repo is tweeted.
        `fetchone()` method returns an object if select was successful
        """

        self.cursor.execute(
            "SELECT id FROM tweets WHERE repo_url = '%s'" % repo_url
        )
        return self.cursor.fetchone() is not None


    def insert_tweet(self, repo_url, current_timestamp):
        """ Inserts a tweet into the DB """

        self.cursor.execute(
            "INSERT INTO tweets (repo_url, last_tweeted_on) VALUES ('%s', '%s')"
            % (repo_url, current_timestamp)
        )
        self.connection.commit()
