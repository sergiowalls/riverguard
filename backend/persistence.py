import json
import sqlite3
from collections import OrderedDict

from flask import jsonify

TWEET_TABLE = 'tweets'


class Persistence:
    def __init__(self, path, log):
        self.path = path
        self.log = log

    def init_db(self):
        db_conn, db_client = self.create_connection()
        try:
            db_client.execute('CREATE TABLE IF NOT EXISTS ' + TWEET_TABLE + '''
                         (id INTEGER PRIMARY KEY,
                         tweet STRING NOT NULL
                         )''')
            db_conn.commit()
        except Exception as e:
            self.close_connection(db_conn)
            raise e
        self.close_connection(db_conn)

    def create_connection(self):
        try:
            db_conn = sqlite3.connect(self.path)
            db_client = db_conn.cursor()
            return db_conn, db_client
        except Exception as ex:
            self.log.error('Error connecting with the SQLite DB. Exception: ' + str(ex))
            raise ex

    def close_connection(self, db_conn):
        try:
            db_conn.close()
            return db_conn
        except Exception as ex:
            self.log.error('Error closing the connection with the SQLite DB. Exception: ' + str(ex))
            raise ex

    def create(self, tweet):
        sql_script = 'INSERT OR REPLACE INTO ' + TWEET_TABLE + ' (id,tweet) VALUES (:id,:tweet)'
        db_conn, db_client = self.create_connection()
        try:
            cursor = db_conn.cursor()
            cursor.execute(sql_script, {'id': tweet['id'], 'tweet': json.dumps(tweet)})
            db_conn.commit()
            self.close_connection(db_conn)
            return None
        except Exception as ex:
            self.log.error('Error executing a query in the SQLite DB. Exception: ' + str(ex))
            if db_conn:
                self.close_connection(db_conn)
            raise ex

    def get(self):
        sql_script = 'SELECT * FROM ' + TWEET_TABLE
        db_conn, db_client = self.create_connection()
        try:
            db_client.execute(sql_script)
            parking = db_client.fetchone()[0]
            self.close_connection(db_conn)
            return parking
        except Exception as ex:
            self.log.error('Error executing a query in the SQLite DB. Exception: ' + str(ex))
            if db_conn:
                self.close_connection(db_conn)
            raise ex

    def delete(self, tweet_id):
        sql_script = 'DELETE FROM ' + TWEET_TABLE + ' WHERE id = :id'
        db_conn, db_client = self.create_connection()
        try:
            db_client.execute(sql_script, {'id': tweet_id})
            db_conn.commit()
            self.close_connection(db_conn)
        except Exception as ex:
            self.log.error('Error executing a query in the SQLite DB. Exception: ' + str(ex))
            if db_conn:
                self.close_connection(db_conn)
            raise ex

    def list(self):
        sql_script = 'SELECT * FROM ' + TWEET_TABLE
        db_conn, db_client = self.create_connection()
        try:
            db_client.execute(sql_script)
            keys = [description[0] for description in db_client.description]
            rows = db_client.fetchall()
            parking_list = []
            for row in rows:
                parking_row = OrderedDict(zip(keys, row))
                parking_row['tweet'] = json.loads(parking_row['tweet'], object_pairs_hook=OrderedDict)
                parking_list.append(parking_row)
            self.close_connection(db_conn)
            return parking_list
        except Exception as ex:
            self.log.error('Error executing a query in the SQLite DB. Exception: ' + str(ex))
            if db_conn:
                self.close_connection(db_conn)
            raise ex
