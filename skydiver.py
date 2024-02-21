import math
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import seaborn as sns
import plotly.express as px
import pandas as pd


# mpl.use('macosx')

h = 0.01
g = 9.81
rho = 1.225     # air density
S = 1.0         # surface area
Cd = 0.43       # coeff of drag
m = 85.0        # mass

Az, Vz, Pz = 0.0, 0.0, 0.0
Drag = 0.0
t = 0.0


def integrate(y: float, x: float, h: float) -> float:
    return y + x * h


if __name__ == '__main__':
    Vz = 0.0
    Pz = 30000.0
    t = 0.0

    time = []
    position = []
    velocity = []
    surface_area = []
    drag = []

    while True:

        print(Pz)

        if math.isinf(Pz):
            break
        elif Pz < 0.0:
            break

        if Pz < 1000:
            S = min(S + 1.0 * h, 300.0)
            Cd = min(Cd + 1.0 * h, 1.75)

        t = t + h
        Drag = 0.5 * rho * Vz * Vz * S * Cd
        Az = Drag / m - g
        Vz = integrate(Vz, Az, h)
        Pz = integrate(Pz, Vz, h)

        time.append(t)
        position.append(Pz)
        velocity.append(Vz*10)
        surface_area.append(S)
        drag.append(Drag)

    data = pd.DataFrame({'Time': time, 'Pz': position, 'Vz': velocity, 'S': surface_area, 'Drag': drag})

    # data_long = pd.melt(data, id_vars=('Time',), value_vars=('Pz', 'Vz', 'Drag',),
    #                     var_name='Series', value_name='Value')
    # sns.lineplot(x='Time', y='Value', hue='Series', data=data_long)
    # plt.show()

    fig = px.line(data, y=['Pz', 'Vz', 'S', 'Drag'], x='Time')
    fig.update_layout(hovermode='x')
    fig.show()
