import datetime
import ephem
from typing import List, Tuple
from enum import Enum

Phase = Enum('Phase', [
  'NEW_MOON', 'WAXING_CRESCENT', 'FIRST_QUARTER', 'WAXING_GIBBOUS',
  'FULL_MOON', 'WANING_GIBBOUS', 'LAST_QUARTER', 'WANING_CRESCENT'])

def get_phase_progress_on_day(year: int, month: int, day: int):
  """Returns a floating-point number from 0-1. where 0=new, 0.5=full, 1=new"""
  #Ephem stores its date numbers as floating points, which the following uses
  #to conveniently extract the percent time between one new moon and the next
  #This corresponds (somewhat roughly) to the phase of the moon.

  #Use Year, Month, Day as arguments
  date = ephem.Date(datetime.date(year,month,day))

  nnm = ephem.next_new_moon(date)
  pnm = ephem.previous_new_moon(date)

  progression = (date-pnm)/(nnm-pnm)

  #Note that there is a ephem.Moon().phase() command, but this returns the
  #percentage of the moon which is illuminated. This is not really what we want.

  return progression

def get_luminocity_on_day(year: int, month: int, day: int):
  """Returns a floating-point number for the percentage of the moon illuminated"""

  #Use Year, Month, Day as arguments
  date = ephem.Date(datetime.date(year,month,day))
  moon = ephem.Moon()
  moon.compute(date)
  luminocity = moon.phase

  return luminocity

def get_phase_from_progression(progression):
  """Returns a Phase Enum given a moon progression (float from 0-1 with 0.5 being Full Moon)."""
  if progression <= 0.02:
    return Phase.NEW_MOON
  elif progression < 0.23:
    return Phase.WAXING_CRESCENT
  elif progression <= 0.27:
    return Phase.FIRST_QUARTER
  elif progression < 0.48:
    return Phase.WAXING_GIBBOUS
  elif progression <= 0.52:
    return Phase.FULL_MOON
  elif progression < 0.73:
    return Phase.WANING_GIBBOUS
  elif progression <= 0.77:
    return Phase.LAST_QUARTER
  elif progression < 0.98:
    return Phase.WANING_CRESCENT
  else:
    return Phase.NEW_MOON