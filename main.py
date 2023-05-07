import os
import sys
from pathlib import Path

# Add the modules folder to the Python path
current_dir = Path(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, str(current_dir / "modules"))

# from esp import ESP
# from aimbot import Aimbot
# from fishing import FishingBot
# from navigation import NavigationBot
from config import Config

def main():
    config = Config.load()

    # Initialize ESP and other modules
    # esp = ESP(config.esp)
    # aimbot = Aimbot(config.aimbot)
    # fishing_bot = FishingBot(config.fishing_bot)
    # navigation_bot = NavigationBot(config.navigation_bot)

    # Main loop
    while True:
        # Update ESP
        # esp.update()
        continue

        # Update aimbot if enabled and in the correct action state
        if config.aimbot.enabled:
            # aimbot.update()
            pass

        # Update fishing bot if enabled and in the correct action state
        if config.fishing_bot.enabled:
            # fishing_bot.update()
            pass

        # Update navigation bot if enabled and in the correct action state
        if config.navigation_bot.enabled:
            # navigation_bot.update()
            pass

if __name__ == "__main__":
    main()
