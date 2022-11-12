#%%
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
def sinplot(fit=1):
    data=np.linspace(0,14,100)
    for i in range(1,7):
        plt.plot(data,np.sin(data+i*0.5)*(7-i)*fit)

with sns.axes_style('darkgrid'):
    plt.subplot(211)
    sinplot()
plt.subplot(212)
sinplot(-1)
plt.show()
# %%
import matplotlib.pyplot as plt

plt.figure()
x=[18,33,6]
y=[50,60,70]
plt.plot(x,y)
# %%
