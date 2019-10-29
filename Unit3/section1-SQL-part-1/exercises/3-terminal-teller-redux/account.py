import sqlite3
import os

# CRUD with Object Orientation

DEFAULTDB = os.path.join(os.path.dirname(__file__), "accounts.db")

class Account:

    dbpath = DEFAULTDB

    @classmethod
    def setdb(cls, path):
        dbpath = path

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.account_num = kwargs.get('account_num')
        # etc.

    def save(self):
    """ Insert a new row into the database if id is not set, update the
    row with that id if it is set """
        if self.id is not None:
            self._insert()
        else:
            self._update()

    def _insert(self):
        """ open a database connection, insert a row into the database
        with self's properties for field values. Update self.id with the
        lastrowid after the insert operation. """
        pass

    def _update(self):
        """ update the row with id=self.id with the current properties """
        pass

    def deposit(self):
        """ add money, then call self.save() """
        pass

    def withdraw(self):
        """ remove money. raise a new exception called InsufficientFundsError if not
        enough money exists. call self.save() """

    @classmethod
    def from_id(cls, id):
        """ return a new Account object with values from the row with the given id
        if that row exists, return None otherwise """
        pass

    @classmethod
    def from_account_num(cls, account_num):
        """ return a new Account object with valus from the row with that number. return none if no such account """
        pass

    @classmethod
    def login(cls, account_num, pin):
        """ return a new Account object with values from the row with the values
        from the row with the given account_num and pin, if that row exists """
        pass

    def delete(self):
        """ delete the row with id=self.id, set self.id to None """
        pass 
