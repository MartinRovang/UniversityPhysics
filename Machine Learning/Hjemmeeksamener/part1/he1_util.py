import numpy as np
import binascii

def _text_to_bits(text, encoding='ascii', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def _text_from_bits(bits, encoding='ascii', errors='surrogatepass'):
    n = int(bits, 2)
    return _int2bytes(n).decode(encoding, errors)

def _int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def get_labels_for_msg(msg):
    """
    Convert message to label array. Reverse of "get_labels_for_msg".
    """
    st = _text_to_bits(msg)
    l = np.array([int(i) for i in st])
    return l

def get_msg_for_labels(l):
    """
    Convert a one-dimensional label array to a message-string.

    Args:
        l (1D array): Predicted (binary) labels which should be converted to a
                      message. The first eight elements are assumed to be the
                      8-bit ASCII representation of the first letter in the
                      message, the next eight elements are assumed to represent
                      the next letter, and so on. len(l) must be a multiple of 8
    Returns:
        msg (string): Decoded message.
    """
    st = "".join([str(i) for i in l])
    return _text_from_bits(st)
