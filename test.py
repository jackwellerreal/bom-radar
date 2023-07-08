from timed import TimedExecution

timer = TimedExecution()

timer.start()

import random
import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

multipliers = {
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

noise1 = PerlinNoise(octaves=multipliers["noise1"]["octaves"], seed=seed)
noise2 = PerlinNoise(octaves=multipliers["noise2"]["octaves"], seed=seed)
noise3 = PerlinNoise(octaves=multipliers["noise3"]["octaves"], seed=seed)
noise4 = PerlinNoise(octaves=multipliers["noise4"]["octaves"], seed=seed)
noise5 = PerlinNoise(octaves=multipliers["noise5"]["octaves"], seed=seed)

xpix, ypix = 512, 512
pic = []
for i in range(xpix):
    row = []
    for j in range(ypix):
        noise_val = multipliers["noise1"]["base"]*noise1(
            [i/(
                multipliers["noise1"]["inner"]*xpix
                ),
            j/(
                multipliers["noise1"]["inner"]*ypix
                )
            ]
        )
        noise_val += multipliers["noise2"]["base"]*noise1(
            [i/(
                multipliers["noise2"]["inner"]*xpix
                ),
            j/(
                multipliers["noise2"]["inner"]*ypix
                )
            ]
        )
        noise_val += multipliers["noise3"]["base"]*noise1(
            [i/(
                multipliers["noise3"]["inner"]*xpix
                ),
            j/(
                multipliers["noise3"]["inner"]*ypix
                )
            ]
        )
        noise_val += multipliers["noise4"]["base"]*noise1(
            [i/(
                multipliers["noise4"]["inner"]*xpix
                ),
            j/(
                multipliers["noise4"]["inner"]*ypix
                )
            ]
        )
        noise_val += multipliers["noise5"]["base"]*noise1(
            [i/(
                multipliers["noise5"]["inner"]*xpix
                ),
            j/(
                multipliers["noise5"]["inner"]*ypix
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