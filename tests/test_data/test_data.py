# coding=utf-8

from tests.test_utils.generate_test_data import GenerateTestData


class TestData(object):
    test_data_generator = GenerateTestData()

    email_size = 5
    password_size = 10
    domain_size = 5
    file_name = "avatar"
    file_extension = "png"
    first_card_num = "1"
    second_card_num = "2"
    third_card_num = "3"
    num_of_interests_checkboxes = 3
    timer_expected_time = "00:00:00"
