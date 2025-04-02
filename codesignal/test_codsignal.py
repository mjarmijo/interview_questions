import codesignal as b

def test_sum_it():
    mylist = [1, 2, 3, 4]
    assert b.sum_it(mylist) == 10
    
    mylist = []
    assert b.sum_it(mylist) == None

def test_sum_and_max():
    mylist = [1, 2, 3, 4]
    assert b.sum_and_max(mylist) == (10, 4)

    mylist = []
    assert b.sum_and_max(mylist) == None

def test_count_occurences():
    mylist = [1, 2, 3, 2, 2, 4]
    assert b.count_occurences(mylist, 2) == 3

def test_reverse_string():
    val = "hello"
    assert b.reverse_string(val) == "olleh"

def test_is_palindrome():
    val = "hello"
    assert b.is_palindrome(val) == False

    val = "radar"
    assert b.is_palindrome(val) == True

    val = ""
    assert b.is_palindrome(val) == False

    val = "a"
    assert b.is_palindrome(val) == True


if __name__ == '__main__':
    # mylist = [1, 2, 3, 4]
    # mylist = []
    # print(b.sum_it(mylist))

    # # print(b.sum_and_max(mylist))
    # mylist = [1, 2, 3, 2, 2, 4]
    # print(b.count_occurences(mylist, 2))

    # val = "hello"
    # print(b.reverse_string(val))

    # val = "radar"
    # val = "mike"
    # val = "ada"
    # print(b.has_palindrome_substring(val))

    denominations = [1, 2, 5]
    amount = 5

    print(b.coin_change(denominations, amount))