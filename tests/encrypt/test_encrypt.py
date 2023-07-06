from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    """ a"""

    # Even key
    assert encrypt_message("message", 4) == "ega_ssem"

    # Odd key
    assert encrypt_message("message", 3) == "sem_egas"

    # Invalid key
    assert encrypt_message("message", -2) == "egassem"

    # Incorrect input type
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(5, 3)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("trybe", 3.9)
