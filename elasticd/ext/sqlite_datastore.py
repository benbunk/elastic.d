__author__ = 'patelm'

import logging

from elasticd.datastore import Datastore


class SqliteDatastore(Datastore):

    def __init__(self, config):
        Datastore.__init__(self, config)
        logging.debug('sqlite datasource started')

    def add_backend(self):
        Datastore.add_backend(self)

