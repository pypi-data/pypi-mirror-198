from volux import VoluxDemo
from time import perf_counter

HZ = 60
SECONDS_PER_HUE_CYCLE = 30
MAX_BRIGHTNESS_MULTIPLIER = 0.2


class HueDemo(VoluxDemo):
    id = "hue"
    description = "A simple demo that slowly fades the hue of a smartlight."
    DEV__requirements = [
        {"distribution_name": "voluxlight", "version_requirement": ">=2.0.0, <3"},
    ]

    @staticmethod
    def main():
        from time import sleep
        from volux.util import get_sine
        from voluxlight import VoluxLightLifxLan

        light_name = input("LIFX device label (case sensitive): ")

        with VoluxLightLifxLan([light_name]) as light:
            hue = 0
            while True:
                y = get_sine(perf_counter() / (SECONDS_PER_HUE_CYCLE * 4), 60)
                y = (y + 1) / 2  # convert y to unit interval

                h = hue
                s = 65535
                v = min(((0.8 * MAX_BRIGHTNESS_MULTIPLIER) + (y * 0.2)) * 65535, 65535)
                k = 6500

                light.set_color((h, s, v, k))
                hue = (hue + (65535 / (HZ * SECONDS_PER_HUE_CYCLE))) % 65535
                sleep(1 / HZ)
