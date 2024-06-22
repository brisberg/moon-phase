import pytest
from moon import Phase, get_luminocity_on_day, get_phase_progress_on_day, get_phase_from_progression

def test_get_phase_progression_from_day():
    # First full moon in 2000 is 5:40 PM Jan, 21 UTC
    progression = get_phase_progress_on_day(2000, 1, 21)

    assert progression == 0.4781190275708537
    
def test_get_luminocity_from_day():
    # First full moon in 2000 is 5:40 PM Jan, 21 UTC
    luminocity = get_luminocity_on_day(2000, 1, 21)


    assert round(luminocity, 2) == 99.94

phase_from_progression_tests = [
    (0, Phase.NEW_MOON),
    (0.02, Phase.NEW_MOON),
    (0.03, Phase.WAXING_CRESCENT),
    (0.22, Phase.WAXING_CRESCENT),
    (0.23, Phase.FIRST_QUARTER),
    (0.27, Phase.FIRST_QUARTER),
    (0.28, Phase.WAXING_GIBBOUS),
    (0.47, Phase.WAXING_GIBBOUS),
    (0.48, Phase.FULL_MOON),
    (0.50, Phase.FULL_MOON),
    (0.52, Phase.FULL_MOON),
    (0.53, Phase.WANING_GIBBOUS),
    (0.72, Phase.WANING_GIBBOUS),
    (0.73, Phase.LAST_QUARTER),
    (0.77, Phase.LAST_QUARTER),
    (0.78, Phase.WANING_CRESCENT),
    (0.97, Phase.WANING_CRESCENT),
    (0.98, Phase.NEW_MOON)]

@pytest.mark.parametrize("progression,expected", phase_from_progression_tests)
def test_get_moon_phase(progression, expected):
    phase = get_phase_from_progression(progression)

    assert phase == expected