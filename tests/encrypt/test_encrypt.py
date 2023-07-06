from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # Test case 1: Valid input with odd key
    message = "Hello, World!"
    key = 3
    expected_output = "lroW_,olleH"
    assert encrypt_message(message, key) == expected_output, "Test case 1 fail"

    # Test case 2: Valid input with even key
    message = "Hello, World!"
    key = 6
    expected_output = "Wo,_lleHlrd"
    assert encrypt_message(message, key) == expected_output, "Test case 2 fail"

    # Test case 3: Invalid key type (not an integer)
    message = "Hello, World!"
    key = "invalid"
    try:
        encrypt_message(message, key)
        assert False, "Test case 3 failed"
    except TypeError:
        pass

    # Test case 4: Invalid message type (not a string)
    message = 12345
    key = 3
    try:
        encrypt_message(message, key)
        assert False, "Test case 4 failed"
    except TypeError:
        pass

    # Test case 5: Invalid key (out of range)
    message = "Hello, World!"
    key = 100
    expected_output = "!dlroW ,olleH"
    assert encrypt_message(message, key) == expected_output, "Test case 5 fail"

    # Test case 6: Empty message with odd key
    message = ""
    key = 5
    expected_output = ""
    assert encrypt_message(message, key) == expected_output, "Test case 6 fail"

    # Test case 7: Empty message with even key
    message = ""
    key = 4
    expected_output = ""
    assert encrypt_message(message, key) == expected_output, "Test case 7 fail"

    print("All test cases passed!")
