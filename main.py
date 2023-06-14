import scipy.signal as sci
import pandas as pd
import numpy as np
import spiceypy as spice
import matplotlib.pyplot as plt

Rm = 2439.4

data = pd.read_table(r"..\MAGMSOSCI12137_V08.TAB",
                     header=None,
                     delim_whitespace=True,
                     parse_dates=[[0,1,2,3,4]],
                     date_format="%Y %j %H %M %S.%f")
data.columns = ["time", "tag", "x", "y", "z", "Bx", "By", "Bz"]
data['lat'] = np.arcsin(data.z / np.sqrt(data.x**2 + data.y**2 + data.z**2)) * (180/np.pi)

fig, (ax1, ax2) = plt.subplots(2,1)
plt.subplots_adjust(hspace=0)

ax1.specgram(data.Bz, Fs=20)
ax1.get_xaxis().set_visible(False)
ax1.set_ylabel("Frequency (Hz)")

ax2.plot(data.time, data.lat)
ax2.set_xlabel("Time")
ax2.set_ylabel("Latitude (deg)")
ax2.set_xlim(min(data.time), max(data.time))

plt.show()
