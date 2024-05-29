import curses
from moon_tracker.tracker import MoonTracker
from moon_tracker.animator import MoonAnimator

if __name__ == "__main__":
    print("Starting Moon Tracker...")  # Add this line for debugging
    longitude = 37.7749  # Longitude for San Francisco
    latitude = -122.4194  # Latitude for San Francisco

    tracker = MoonTracker(longitude, latitude)
    animator = MoonAnimator(tracker)
    
    curses.wrapper(animator.draw_moon)
