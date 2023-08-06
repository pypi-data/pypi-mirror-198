"""
Test time normalisation
"""
from techiaith.tts.testun.time_norm import expand_time_welsh

tests = [
    ["12:30yh", "hanner awr wedi hanner dydd"],
    ["08:30", "hanner awr wedi wyth y bore"],
    ["20:30", "hanner awr wedi wyth yr hwyr"],
    ["16:01", "un munud wedi pedwar yr hwyr"],
    ["04:01 yb", "un munud wedi pedwar y bore"],
    ["5:15 yb", "chwater awr wedi pump y bore"],
    ["4:45 yh", "chwater awr i bump yr hwyr"],
    ["16:22", "dau funud ar hugain wedi pedwar yr hwyr"],
    ["16:34", "chwe munud ar hugain i bump yr hwyr"],
    ["Dwi'n mynd adra cyn 12:00", "Dwi'n mynd adra cyn hanner dydd"],
    ["Dwi'n mynd adra cyn 00:00", "Dwi'n mynd adra cyn hanner nos"],
    ["Dwi'n mynd adra cyn 12", "Dwi'n mynd adra cyn 12"],
]


def test_time():
    for time in tests:
        result = expand_time_welsh(time[0])
        assert result == time[1]
