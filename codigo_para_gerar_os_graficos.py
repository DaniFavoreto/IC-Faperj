import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

df1 = pd.read_csv("gmapping_map_data.csv")
df2 = pd.read_csv("gmapping_odom_data.csv")
df3 = pd.read_csv("rtab_map_data.csv")
df4 = pd.read_csv("rtab_odom_data.csv")

figure(figsize=(8, 6), dpi=80)

plt.plot(df1.x_value, df1.y_value, ':', linewidth = 7)
plt.plot(df2.x_value, df2.y_value, 'r', linewidth = 2)

plt.legend(["Posição estimada", "Posição real do robô"])
plt.title("GMapping Slam")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")

figure(figsize=(8, 6), dpi=80)
plt.plot(df3.x_value, df3.y_value, ':', linewidth = 7)
plt.plot(df4.x_value, df4.y_value, 'r', linewidth = 2)

plt.legend(["Posição estimada", "Posição real do robô"])
plt.title("Rtab Slam")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
