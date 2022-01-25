import matplotlib.pyplot as plt
import pandas as pd

#--------------------------------------GRAPH №1-------------------------------------#
def graph1():
    df = pd.read_csv('../log.csv', skiprows=1, nrows=2100)  # Plot 4205
    runc = pd.read_csv('../log.csv', skiprows=56865, nrows=84)  # Plot

    df = df.loc[df["CPU"] == 'all'].reset_index(drop=True)
    print('meow1')
    #
    df['%idle'] = 100 - df['%idle']
    df["runq-sz"] = runc["runq-sz"]
    #
    df['09:20:06'] = pd.to_datetime(df['09:20:06']).apply(lambda x: x.strftime('%H:%M'))
    df['09:20:06'] = pd.to_datetime(df['09:20:06'], format='%H:%M')

    dff = pd.DataFrame(df)

    idx = [i for i in range(0, 84)]
    positions = [p for p in df['09:20:06']]
    labels = [l.strftime('%H:%M') for l in positions]

    df.plot(y=["runq-sz", '%idle'], figsize=(10, 16.5), grid=True, xlim=(0, 20))

    plt.xticks(idx[0::5], labels[0::5])
    plt.xlabel('Продолжительность теста ч:мм', loc='right', fontsize=10, fontweight='bold')
    plt.title("Утилизация CPU", loc='center', fontsize=14, fontweight='bold')
    plt.title("Утилизация CPU,  %", loc='left', fontsize=8)
    plt.title("Длина очереди, шт", loc='right', fontsize=8)
    plt.show()


#--------------------------------------GRAPH №2-------------------------------------#
def graph2():
    df = pd.read_csv('../log.csv', skiprows=56469, nrows=194)  # swp
    runc = pd.read_csv('../log.csv', skiprows=56271, nrows=194)  # Plot
    #
    df["memused"] = runc["%memused"]
    print('meow2')

    df['09:20:06'] = pd.to_datetime(df['09:20:06']).apply(lambda x: x.strftime('%H:%M'))
    df['09:20:06'] = pd.to_datetime(df['09:20:06'], format='%H:%M')

    idx = [i for i in range(0, 193)]
    positions = [p for p in df['09:20:06']]
    labels = [l.strftime('%H:%M') for l in positions]

    df['memused'].plot(figsize=(10, 16.5), grid=True, xlim=(0, 20), ylim=(0, 80))
    df['%swpused'].plot(secondary_y=True)

    plt.xticks(idx[0::15], labels[0::15], rotation='vertical')
    plt.xlabel('Продолжительность теста ч:мм', loc='right', fontsize=10, fontweight='bold')
    plt.title("Утилизация Памяти", loc='center', fontsize=14, fontweight='bold')
    plt.title("Утилизация подкачки, %", loc='left', fontsize=8)
    plt.title("Использование памяти, %", loc='right', fontsize=8)
    plt.show()

#-------------------------------------GRAPH №3-------------------------------------#
def graph3():
    df = pd.read_csv('../log.csv', skiprows=57063, nrows=4290)  # swp

    df['09:20:06'] = pd.to_datetime(df['09:20:06']).apply(lambda x: x.strftime('%H:%M'))
    df['09:20:06'] = pd.to_datetime(df['09:20:06'], format='%H:%M')

    idx = [i for i in range(0,4290)]
    positions = [p for p in df['09:20:06']]
    labels = [l.strftime('%H:%M') for l in positions]

    df.plot(y=["await", 'svctm'], figsize=(10, 16.5), grid=True, xlim=(0,20))

    plt.xticks(idx[0::100], labels[0::100], rotation='vertical')
    plt.xlabel('Продолжительность теста ч:мм', loc='right', fontsize=10, fontweight='bold')
    plt.title("Среднее время чтения/записи", loc='center',fontsize=14, fontweight='bold')
    plt.title("Среднее время чтения/записи", loc='left', fontsize=8)
    plt.title("Использование памяти, %", loc='right', fontsize=8)

    plt.show()
#-------------------------------------GRAPH №4-------------------------------------#без нулей
def graph4():
    df = pd.read_csv('../log.csv', skiprows=57063, nrows=4290)  # swp

    df = df.loc[df["await"] != 0.00].reset_index(drop=True)
    # print(df['await'])
    df['09:20:06'] = pd.to_datetime(df['09:20:06']).apply(lambda x: x.strftime('%H:%M'))
    df['09:20:06'] = pd.to_datetime(df['09:20:06'], format='%H:%M')

    idx = [i for i in range(0,1159)]
    positions = [p for p in df['09:20:06']]
    labels = [l.strftime('%H:%M') for l in positions]

    df.plot(y=["await", 'svctm'], figsize=(10, 16.5), grid=True, xlim=(0,20))

    plt.xticks(idx[0::30], labels[0::30], rotation='vertical')
    plt.xlabel('Продолжительность теста ч:мм', loc='right', fontsize=10, fontweight='bold')
    plt.title("Среднее время чтения/записи", loc='center',fontsize=14, fontweight='bold')
    plt.title("Среднее время чтения/записи", loc='left', fontsize=8)
    plt.show()
#-------------------------------------GRAPH №5-------------------------------------#
def graph5():
    df = pd.read_csv('../log.csv', skiprows=57063, nrows=4290)  # Plot 4205
    #
    df['09:20:06'] = pd.to_datetime(df['09:20:06']).apply(lambda x: x.strftime('%H:%M'))
    df['09:20:06'] = pd.to_datetime(df['09:20:06'], format='%H:%M')

    idx = [i for i in range(0,4290)]
    positions = [p for p in df['09:20:06']]
    labels = [l.strftime('%H:%M') for l in positions]
    #
    df.plot(y=["avgqu-sz"], figsize=(10, 16.5), grid=True, xlim=(0,20))

    plt.xticks(idx[0::100], labels[0::100], rotation='vertical')
    plt.xlabel('Продолжительность теста ч:мм', loc='right', fontsize=10, fontweight='bold')
    plt.title("Очередь дисковой подсистемы", loc='center', fontsize=14, fontweight='bold')
    plt.title("без нулевых значений", loc='left', fontsize=8)
    plt.title("Очередь дисковой подсистемы", loc='right', fontsize=8)
    plt.show()

#-------------------------------------GRAPH №6-------------------------------------# without zero
def graph6():
    df = pd.read_csv('../log.csv', skiprows=57063, nrows=4290)
    #
    df = df.loc[df["avgqu-sz"] != 0.00].reset_index(drop=True)

    df['09:20:06'] = pd.to_datetime(df['09:20:06']).apply(lambda x: x.strftime('%H:%M'))
    df['09:20:06'] = pd.to_datetime(df['09:20:06'], format='%H:%M')

    idx = [i for i in range(0,678)]
    positions = [p for p in df['09:20:06']]
    labels = [l.strftime('%H:%M') for l in positions]

    df.plot(y=["avgqu-sz"], figsize=(10, 16.5), grid=True, xlim=(0, 20))

    plt.xticks(idx[0::30], labels[0::30], rotation='vertical')
    plt.xlabel('Продолжительность теста ч:мм', loc='right', fontsize=10, fontweight='bold')
    plt.title("Очередь дисковой подсистемы", loc='center',fontsize=14, fontweight='bold')
    plt.title("без нулевых значений", loc='left', fontsize=8)
    plt.title("Очередь дисковой подсистемы", loc='right', fontsize=8)
    plt.show()

#-------------------------------------GRAPH №7-------------------------------------# without zero
def graph7():
    df = pd.read_csv('../log.csv', skiprows=57063, nrows=4290)
    #
    df = df.loc[df["%util"] != 0.00].reset_index(drop=True)

    df['09:20:06'] = pd.to_datetime(df['09:20:06']).apply(lambda x: x.strftime('%H:%M'))
    df['09:20:06'] = pd.to_datetime(df['09:20:06'], format='%H:%M')
    print(df)
    idx = [i for i in range(0,1134)]
    positions = [p for p in df['09:20:06']]
    labels = [l.strftime('%H:%M') for l in positions]

    df.plot(y=["%util"], figsize=(10, 16.5), grid=True, xlim=(0, 20))

    plt.xticks(idx[0::30], labels[0::30], rotation='vertical')
    plt.xlabel('Продолжительность теста ч:мм', loc='right', fontsize=10, fontweight='bold')
    plt.title("Утилизация CPU\nдисковой подсистемой (устройство)", loc='center',fontsize=14, fontweight='bold')
    plt.title("Использование CPU\nдисковой подсистемой", loc='left', fontsize=8)
    plt.show()

#-------------------------------------GRAPH №8-------------------------------------#
def graph8():
    df = pd.read_csv('../log.csv', skiprows=61377, nrows=1364)
    #

    df['09:20:06'] = pd.to_datetime(df['09:20:06']).apply(lambda x: x.strftime('%H:%M'))
    df['09:20:06'] = pd.to_datetime(df['09:20:06'], format='%H:%M')
    print(df['txkB/s'])

    idx = [i for i in range(0,390)]
    positions = [p for p in df['09:20:06']]
    labels = [l.strftime('%H:%M') for l in positions]

    df.plot(y=["txkB/s", "rxkB/s"], figsize=(10, 16.5), grid=True, xlim=(0, 20))

    plt.xticks(idx[0::30], labels[0::30], rotation='vertical')
    plt.xlabel('Продолжительность теста ч:мм', loc='right', fontsize=10, fontweight='bold')
    plt.title("Утилизация сетевого интерфейса", loc='center',fontsize=14, fontweight='bold')
    plt.title("Кбит/с", loc='left', fontsize=8)
    plt.show()

#-------------------------------------GRAPH №9-------------------------------------#
def graph9():
    df = pd.read_csv("../log.csv", skiprows=61377, nrows=1364)
    #
    df = df.loc[df["txkB/s"] != 0.00].reset_index(drop=True)
    df = df.loc[df["rxkB/s"] != 0.00].reset_index(drop=True)

    df['09:20:06'] = pd.to_datetime(df['09:20:06']).apply(lambda x: x.strftime('%H:%M'))
    df['09:20:06'] = pd.to_datetime(df['09:20:06'], format='%H:%M')
    print(df['txkB/s'])

    idx = [i for i in range(0,390)]
    positions = [p for p in df['09:20:06']]
    labels = [l.strftime('%H:%M') for l in positions]

    df.plot(y=["txkB/s", "rxkB/s"], figsize=(10, 16.5), grid=True, xlim=(0, 20))

    plt.xticks(idx[0::30], labels[0::30], rotation='vertical')
    plt.xlabel('Продолжительность теста ч:мм', loc='right', fontsize=10, fontweight='bold')
    plt.title("Утилизация сетевого интерфейса", loc='center',fontsize=14, fontweight='bold')
    plt.title("Кбит/с", loc='left', fontsize=8)
    plt.show()

#-------------------------------------GRAPH №10-------------------------------------#
def graph10():
    df = pd.read_csv("../log.csv", skiprows=56865, nrows=195)
    #

    df['09:20:06'] = pd.to_datetime(df['09:20:06']).apply(lambda x: x.strftime('%H:%M'))
    df['09:20:06'] = pd.to_datetime(df['09:20:06'], format='%H:%M')
    # print(df['txkB/s'])

    idx = [i for i in range(0,195)]
    positions = [p for p in df['09:20:06']]
    labels = [l.strftime('%H:%M') for l in positions]

    df.plot(y=["ldavg-1", "ldavg-5", "ldavg-15"], figsize=(10, 16.5), grid=True, xlim=(0, 20))

    plt.xticks(idx[0::10], labels[0::10], rotation='vertical')
    plt.xlabel('Продолжительность теста ч:мм', loc='right', fontsize=10, fontweight='bold')
    plt.title("Динамика Load Average", loc='center',fontsize=14, fontweight='bold')
    plt.title("Кбит/с", loc='left', fontsize=8)
    plt.show()

# running the functions, uncomment if u need to
# graph1()
# graph2()
# graph3()
# graph4()
# graph5()
# graph6()
# graph7()
# graph8()
# graph9()
graph10()