# Author:	Louis Holbrook <dev@holbrook.no> 0826EDA1702D1E87C6E2875121D2E7BB88C2A746
# SPDX-License-Identifier:	GPL-3.0-or-later
# File-version: 1
# Description: Python interface to abi and bin files for faucet contracts

# standard imports
import logging
import json
import os

# external imports
from chainlib.eth.tx import (
        TxFactory,
        TxFormat,
        )
from chainlib.eth.constant import ZERO_ADDRESS
from chainlib.eth.contract import (
        ABIContractEncoder,
        ABIContractDecoder,
        ABIContractType,
        abi_decode_single,
        )
from chainlib.jsonrpc import JSONRPCRequest
from hexathon import (
        add_0x,
        strip_0x,
        )

logg = logging.getLogger().getChild(__name__)

moddir = os.path.dirname(__file__)
datadir = os.path.join(moddir, 'data')


class Request:

    def __init__(self, sender, recipient, value, token):
        self.sender = sender
        self.recipient = recipient
        self.value = value
        self.token = token
        self.serial = 0
        self.yay = 0
        self.nay = 0
        self.result = 0


    @classmethod
    def create(cls, sender, recipient, value, token, *args):
        o = Request(sender, recipient, value, token)
        if len(args) > 0:
            o.serial = args[0]
            o.yay = args[1]
            o.nsy = args[2]
            o.result = args[3]
        return o


    def is_accepted(self):
        return self.result & 2 > 0


    def is_rejected(self):
        return self.result & 4 > 0


    def is_transferred(self):
        return self.result & 24 == 8


    def is_voting(self):
        return self.result & 7 == 1


    def is_executed(self):
        return self.result & 8 == 8


    def __str__(self):
        return "{} {} {} {}".format(self.sender, self.recipient, self.value, self.result)



class TransferAuthorization(TxFactory):

    __abi = None
    __bytecode = None


    def __init__(self, *args, **kwargs):
        super(TransferAuthorization, self).__init__(*args, **kwargs)


    def count(self, *args, **kwargs):
        return self.call_noarg('count', *args, **kwargs)


    def quorum_threshold(self, *args, **kwargs):
        return self.call_noarg('quorum', *args, **kwargs)


    def veto_threshold(self, *args, **kwargs):
        return self.call_noarg('vetoThreshold', *args, **kwargs)


    def signer_count(self, *args, **kwargs):
        return self.call_noarg('signerCount', *args, **kwargs)


    def last_serial(self, *args, **kwargs):
        return self.call_noarg('lastSerial', *args, **kwargs)


    def next_serial(self, *args, **kwargs):
        return self.call_noarg('nextSerial', *args, **kwargs)


    @staticmethod
    def abi():
        if TransferAuthorization.__abi == None:
            f = open(os.path.join(datadir, 'ERC20TransferAuthorization.json'), 'r')
            TransferAuthorization.__abi = json.load(f)
            f.close()
        return TransferAuthorization.__abi


    @staticmethod
    def bytecode():
        if TransferAuthorization.__bytecode == None:
            f = open(os.path.join(datadir, 'ERC20TransferAuthorization.bin'))
            TransferAuthorization.__bytecode = f.read()
            f.close()
        return TransferAuthorization.__bytecode


    @staticmethod
    def gas(code=None):
        return 2800000


    def __single_address_method(self, method, contract_address, sender_address, address, tx_format=TxFormat.JSONRPC):
        enc = ABIContractEncoder()
        enc.method(method)
        enc.typ(ABIContractType.ADDRESS)
        enc.address(address)
        data = enc.get()
        tx = self.template(sender_address, contract_address, use_nonce=True)
        tx = self.set_code(tx, data)
        tx = self.finalize(tx, tx_format)        
        return tx


    def add_writer(self, contract_address, sender_address, address, tx_format=TxFormat.JSONRPC):
        return self.__single_address_method('addWriter', contract_address, sender_address, address, tx_format)


    def delete_writer(self, contract_address, sender_address, address, tx_format=TxFormat.JSONRPC):
        return self.__single_address_method('deleteWriter', contract_address, sender_address, address, tx_format)


    def create_request(self, contract_address, sender_address, sender, recipient, token, value, tx_format=TxFormat.JSONRPC):
        enc = ABIContractEncoder()
        enc.method('createRequest')
        enc.typ(ABIContractType.ADDRESS)
        enc.typ(ABIContractType.ADDRESS)
        enc.typ(ABIContractType.ADDRESS)
        enc.typ(ABIContractType.UINT256)
        enc.address(sender)
        enc.address(recipient)
        enc.address(token)
        enc.uint256(value)
        data = enc.get()
        tx = self.template(sender_address, contract_address, use_nonce=True)
        tx = self.set_code(tx, data)
        tx = self.finalize(tx, tx_format)        
        return tx



    def set_thresholds(self, contract_address, sender_address, quorum_threshold, veto_threshold, tx_format=TxFormat.JSONRPC):
        enc = ABIContractEncoder()
        enc.method('setThresholds')
        enc.typ(ABIContractType.UINT32)
        enc.typ(ABIContractType.UINT32)
        enc.uintn(quorum_threshold, 32)
        enc.uintn(veto_threshold, 32)
        data = enc.get()
        tx = self.template(sender_address, contract_address, use_nonce=True)
        tx = self.set_code(tx, data)
        tx = self.finalize(tx, tx_format)        
        return tx


    def requests(self, contract_address, idx, sender_address=ZERO_ADDRESS, id_generator=None):
        j = JSONRPCRequest(id_generator)
        o = j.template()
        o['method'] = 'eth_call'
        enc = ABIContractEncoder()
        enc.method('requests')
        enc.typ(ABIContractType.UINT32)
        enc.uintn(idx, 32)
        data = add_0x(enc.get())
        tx = self.template(sender_address, contract_address)
        tx = self.set_code(tx, data)
        o['params'].append(self.normalize(tx))
        o['params'].append('latest')
        o = j.finalize(o)
        return o


    def yay(self, contract_address, sender_address, serial, tx_format=TxFormat.JSONRPC):
        enc = ABIContractEncoder()
        enc.method('yay')
        enc.typ(ABIContractType.UINT32)
        enc.uintn(serial, 32)
        data = enc.get()
        tx = self.template(sender_address, contract_address, use_nonce=True)
        tx = self.set_code(tx, data)
        tx = self.finalize(tx, tx_format)        
        return tx


    def nay(self, contract_address, sender_address, serial, tx_format=TxFormat.JSONRPC):
        enc = ABIContractEncoder()
        enc.method('nay')
        enc.typ(ABIContractType.UINT32)
        enc.uintn(serial, 32)
        data = enc.get()
        tx = self.template(sender_address, contract_address, use_nonce=True)
        tx = self.set_code(tx, data)
        tx = self.finalize(tx, tx_format)        
        return tx


    def constructor(self, sender_address):
        code = TransferAuthorization.bytecode()
        tx = self.template(sender_address, None, use_nonce=True)
        tx = self.set_code(tx, code)
        return self.build(tx)


    def writers(self, contract_address, signer_address, sender_address=ZERO_ADDRESS, id_generator=None):
        j = JSONRPCRequest(id_generator)
        o = j.template()
        o['method'] = 'eth_call'
        enc = ABIContractEncoder()
        enc.method('signers')
        enc.typ(ABIContractType.ADDRESS)
        enc.address(signer_address)
        data = add_0x(enc.get())
        tx = self.template(sender_address, contract_address)
        tx = self.set_code(tx, data)
        o['params'].append(self.normalize(tx))
        o['params'].append('latest')
        o = j.finalize(o)
        return o


    def check_result(self, contract_address, sender_address, serial, id_generator=None, tx_format=TxFormat.JSONRPC):
        enc = ABIContractEncoder()
        enc.method('checkResult')
        enc.typ(ABIContractType.UINT32)
        enc.uintn(serial, 32)
        data = enc.get()
        tx = self.template(sender_address, contract_address, use_nonce=True)
        tx = self.set_code(tx, data)
        tx = self.finalize(tx, tx_format)        
        return tx


    def execute_request(self, contract_address, sender_address, serial, id_generator=None, tx_format=TxFormat.JSONRPC):
        enc = ABIContractEncoder()
        enc.method('executeRequest')
        enc.typ(ABIContractType.UINT32)
        enc.uintn(serial, 32)
        data = enc.get()
        tx = self.template(sender_address, contract_address, use_nonce=True)
        tx = self.set_code(tx, data)
        tx = self.finalize(tx, tx_format)        
        return tx


    def is_writer(self, contract_address, signer_address, sender_address=ZERO_ADDRESS, id_generator=None):
        return self.writers(contract_address, signer_address, sender_address)


    @classmethod
    def parse_signers(self, v):
        return abi_decode_single(ABIContractType.BOOLEAN, v)


    @classmethod
    def parse_count(self, v):
        return abi_decode_single(ABIContractType.UINT32, v)


    @classmethod
    def parse_create_request_request(self, v):
        v = strip_0x(v)
        cursor = 0
        enc = ABIContractEncoder()
        enc.method('createRequest')
        enc.typ(ABIContractType.ADDRESS)
        enc.typ(ABIContractType.ADDRESS)
        enc.typ(ABIContractType.ADDRESS)
        enc.typ(ABIContractType.UINT256)
        r = enc.get()
        l = len(r)
        m = v[:l]
        if m != r:
            logg.error('method mismatch, expected {}, got {}'.format(r, m))
            raise RequestMismatchException(v)
        cursor += l

        dec = ABIContractDecoder()
        dec.typ(ABIContractType.ADDRESS)
        dec.typ(ABIContractType.ADDRESS)
        dec.typ(ABIContractType.ADDRESS)
        dec.typ(ABIContractType.UINT256)
        dec.val(v[cursor:cursor+64])
        cursor += 64
        dec.val(v[cursor:cursor+64])
        cursor += 64
        dec.val(v[cursor:cursor+64])
        cursor += 64
        dec.val(v[cursor:cursor+64])
        r = dec.decode()
        return r 


    @classmethod
    def parse_request(self, v):
        cursor = 0
        v = strip_0x(v)
        d = ABIContractDecoder()
        d.typ(ABIContractType.UINT256)
        d.typ(ABIContractType.ADDRESS)
        d.typ(ABIContractType.ADDRESS)
        d.typ(ABIContractType.ADDRESS)
        d.typ(ABIContractType.UINT32)
        d.typ(ABIContractType.UINT32)
        d.typ(ABIContractType.UINT32)
        d.typ(ABIContractType.UINT32)
        d.val(v[cursor:cursor+64])
        cursor += 64
        d.val(v[cursor:cursor+64])
        cursor += 64 
        d.val(v[cursor:cursor+64])
        cursor += 64 
        d.val(v[cursor:cursor+64])
        cursor += 64 
        d.val(v[cursor:cursor+64])
        cursor += 64
        d.val(v[cursor:cursor+64])
        cursor += 64
        d.val(v[cursor:cursor+64])
        cursor += 64
        d.val(v[cursor:cursor+64])
        cursor += 64
        r = d.decode()
        return Request.create(r[1], r[2], r[0], r[3], r[4], r[5], r[6], r[7])
