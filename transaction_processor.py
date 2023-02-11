import sys
import json

from sawtooth_sdk.processor.core import TransactionProcessor
from sawtooth_sdk.processor.handler import TransactionHandler

from transaction_family import TransactionPayload, State, InvalidAction, \
    NAMESPACE, NAME, VERSION

import logging

logger = logging.getLogger(__name__)


class CustomTransactionHandler(TransactionHandler):

    @property
    def family_name(self):
        return NAME

    @property
    def family_versions(self):
        return [VERSION]

    @property
    def namespaces(self):
        return [NAMESPACE]

    # The argument transaction is an instance of the class Transaction that
    # is created from the protobuf definition. Also, context is an instance of
    # the class Context from the python SDK.
    def apply(self, transaction, context):
        logger.error("inside apply")
        header = transaction.header
        signer = header.signer_public_key

        transaction = TransactionPayload.from_bytes(transaction.payload)
        
        if transaction.datatype not in ['hash', 'tuple', 'record']:
            raise InvalidAction(transaction.datatype)
        
        state = State(context)
        val = json.dumps({transaction.datatype: transaction.value})
        state.insert(transaction.id, val)


def main():
    processor = TransactionProcessor(url=sys.argv[1])
    processor.add_handler(CustomTransactionHandler())
    processor.start()


if __name__ == '__main__':
    logging.basicConfig(filename='example.log',
                        level=logging.DEBUG)
    logger.setLevel(logging.INFO)
    logger.info("hello")
    main()
