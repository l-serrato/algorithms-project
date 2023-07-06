from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # Test case 1: Valid input with odd key
    message = "Hello"
    key = 3
    expected_output = "lroHe"
    assert (
        encrypt_message(message, key) == expected_output
    ), "Test case 1 failed"

    # Test case 2: Valid input with even key
    message = "Hello"
    key = 2
    expected_output = "olleH"
    assert (
        encrypt_message(message, key) == expected_output
    ), "Test case 2 failed"

    # Test case 3: Invalid key type (not an integer)
    message = "Hello"
    key = "invalid"
    try:
        encrypt_message(message, key)
        assert False, "Test case 3 failed"
    except TypeError:
        pass

    print("All test cases passed!")


# Run the test function
test_encrypt_message()
