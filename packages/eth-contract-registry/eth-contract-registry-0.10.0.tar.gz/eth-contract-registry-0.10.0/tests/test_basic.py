# standard imports
import os

# external imports
import logging
import pytest
from chainlib.eth.tx import (
        receipt,
        transaction,
        )
from chainlib.connection import RPCConnection
from chainlib.eth.contract import (
        ABIContractEncoder,
        ABIContractType,
        abi_decode_single,
        )
from chainlib.eth.nonce import RPCNonceOracle
from chainlib.eth.address import to_checksum_address
from hexathon import (
        add_0x,
        strip_0x,
        )

# local imports
from eth_contract_registry import Registry
from eth_contract_registry.registry import ContractRegistry
from eth_contract_registry.encoding import from_identifier_hex
from eth_contract_registry.pytest.fixtures_registry import valid_identifiers

logg = logging.getLogger()

valid_identifiers += [
        'FooContract',
        ]

def test_set(
        default_chain_spec,
        registry,
        eth_accounts,
        eth_rpc,
        eth_signer,
        roles,
        ):
   
    addr_registry = to_checksum_address(os.urandom(20).hex())
    addr_foo = to_checksum_address(os.urandom(20).hex())
    bogus_hash = add_0x(os.urandom(32).hex())

    nonce_oracle = RPCNonceOracle(roles['CONTRACT_DEPLOYER'], eth_rpc)
    builder = ContractRegistry(default_chain_spec, signer=eth_signer, nonce_oracle=nonce_oracle)

    o = builder.address_of(registry, 'ContractRegistry', sender_address=eth_accounts[0])
    r = eth_rpc.do(o)
    r = abi_decode_single(ABIContractType.ADDRESS, r)
    assert r == strip_0x(registry)

    (tx_hash_hex, o) = builder.set(registry, roles['CONTRACT_DEPLOYER'], 'ContractRegistry', addr_registry)
    r = eth_rpc.do(o)
    o = receipt(r)
    rcpt = eth_rpc.do(o)
    assert rcpt['status'] == 0

    (tx_hash_hex, o) = builder.set(registry, roles['CONTRACT_DEPLOYER'], 'FooContract', addr_foo)
    r = eth_rpc.do(o)
    o = receipt(r)
    rcpt = eth_rpc.do(o)
    assert rcpt['status'] == 1

    builder = Registry(default_chain_spec)
    o = builder.address_of(registry, 'FooContract', sender_address=eth_accounts[0])
    r = eth_rpc.do(o)
    r = abi_decode_single(ABIContractType.ADDRESS, r)
    assert r == addr_foo

