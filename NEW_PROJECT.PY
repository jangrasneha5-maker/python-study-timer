import time
import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def study_timer():
    try:
        # Step 1: Ask for Topic AND Time
        print("--- Custom Study Session Setup ---")
        task_name = input("What are you focusing on? (e.g. AutoCAD, Python, Math): ")
        val = input(f"Enter minutes for {task_name}: ")
        
        minutes = float(val)
        seconds = int(minutes * 60)

        # Step 2: The Countdown Loop
        while seconds > 0:
            clear_screen()
            mins, secs = divmod(seconds, 60)
            timer_display = f"{mins:02d}:{secs:02d}"
            
            print("====================================")
            # Now it shows whatever you typed in task_name!
            print(f"   CURRENT FOCUS: {task_name.upper()} ") 
            print("====================================")
            print(f"      TIME REMAINING: {timer_display}")
            print("====================================")
            print(" (Press Ctrl+C to stop the timer early)")
            
            time.sleep(1)
            seconds -= 1

        # Step 3: The Reward
        clear_screen()
        print(f"WELL DONE! {task_name.upper()} SESSION COMPLETE.")
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
        print(f"\nTime for a break after that {task_name} session!")
        input("\nPress ENTER to exit...")

    except KeyboardInterrupt:
        print("\n\n[!] Timer stopped manually. See you later! 👋")
        sys.exit()
    except ValueError:
        print("\n[!] Error: Please enter a valid number for minutes.")

if __name__ == "__main__":
    study_timer()