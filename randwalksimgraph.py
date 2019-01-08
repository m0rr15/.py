

# RANDOM WALK!!!!!

# Numpy is imported, seed is set
import numpy as np

np.random.seed(123) # set seed



all_walks = [] # initialize and populate all_walks
for i in range(10) : #  number of sims
    random_walk = [0]
    for x in range(100) : # length of rand walk
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        
        # Implement clumsiness
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk) # IMPORTANT: diff. indentation closes loops!!!!!

# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)

# # Plot np_aw and show
# plt.plot(np_aw)
# plt.show()
# # Clear the figure
# plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()


# Select last row from np_aw_t: ends. This contains endpoints of all sim. walks
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()
