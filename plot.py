from matplotlib import pyplot as plt

wid = 7

plt.figure(figsize=(8, 6))

plt.rc('axes', labelsize=20)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=16)    # fontsize of the tick labels
plt.rc('ytick', labelsize=16)    # fontsize of the tick labels
plt.rc('font', size=14)          # controls default text sizes

plt.xlabel("Number of blocks mined")
plt.ylabel("Computation Time (s)")
plt.title("No. of nodes: 7,     No. of transactions per block: 250")

times = [20.82, 52.71, 78.11, 103.19, 127.26]
blks = [10, 20, 30, 40, 50]

for index, _ in enumerate(blks):
    plt.text(blks[index] - wid/3, times[index] + 1,
             times[index])


plt.bar(blks, times, width=wid, color='blue')
plt.show()

##########

wid = 70

plt.figure(figsize=(8, 6))

plt.rc('axes', labelsize=20)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=16)    # fontsize of the tick labels
plt.rc('ytick', labelsize=16)    # fontsize of the tick labels
plt.rc('font', size=16)          # controls default text sizes

plt.xlabel("Number of Transactions per block")
plt.ylabel("Computation Time (s)")
plt.title("No. of nodes: 7,     No. of blocks mined: 10")

times = [2.37, 10.59, 31.61, 50.23, 72.85]
txs = [100, 200, 300, 400, 500]

for index, _ in enumerate(txs):
    plt.text(txs[index] - wid/3, times[index] + 0.5,
             times[index])


plt.bar(txs, times, width=wid, color='green')
plt.show()