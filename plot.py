from matplotlib import pyplot as plt
 
wid = 0.7

# Creating dataset
times = [0.408, 0.556]
txs = [10, 20, 30 , 40, 50]
 
# Creating histogram
plt.bar(txs, times, width=wid)
 
# Show plot
plt.show()