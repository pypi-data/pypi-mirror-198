"""
Test number normaliser
"""
from techiaith.tts.testun.date_norm import expand_date_welsh

tests = [
    ["1/1/2020", "cyntaf o Ionawr dau mil dau ddeg"],
    ["02/2/2023", "ail o Chwefror dau mil dau ddeg tri"],
    ["3/03/2021", "trydydd o Fawrth dau mil dau ddeg un"],
    ["04/04/2021", "pedwerydd o Ebrill dau mil dau ddeg un"],
    ["5/5/1995", "pumed o Mai mil naw cant naw deg pump"],
    ["15/06/2021", "pymthegfed o Fehefin dau mil dau ddeg un"],
    ["31/7/2000", "unfed ar ddeg ar hugain o Orffennaf dau mil"],
    ["25/8/2010", "pumed ar hugain o Awst dau mil un deg"],
    ["6/9/1999", "chweched o Fedi mil naw cant naw deg naw"],
    ["01/10/1920", "cyntaf o Hydref mil naw cant dau ddeg"],
    ["9/11/2024", "nawfed o Dachwedd dau mil dau ddeg pedwar"],
    ["21/12/2024", "unfed ar hugain o Ragfyr dau mil dau ddeg pedwar"],
]


def test_date():
    for date in tests:
        result = expand_date_welsh(date[0])
        assert result == date[1]
