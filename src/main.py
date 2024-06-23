import ephem
from datetime import datetime
from moon.moon import get_phase_progress_on_day, get_phase_from_progression

def mainfunction():
    print('Welcome to Moon Phase!')

date = datetime.now()

print(get_phase_from_progression(get_phase_progress_on_day(date.year, date.month, date.day)))
print(f'Next Full Moon: {ephem.next_full_moon(date)}')