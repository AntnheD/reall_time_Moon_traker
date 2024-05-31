# File: moon_tracker/animator.py

import curses
import time
from .tracker import MoonTracker
from colorama import init, Fore, Back, Style
class MoonAnimator:
    def __init__(self, moon_tracker):
        self.moon_tracker = moon_tracker

    def draw_moon(self, stdscr):
        # Clear screen
        stdscr.clear()
        
        while True:
            moon_info = self.moon_tracker.get_moon_info()
            phase = moon_info['phase']
            phase_art = self.get_phase_art(phase)
            
            # Display moon phase and other information
            stdscr.addstr(2, 2, f"Moon Phase (percentage): {phase:.2f}")
            stdscr.addstr(3, 2, f"Moon Altitude (radians): {moon_info['altitude']:.2f}")
            stdscr.addstr(4, 2, f"Moon Azimuth (radians): {moon_info['azimuth']:.2f}")
            stdscr.addstr(5, 2, f"Moon Distance from Earth (AU): {moon_info['earth_distance']:.4f}")
            
            # Display moon phase art
            for i, line in enumerate(phase_art.split('\n')):
                stdscr.addstr(7 + i, 2, line)
            
            # Refresh screen
            stdscr.refresh()
            
            # Wait before updating
            time.sleep(1)
            stdscr.clear()

    def get_phase_art(self, phase):
        if phase == 0 or phase == 100:
            return """
     _..._
   .:::::::.
  :::::::::::
 ::::::::::::: 
 ::::::::::::: 
 ::::::::::::: 
  ::::::::::: 
   ':::::::' 
     ''''
"""
        elif phase < 25:
            return """
     _..._
   .::::: 
  ::::::  
 ::::::   
 ::::::   
  :::::: 
   ':::::
     ''''
"""
        elif phase < 50:
            return """
     _..._
   .:::::: 
  :::::::  
 :::::::   
 :::::::   
 :::::::  
  ::::::: 
   '::::: 
     '''  
"""
        elif phase < 75:
            return """
     _..._
   .:::::::.
  :::::::::::
 ::::::::::::: 
 ::::::::::::: 
 ::::::::::'. 
  ::::::::' 
   '::::::' 
     '''' 
"""
        else:
            return """
     _..._
   .:::::. 
  :::::::. 
 ::::::::. 
 ::::::::. 
 ::::::::. 
  :::::::. 
   ':::::' 
     ''''
"""

