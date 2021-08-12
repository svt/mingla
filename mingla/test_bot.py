from . import bot


def test_split_users_tree_users_three_rooms_size():
    a = list(bot.split_users([1, 2, 3], 3))
    b = [[1, 2, 3]]
    assert a == b, "Split 3 users, room size 3"


def test_split_users_five_users_three_rooms_size():
    a = list(bot.split_users([1, 2, 3, 4, 5], 3))
    b = [[1, 2, 3], [4, 5]]
    assert a == b, "Split 5 users, room size 3"


def test_split_users_twelve_users_three_rooms_size():
    a = list(bot.split_users([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3))
    b = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    assert a == b, "Split 12 users, room size 3"


def test_split_users_twelve_users_three_rooms_size():
    a = list(bot.split_users([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 2))
    b = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
    assert a == b, "Split 12 users, room size 2"


def test_split_users_two_users_three_rooms_size():
    a = list(bot.split_users([1, 2], 3))
    b = [[1, 2]]
    assert a == b, "Split 2 users, room size 3"


def test_split_users_two_users_two_rooms_size():
    a = list(bot.split_users([1, 2], 2))
    b = [[1, 2]]
    assert a == b, "Split 2 users, room size 2"


def test_split_users_tree_users_two_rooms_size():
    a = list(bot.split_users([1, 2, 3], 2))
    b = [[1, 2, 3]]
    assert a == b, "Split 2 users, room size 2"


def test_split_users_four_users_tree_rooms_size():
    a = list(bot.split_users([1, 2, 3, 4], 3))
    b = [[1, 2, 3, 4]]
    assert a == b, "Split 4 users, room size 3"


def test_split_users_five_users_tree_rooms_size():
    a = list(bot.split_users([1, 2, 3, 4, 5], 3))
    b = [[1, 2, 3], [4, 5]]
    assert a == b, "Split 5 users, room size 3"


def test_split_users_six_users_tree_rooms_size():
    a = list(bot.split_users([1, 2, 3, 4, 5, 6], 3))
    b = [[1, 2, 3], [4, 5, 6]]
    assert a == b, "Split 6 users, room size 3"


def test_split_users_seven_users_tree_rooms_size():
    a = list(bot.split_users([1, 2, 3, 4, 5, 6, 7], 3))
    b = [[1, 2, 3], [4, 5, 6, 7]]
    assert a == b, "Split 7 users, room size 3"


def test_split_users_eight_users_tree_rooms_size():
    a = list(bot.split_users([1, 2, 3, 4, 5, 6, 7, 8], 3))
    b = [[1, 2, 3], [4, 5, 6], [7, 8]]
    assert a == b, "Split 8 users, room size 3"
