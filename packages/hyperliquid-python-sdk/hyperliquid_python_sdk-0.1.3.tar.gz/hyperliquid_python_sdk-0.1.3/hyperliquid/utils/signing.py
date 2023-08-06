import struct
import sys

from eth_abi import encode
from eth_account.messages import encode_structured_data
from eth_utils import keccak

ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"


def order_type_to_array(order_type):
    if "limit" in order_type:
        tif = order_type["limit"]["tif"]
        if tif == "Gtc":
            return [2, 0]
        elif tif == "Alo":
            return [1, 0]
        elif tif == "Ioc":
            return [3, 0]
    elif "trigger" in order_type:
        trigger = order_type["trigger"]
        trigger_px = trigger["triggerPx"]
        if trigger["isMarket"] and trigger["tpsl"] == "tp":
            return [4, trigger_px]
        elif not trigger["isMarket"] and trigger["tpsl"] == "tp":
            return [5, trigger_px]
        elif trigger["isMarket"] and trigger["tpsl"] == "sl":
            return [6, trigger_px]
        elif not trigger["isMarket"] and trigger["tpsl"] == "sl":
            return [7, trigger_px]


def order_grouping_to_number(grouping):
    if grouping == "na":
        return 0
    elif grouping == "normalTpsl":
        return 1
    elif grouping == "positionTpsl":
        return 2


def double_to_byte_array(d):
    arr = bytearray(struct.pack("<d", d))
    if sys.byteorder == "little":
        arr.reverse()

    return arr


def order_spec_pre_processing(order_spec):
    decoded_order = order_spec["decodedOrder"]
    order_type_array = order_type_to_array(order_spec["orderType"])
    return (
        decoded_order["asset"],
        decoded_order["isBuyOrder"],
        double_to_byte_array(decoded_order["limitPx"]),
        double_to_byte_array(decoded_order["sz"]),
        decoded_order["isReduceOnly"],
        order_type_array[0],
        double_to_byte_array(order_type_array[1]),
    )


def construct_phantom_agent(signature_types, signature_data):
    connection_id = encode(signature_types, signature_data)

    return {"source": "a", "connectionId": keccak(connection_id)}


def sign_l1_action(wallet, signature_types, signature_data, active_pool, nonce):
    signature_types.append("address")
    signature_types.append("uint64")
    if active_pool is None:
        signature_data.append(ZERO_ADDRESS)
    else:
        signature_data.append(active_pool)
    signature_data.append(nonce)

    phantom_agent = construct_phantom_agent(signature_types, signature_data)

    data = {
        "domain": {
            "chainId": 1337,
            "name": "Exchange",
            "verifyingContract": "0x0000000000000000000000000000000000000000",
            "version": "1",
        },
        "types": {
            "Agent": [
                {"name": "source", "type": "string"},
                {"name": "connectionId", "type": "bytes32"},
            ],
            "EIP712Domain": [
                {"name": "name", "type": "string"},
                {"name": "version", "type": "string"},
                {"name": "chainId", "type": "uint256"},
            ],
        },
        "primaryType": "Agent",
        "message": phantom_agent,
    }

    structured_data = encode_structured_data(data)
    signed = wallet.sign_message(structured_data)
    return signed
