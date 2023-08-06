#@title FINAL (TESE) Graph { display-mode: "form" }

class Graph():
  def __init__(self):
    pass
  def Heatmap(self, location, panel_tilt:int = 35, surface_azimuth:int = 0, year:int=2020): 
    
    from pvmodule import PVGIS
    import calendar
    import matplotlib.pyplot as plt
    import seaborn as sns

    _, data, _ = PVGIS().retrieve_hourly(location.latitude, location.longitude , startyear = year, endyear= year,surface_tilt = panel_tilt, surface_azimuth = surface_azimuth)

    heatmap_data_normal = data.iloc[-(365 + calendar.isleap(int(2020)))*24:].copy()
    heatmap_data_normal = heatmap_data_normal.drop(columns=['H_sun', 'T2m', 'WS10m', 'Int'], axis=1)
    heatmap_data_normal['Day'] = heatmap_data_normal.index.date
    heatmap_data_normal['Time in hours' ] = heatmap_data_normal.index.time
    heatmap_data_normal = heatmap_data_normal.reset_index(drop=True)


    fig, ax = plt.subplots(figsize=(15,7),sharex=True);

    pivot_normal = heatmap_data_normal.pivot(index='Time in hours', columns='Day', values='G(i)')
    sns.heatmap(pivot_normal,ax=ax,cmap="Spectral_r",vmin=0, vmax=1000)
    ax.set_title(f'Lat: {location.latitude } Long: {location.longitude }');
    ax.grid()
    plt.tight_layout()

  def Bifacial_Heatmap(self, location, surface_azimuth:int = 90, year:int=2020): 
    
    from pvmodule import PVGIS
    import calendar
    import matplotlib.pyplot as plt
    import seaborn as sns

    panel_tilt = 90

    azimuth_backsheet = int(surface_azimuth) + 180
    if azimuth_backsheet <= 180:
      pass
    else:
      azimuth_backsheet = azimuth_backsheet - 360

    _, data1, _ = PVGIS().retrieve_hourly(location.latitude, location.longitude , startyear = year, endyear= year, surface_tilt = panel_tilt, surface_azimuth = surface_azimuth)
    _, data2, _ = PVGIS().retrieve_hourly(location.latitude, location.longitude , startyear = year, endyear= year, surface_tilt = panel_tilt, surface_azimuth = azimuth_backsheet)
    
    data2 = data2.drop(['H_sun','T2m','WS10m'], axis=1)
    data = data1.add(data2, fill_value=0)


    heatmap_data_normal = data.iloc[-(365 + calendar.isleap(int(2020)))*24:].copy()
    heatmap_data_normal = heatmap_data_normal.drop(columns=['H_sun', 'T2m', 'WS10m', 'Int'], axis=1)
    heatmap_data_normal['Day'] = heatmap_data_normal.index.date
    heatmap_data_normal['Time in hours' ] = heatmap_data_normal.index.time
    heatmap_data_normal = heatmap_data_normal.reset_index(drop=True)


    fig, ax = plt.subplots(figsize=(15,7),sharex=True);

    pivot_normal = heatmap_data_normal.pivot(index='Time in hours', columns='Day', values='G(i)')
    sns.heatmap(pivot_normal,ax=ax,cmap="Spectral_r",vmin=0, vmax=1000)
    ax.set_title(f'Lat: {location.latitude } Long: {location.longitude }');
    ax.grid()
    plt.tight_layout()

  def Comparison(self, bifacial_data, normal_data, column_name):
    import numpy as np
    irradiance_1 = bifacial_data
    irradiance_2 = normal_data

    if len(irradiance_1) != len(irradiance_2):
      return print("Dataframes don't have the same length.")

    if ('month' in irradiance_1.columns) and ('month' in irradiance_2.columns):
      irradiance_1 = irradiance_1[['month', column_name]]
      irradiance_2 = irradiance_2[['month', column_name]]

      df1 = irradiance_1[column_name].groupby(irradiance_1['month']).sum()
      df2 = irradiance_2[column_name].groupby(irradiance_2['month']).sum()
      comparison =  ( df1 / df2) * 100
      comparison = comparison.reset_index()
      comparison[column_name] = np.where((df1 / df2) * 100 >= 100 , (df1 / df2) * 100 - 100 , -(df2 / df1) * 100 + 100)

      comparison.rename({'month': 'Month', column_name: 'Irradiance %'}, axis=1, inplace=True)

    else:
      irradiance_1 = irradiance_1[['time', column_name]]
      irradiance_2 = irradiance_2[['time', column_name]]
      df1 = irradiance_1[column_name].groupby(irradiance_1.index.month).sum()
      df2 = irradiance_2[column_name].groupby(irradiance_2.index.month).sum()
      comparison =  ( df1 / df2) * 100
      comparison = comparison.reset_index()
      comparison[column_name] = np.where((df1 / df2) * 100 >= 100 , (df1 / df2) * 100 - 100 , -(df2 / df1) * 100 + 100)
      comparison.rename({'time': 'Month', column_name: 'Irradiance %'}, axis=1, inplace=True)


    import calendar
    comparison['Month'] = comparison['Month'].apply(lambda x: calendar.month_abbr[int(x)])
 
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(15,7),sharex=True);
    bars = ax.bar(
        x=comparison['Month'],
        height=comparison['Irradiance %'],
        tick_label=comparison['Month'],
        hatch='//', 
        alpha=0.5, 
        color='#ff4dc4'
    )

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#DDDDDD')
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True, color='#EEEEEE')
    ax.xaxis.grid(False)

    # Add text annotations to the top of the bars.
    bar_color = bars[0].get_facecolor()
    for bar in bars:
      if bar.get_height() < 0:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() - 2.5,
            f'{round(bar.get_height(), 1)} %',
            horizontalalignment='center',
            color="black",
            weight='bold'
        )
      else:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 2.5,
            f'+{round(bar.get_height(), 1)} %',
            horizontalalignment='center',
            color="black",
            weight='bold'
        )

    # Add labels and a title.
    ax.set_xlabel('Month', labelpad=15, color='#333333', fontsize= 16)
    ax.set_ylabel('Irradiance %', labelpad=15, color='#333333', fontsize= 16)
    ax.set_title('Vertical Bifacial versus Tilted Monofacial', pad=15, color='#333333',
                weight='bold', fontsize= 16)

    gains = round((irradiance_1[column_name].sum() / irradiance_2[column_name].sum()) * 100 - 100,2) 
    gains_watts = round((irradiance_1[column_name].sum() - irradiance_2[column_name].sum())/1000,2)
    bifacial_energy = round(irradiance_1[column_name].sum()/1000,2)
    monofacial_energy = round(irradiance_2[column_name].sum()/1000,2)


  
    if gains < 0:
      ax.text(0.05, 0.85, f'Total loss of {gains} %\nApproximately of {gains_watts} kW/m2\nBifacial Energy of {bifacial_energy} kW/m2 \nNormal Energy of {monofacial_energy} kW/m2',
        style='italic', bbox={'facecolor': 'red', 'alpha': 0.2, 'pad': 10}, transform=plt.gcf().transFigure)
    else:
      ax.text(0.05,0.85, f'Total gain of {gains} %\nApproximately of {gains_watts} kW/m2\nBifacial Energy of {bifacial_energy} kW/m2 \nNormal Energy of {monofacial_energy} kW/m2',
        style='italic', bbox={'facecolor': 'green', 'alpha': 0.2, 'pad': 10}, transform=plt.gcf().transFigure)

    fig.tight_layout()

  

  def Efficiency_curve_of_inverter(self, inverter):
      import pandas as pd
      inverter_efficiency = pd.DataFrame()
      x = [inverter['Power Level 10% (kW)'].values[0] ,inverter['Power Level 20% (kW)'].values[0] ,inverter['Power Level 30% (kW)'].values[0] ,inverter['Power Level 50% (kW)'].values[0] ,inverter['Power Level 75% (kW)'].values[0] ,inverter['Power Level 100% (kW)'].values[0] ]
      y_min = [inverter['Efficiency @Vmin 10% Pwr Lvl (%)'].values[0] ,inverter['Efficiency @Vmin 20% Pwr Lvl (%)'].values[0] ,inverter['Efficiency @Vmin 30% Pwr Lvl (%)'].values[0] ,inverter['Efficiency @Vmin 50% Pwr Lvl (%)'].values[0] ,inverter['Efficiency @Vmin 75% Pwr Lvl (%)'].values[0] ,inverter['Efficiency @Vmin 100% Pwr Lvl (%)'].values[0]]
      y_nom = [inverter['Efficiency @Vnom 10% Pwr Lvl (%)'].values[0] ,inverter['Efficiency @Vnom 20% Pwr Lvl (%)'].values[0] ,inverter['Efficiency @Vnom 30% Pwr Lvl (%)'].values[0] ,inverter['Efficiency @Vnom 50% Pwr Lvl (%)'].values[0] ,inverter['Efficiency @Vnom 75% Pwr Lvl (%)'].values[0] ,inverter['Efficiency @Vnom 100% Pwr Lvl (%)'].values[0]]
      y_max = [inverter['Efficiency @Vmax 10% Pwr Lvl (%)'].values[0] ,inverter['Efficiency @Vmax 20% Pwr Lvl (%)'].values[0] ,inverter['Efficiency @Vmax 30% Pwr Lvl (%)'].values[0] ,inverter['Efficiency @Vmax 50% Pwr Lvl (%)'].values[0] ,inverter['Efficiency @Vmax 75% Pwr Lvl (%)'].values[0] ,inverter['Efficiency @Vmax 100% Pwr Lvl (%)'].values[0]]


      voltage_list = []
      min_voltage = inverter['Voltage Minimum (Vdc)'].values[0]
      voltage_list.append(min_voltage)

      nominal_voltage = inverter['Voltage Nominal (Vdc)'].values[0]
      voltage_list.append(nominal_voltage)

      max_voltage = inverter['Voltage Maximum (Vdc)'].values[0]
      voltage_list.append(max_voltage)


      import numpy as np
      import pylab
      z_min = np.polyfit(x, y_min, 4)
      f_min = np.poly1d(z_min)

      z_nom = np.polyfit(x, y_nom, 4)
      f_nom = np.poly1d(z_nom)

      z_max = np.polyfit(x, y_max, 4)
      f_max = np.poly1d(z_max)


      xx = np.linspace(min(x), max(x), 30)
      xxx = np.linspace(min(x), max(x), 30)
      
      import matplotlib.pyplot as plt
      plt.rcParams["figure.figsize"] = (15,9)

      pylab.semilogy(xx, f_min(xx), 'gD--', markerfacecolor='none', label=r'$η_{min} = %sx^4 + %sx^3 + %sx^2 + %sx + %s$' % (str(f_min).splitlines()[1].rsplit('x')[0].replace(" ", "").replace("+", "").replace("-", ""),str(f_min).splitlines()[1].rsplit('x')[1].replace(" ", "").replace("+", "").replace("-", ""),str(f_min).splitlines()[1].rsplit('x')[2].replace(" ", "").replace("+", "").replace("-", ""),str(f_min).splitlines()[1].rsplit('x')[3].replace(" ", "").replace("+", "").replace("-", ""),str(f_min).splitlines()[1].rsplit('x')[4].replace(" ", "").replace("+", "").replace("-", "")))
      pylab.semilogy(xx, f_nom(xx), 'bv--', markerfacecolor='none', label=r'$η_{nom} = %sx^4 + %sx^3 + %sx^2 + %sx + %s$' % (str(f_nom).splitlines()[1].rsplit('x')[0].replace(" ", "").replace("+", "").replace("-", ""),str(f_nom).splitlines()[1].rsplit('x')[1].replace(" ", "").replace("+", "").replace("-", ""),str(f_nom).splitlines()[1].rsplit('x')[2].replace(" ", "").replace("+", "").replace("-", ""),str(f_nom).splitlines()[1].rsplit('x')[3].replace(" ", "").replace("+", "").replace("-", ""),str(f_nom).splitlines()[1].rsplit('x')[4].replace(" ", "").replace("+", "").replace("-", "")))
      pylab.semilogy(xx, f_max(xx), 'ms--', markerfacecolor='none', label=r'$η_{max} = %sx^4 + %sx^3 + %sx^2 + %sx + %s$' % (str(f_max).splitlines()[1].rsplit('x')[0].replace(" ", "").replace("+", "").replace("-", ""),str(f_max).splitlines()[1].rsplit('x')[1].replace(" ", "").replace("+", "").replace("-", ""),str(f_max).splitlines()[1].rsplit('x')[2].replace(" ", "").replace("+", "").replace("-", ""),str(f_max).splitlines()[1].rsplit('x')[3].replace(" ", "").replace("+", "").replace("-", ""),str(f_max).splitlines()[1].rsplit('x')[4].replace(" ", "").replace("+", "").replace("-", "")))

    
      y_tick1 =  list(dict.fromkeys(np.round(f_min(xxx),1)))
      y_tick2 =  list(dict.fromkeys(np.round(f_nom(xxx),1)))
      y_tick3 =  list(dict.fromkeys(np.round(f_max(xxx),1)))
      x_tick =  list(dict.fromkeys(np.round(xxx,2)))

      y_tick = (y_tick1 + y_tick2 + y_tick3)
      y_tick = list(dict.fromkeys(y_tick))
      y_tick1 = list(dict.fromkeys(np.round(y_tick,0)))
      del y_tick[::2]
      y_tick = y_tick1 + y_tick
      y_tick = list(dict.fromkeys(y_tick))

      plt.legend(loc='lower right', frameon=True)
      plt.grid(color = 'black', linestyle = '--', linewidth = 0.5);
      plt.xticks(x_tick, x_tick);
      plt.yticks(y_tick, y_tick);

      plt.xticks(rotation=45);
      plt.title(f"Inverter Efficiency", fontsize= 16);
      plt.ylabel('Efficiency (%)', fontsize= 16);
      plt.xlabel('Power (kW)', fontsize= 16);
      plt.show()

  def plot(self, data_list, column_name):
    
    import matplotlib.pyplot as plt
    import pandas as pd
    pd.options.mode.chained_assignment = None  # default='w
    fig, ax = plt.subplots();
    colors = ['r','b','g','y','m']
    hatches = ['/', '\\', '|', '-', '+', 'x', 'o', 'O', '.', '*']
    lines = ['--', '-.', '-', ':']
    colors_i = 0
    hatches_i = 0
    lines_i = 0
    for data in data_list:

      data = data.dropna()
      import calendar
      data['month'] = data['month'].apply(lambda x: calendar.month_abbr[int(x)])

      data[column_name].plot(figsize=(11.69,8.27), ax=ax, fontsize=10, color = colors[colors_i],  linestyle = lines[lines_i]);
      plt.fill_between(data.index, data[column_name], step="mid",hatch=hatches[hatches_i], alpha=0.2, color=colors[colors_i])

      colors_i += 1
      hatches_i += 1
      lines_i += 1
      if lines_i == len(lines):
        lines_i = 0
      if hatches_i == len(hatches):
        hatches_i = 0
      if colors_i == len(colors):
        colors_i = 0

    plt.title(f"AVERAGE Yearly IRRADIANCE DATA - {data['month'].values[0]}", fontsize= 10);
    ax.set_ylabel('W/m2', fontsize= 10);
    ax.set_xlabel('time h', fontsize= 10);
    plt.grid(color = 'black', linestyle = '--', linewidth = 0.5);
    plt.xticks(rotation=45);
