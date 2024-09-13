from scipy.optimize import minimize

# Define cost function for energy usage
def cost_function(x):
    return x[0]**2 + x[1]**2 + 100 * (x[2]**2)

# Initial guess
initial_guess = [1, 1, 1]

# Minimize energy cost
result = minimize(cost_function, initial_guess, method='BFGS')
print("Optimized Energy Usage:", result.x)
