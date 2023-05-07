import json
from dataclasses import dataclass

@dataclass
class ESPConfig:
    enabled: bool

@dataclass
class AimbotConfig:
    enabled: bool

@dataclass
class FishingBotConfig:
    enabled: bool

@dataclass
class NavigationBotConfig:
    enabled: bool

@dataclass
class Config:
    esp: ESPConfig
    aimbot: AimbotConfig
    fishing_bot: FishingBotConfig
    navigation_bot: NavigationBotConfig

    @classmethod
    def load(cls, config_file="config.json"):
        with open(config_file, "r") as file:
            config_data = json.load(file)

        esp = ESPConfig(config_data["esp"]["enabled"])
        aimbot = AimbotConfig(config_data["aimbot"]["enabled"])
        fishing_bot = FishingBotConfig(config_data["fishing_bot"]["enabled"])
        navigation_bot = NavigationBotConfig(config_data["navigation_bot"]["enabled"])

        return cls(esp, aimbot, fishing_bot, navigation_bot)
