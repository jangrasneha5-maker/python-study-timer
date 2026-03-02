import time
import os
import sys

def clear_screen():
    # Clears terminal: 'cls' for Windows, 'clear' for Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def study_timer():
    try:
        # Step 1: Ask for time
        print("--- AutoCAD Study Session Setup ---")
        val = input("Enter study duration in minutes (e.g., 25): ")
        minutes = float(val)
        seconds = int(minutes * 60)

        # Step 2: The Countdown Loop
        while seconds > 0:
            clear_screen()
            mins, secs = divmod(seconds, 60)
            timer_display = f"{mins:02d}:{secs:02d}"
            
            print("====================================")
            print(f"   CURRENT FOCUS: AutoCAD Practice  ")
            print("====================================")
            print(f"      TIME REMAINING: {timer_display}")
            print("====================================")
            print(" (Press Ctrl+C to stop the timer early)")
            
            time.sleep(1)
            seconds -= 1

        # Step 3: The Reward (ASCII Art)
        clear_screen()
        print("WELL DONE! SESSION COMPLETE.")
        print("""
              (  )   (   )  )
               ) (   )  (  (
               ( )  (    ) )
               _____________
              <_____________> ___
              |             |/ _ \\
              |               | | |
              |               |_| |
              |             |\\___/
               \\___________/
        """)
        print("\nTime for a break and a cup of tea!")
        input("\nPress ENTER to exit...")

    except KeyboardInterrupt:
        # This catches Ctrl+C so the program exits gracefully
        print("\n\n[!] Timer stopped manually. Back to work! 📐")
        sys.exit()
    except ValueError:
        print("\n[!] Error: Please enter a number for the minutes.")

# Run the program
if __name__ == "__main__":
    study_timer()