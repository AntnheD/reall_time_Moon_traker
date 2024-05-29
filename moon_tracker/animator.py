import curses
import time
from .tracker.py import MoonTracker

class MoonAnimator:
    def __init__(self, moon_tracker):
        self.moon_tracker = moon_tracker

    def draw_moon(self, stdscr):
        # Clear screen
        stdscr.clear()
        
        while True:
            moon_info = self.moon_tracker.get_moon_info()
            phase = moon_info['phase']
            phase_char = self.get_phase_char(phase)
            
            # Display moon phase and other information
            stdscr.addstr(2, 2, f"Moon Phase (percentage): {phase:.2f}")
            stdscr.addstr(3, 2, f"Moon Altitude (radians): {moon_info['altitude']:.2f}")
            stdscr.addstr(4, 2, f"Moon Azimuth (radians): {moon_info['azimuth']:.2f}")
            stdscr.addstr(5, 2, f"Moon Distance from Earth (AU): {moon_info['earth_distance']:.4f}")
            stdscr.addstr(7, 2, f"Moon Phase: {phase_char}")
            
            # Refresh screen
            stdscr.refresh()
            
            # Wait before updating
            time.sleep(1)
            stdscr.clear()

    def get_phase_char(self, phase):
        if phase == 0 or phase == 100:
            return "●"  # Full Moon
        elif phase < 25:
            return "◔"  # Waxing Crescent
        elif phase < 50:
            return "◑"  # First Quarter
        elif phase < 75:
            return "◕"  # Waxing Gibbous
        else:
            return "○"  # New Moon
