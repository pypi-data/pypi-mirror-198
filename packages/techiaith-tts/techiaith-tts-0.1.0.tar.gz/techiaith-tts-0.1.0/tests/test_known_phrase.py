"""
Test known_phrases
"""
from techiaith.tts.testun.known_phrases import replace_phrase


def test_replace_phrase():
    expected = "mae golwg tri chwech ddim yn wefan"
    result = replace_phrase("mae golwg360 yn wefan")
    assert expected == result
