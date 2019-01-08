

# RANDOM WALK!!!!!

# Numpy is imported, seed is set
import numpy as np

np.random.seed(123) # set seed

# Initialization
random_walk = [0] # create a list in which we stock the walk

for x in range(100) : # amount of iterations
    step = random_walk[-1] # create step, equal to last position of walk
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step) # update our walk with last step

# Print random_walk
print(random_walk)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()