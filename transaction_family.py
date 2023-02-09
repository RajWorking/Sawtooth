import hashlib
import sys

import cbor2

NAME = 'custom'
NAMESPACE = hashlib.sha512(NAME.encode('utf-8')).hexdigest()[:6]
VERSION = '1.0'


def generate_address(key):
    return NAMESPACE + hashlib.sha512(str(key).encode('utf-8')).hexdigest()[
                       -64:]


class TransactionPayload:

    def __init__(self, payload):
        datatype, id, value = cbor2.loads(payload)
        self._datatype = datatype
        self._id = id
        self._value = value

    @property
    def datatype(self):
        return self._datatype

    @property
    def id(self):
        return self._id

    @property
    def value(self):
        return self._value

    @classmethod
    def from_bytes(cls, payload):
        return cls(payload)


class State:

    def __init__(self, context):
        self._context = context

    def insert(self, key, value):
        address = generate_address(key)
        self._context.set_state({address: bytes(value, 'utf-8')})

    # def fetch(self, key):
    #     address = generate_address(key)
    #     self._context.delete_state([address])


class InvalidAction(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return self._msg
