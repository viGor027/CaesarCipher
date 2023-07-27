from CaesarCipher.logic.constants import ASCII_RANGES, ASCII_RANGES_LENGTHS


class Cipher:
    """
    Class implements logic of message encrypting/decrypting
    """
    def __init__(self, message, shift):
        self.message = message
        self.shift = shift
        self.encrypted_message = self.encrypt_message()

    def encrypt_message(self) -> str:
        message_table = list(self.message)
        for letter_idx, letter in enumerate(message_table):
            if letter == " ":
                continue
            letter_ascii_code = ord(letter)
            if key := Cipher.get_range_key(letter_ascii_code):
                message_table[letter_idx] = chr(self.shift_char(letter_ascii_code, key))
            else:
                return ""
        message_table = "".join(message_table)
        return message_table

    @staticmethod
    def get_range_key(char_ascii: int) -> int:
        """
        gets: ascii code of a char
        returns: key to dictionary storing ranges in constants.py
        """
        for key in ASCII_RANGES:
            if ASCII_RANGES[key][0] <= char_ascii <= ASCII_RANGES[key][1]:
                return key
        return 0

    def shift_char(self, char_ascii: int, range_len_key: int) -> int:
        """
        :param char_ascii: ascii code of a char that we want to shift
        :param range_len_key: key to range including that ascii code from constants.py
        :return: ascii code for a shifted char
        """
        range_start_ascii = ASCII_RANGES[range_len_key][0]
        range_diff = char_ascii - range_start_ascii
        temp_shift = range_diff + self.shift
        normalized_shift = temp_shift % ASCII_RANGES_LENGTHS[range_len_key]
        result = range_start_ascii + normalized_shift
        return result
