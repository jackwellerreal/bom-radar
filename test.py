from timed import TimedExecution

timer = TimedExecution()

timer.start()

import random
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

config = {
    "noise1": {
        "octaves": 3,
        "base": 8,
        "inner": 1
    },"noise2": {
        "octaves": 6,
        "base": 4,
        "inner": 1
    },"noise3": {
        "octaves": 12,
        "base": 2,
        "inner": 2
    },"noise4": {
        "octaves": 24,
        "base": 1,
        "inner": 4
    },"noise5": {
        "octaves": 48,
        "base": 1,
        "inner": 5
    }
}

seed = random.randint(1,1000)

noise1 = PerlinNoise(octaves=config["noise1"]["octaves"], seed=seed)
noise2 = PerlinNoise(octaves=config["noise2"]["octaves"], seed=seed)
noise3 = PerlinNoise(octaves=config["noise3"]["octaves"], seed=seed)
noise4 = PerlinNoise(octaves=config["noise4"]["octaves"], seed=seed)
noise5 = PerlinNoise(octaves=config["noise5"]["octaves"], seed=seed)

xpix, ypix = 512, 512
pic = []
for i in range(xpix):
    row = []
    for j in range(ypix):
        noise_val = config["noise1"]["base"]*noise1(
            [i/(
                config["noise1"]["inner"]*xpix
                ),
            j/(
                config["noise1"]["inner"]*ypix
                )
            ]
        )
        noise_val += config["noise2"]["base"]*noise1(
            [i/(
                config["noise2"]["inner"]*xpix
                ),
            j/(
                config["noise2"]["inner"]*ypix
                )
            ]
        )
        noise_val += config["noise3"]["base"]*noise1(
            [i/(
                config["noise3"]["inner"]*xpix
                ),
            j/(
                config["noise3"]["inner"]*ypix
                )
            ]
        )
        noise_val += config["noise4"]["base"]*noise1(
            [i/(
                config["noise4"]["inner"]*xpix
                ),
            j/(
                config["noise4"]["inner"]*ypix
                )
            ]
        )
        noise_val += config["noise5"]["base"]*noise1(
            [i/(
                config["noise5"]["inner"]*xpix
                ),
            j/(
                config["noise5"]["inner"]*ypix
                )
            ]
        )

        row.append(noise_val)
    pic.append(row)

plt.imshow(pic, cmap='gray')
plt.savefig('images/weather.png')

timer.end()
total_time = timer.get_elapsed_time()
print(f'code ran in {total_time} seconds')