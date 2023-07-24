import pytest
from cipher import Cipher


@pytest.mark.parametrize(
    ('ascii_code', 'expected_key'),
    (
        (50, 1),
        (52, 1),
        (66, 2),
        (88, 2),
        (100, 3),
        (120, 3)
    ),
)
def test_should_return_key_for_non_edge_ascii_code_inside_range(ascii_code, expected_key):
    assert Cipher.get_range_key(ascii_code) == expected_key


def test_should_return_one_for_bottom_edge_ascii_value():
    ascii_code = 48
    expected_key = 1
    assert Cipher.get_range_key(ascii_code) == expected_key


def test_should_return_one_for_upper_edge_ascii_value():
    ascii_code = 57
    expected_key = 1
    assert Cipher.get_range_key(ascii_code) == expected_key


def test_should_return_two_for_bottom_edge_ascii_value():
    ascii_code = 65
    expected_key = 2
    assert Cipher.get_range_key(ascii_code) == expected_key


def test_should_return_two_for_upper_edge_ascii_value():
    ascii_code = 90
    expected_key = 2
    assert Cipher.get_range_key(ascii_code) == expected_key


def test_should_return_three_for_bottom_edge_ascii_value():
    ascii_code = 97
    expected_key = 3
    assert Cipher.get_range_key(ascii_code) == expected_key


def test_should_return_three_for_upper_edge_ascii_value():
    ascii_code = 122
    expected_key = 3
    assert Cipher.get_range_key(ascii_code) == expected_key


@pytest.mark.parametrize(
    ('char_ascii', 'range_len_key', 'shift', 'expected_ascii'),
    (
            (50, 1, 5, 55),
            (50, 1, 8, 48),
            (70, 2, 5, 75),
            (70, 2, 22, 66),
            (100, 3, 12, 112),
            (100, 3, 23, 97)
    ),
)
def test_should_return_shifted_ascii_for_non_edge_ascii_entry(char_ascii, range_len_key, shift, expected_ascii):
    cipher_obj = Cipher("example message", shift)
    assert cipher_obj.shift_char(char_ascii, range_len_key) == expected_ascii


@pytest.mark.parametrize(
    ('char_ascii', 'range_len_key', 'shift', 'expected_ascii'),
    (
            (48, 1, 0, 48),
            (48, 1, 2, 50),
            (57, 1, 1, 48),
            (65, 2, 0, 65),
            (65, 2, 2, 67),
            (90, 2, 1, 65),
            (97, 3, 0, 97),
            (97, 3, 2, 99),
            (122, 3, 1, 97)
    ),
)
def test_should_return_shifted_ascii_for_edge_ascii_entry(char_ascii, range_len_key, shift, expected_ascii):
    cipher_obj = Cipher("example message", shift)
    assert cipher_obj.shift_char(char_ascii, range_len_key) == expected_ascii


@pytest.mark.parametrize(
    ('msg', 'shift', 'expected_encrypted_msg'),
    (
            ('Aa Bb 90', 1, 'Bb Cc 01'),
            ('My message', 2, 'Oa oguucig')
    ),
)
def test_should_return_properly_encrypted_message_for_message_containing_spaces(msg, shift, expected_encrypted_msg):
    cypher_obj = Cipher(msg, shift)
    assert cypher_obj.encrypt_message() == expected_encrypted_msg


@pytest.mark.parametrize(
    ('msg', 'shift', 'expected_encrypted_msg'),
    (
            ('AaBb90', 1, 'BbCc01'),
            ('Mymessage', 2, 'Oaoguucig')
    ),
)
def test_should_return_properly_encrypted_message_for_message_not_containing_spaces(msg, shift, expected_encrypted_msg):
    cypher_obj = Cipher(msg, shift)
    assert cypher_obj.encrypt_message() == expected_encrypted_msg
