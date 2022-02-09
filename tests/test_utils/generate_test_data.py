# coding=utf-8

import string
from framework.utils.string_data_generator import StringDataGenerator


class GenerateTestData(object):

    cyrillic_characters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    @staticmethod
    def generate_email(length: int) -> str:
        """
        Generate a random email for test of a given `length`.

        Raises:
            ValueError -- If `length` is lesser than 1.
        """
        if length < 1:
            raise ValueError("Email length should be at least 1")

        return StringDataGenerator.generate_random_string(
            length,
            string.ascii_lowercase,
        )

    @staticmethod
    def generate_domain(length: int) -> str:
        """
        Generate a random domain for test of a given `length`.

        Raises:
            ValueError -- If `length` is lesser than 1.
        """
        if length < 1:
            raise ValueError("Domain length should be at least 1")

        return StringDataGenerator.generate_random_string(
            length,
            string.ascii_lowercase,
        )

    def generate_password(self, length: int, email_character) -> str:
        """
        Generate a random password for MyDB of a given `length`.

        Raises:
            ValueError -- If `length` is lesser than 10.
        """
        if length < 10:
            raise ValueError("Password length should be at least 10")

        return StringDataGenerator.generate_random_string(
            length,
            string.ascii_uppercase,
            string.ascii_lowercase,
            string.digits,
            email_character,
            self.cyrillic_characters
        )
