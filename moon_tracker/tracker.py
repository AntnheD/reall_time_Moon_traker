import ephem
from datetime import datetime

class MoonTracker:
    def __init__(self, longitude, latitude):
        self.observer = ephem.Observer()
        self.observer.lon = str(longitude)
        self.observer.lat = str(latitude)
        self.moon = ephem.Moon()

    def update_observer_date(self, date_time=None):
        if date_time is None:
            date_time = datetime.utcnow()
        self.observer.date = date_time

    def get_moon_info(self, date_time=None):
        self.update_observer_date(date_time)
        self.moon.compute(self.observer)
        
        moon_phase = self.moon.phase  # Percentage of the moon illuminated
        moon_alt = self.moon.alt  # Moon altitude
        moon_az = self.moon.az  # Moon azimuth
        
        return {
            'phase': moon_phase,
            'altitude': moon_alt,
            'azimuth': moon_az,
            'earth_distance': self.moon.earth_distance  # Distance from Earth
        }
