import numpy as np
import sys
import matplotlib.pyplot as plt

# Taken from Wikipedia:
def simpson_nonuniform(x, f):
    """
    Simpson rule for irregularly spaced data.

        Parameters
        ----------
        x : list or np.array of floats
                Sampling points for the function values
        f : list or np.array of floats
                Function values at the sampling points

        Returns
        -------
        float : approximation for the integral
    """
    N = len(x) - 1
    h = np.diff(x)

    result = 0.0
    for i in range(1, N, 2):
        hph = h[i] + h[i - 1]
        result += f[i] * ( h[i]**3 + h[i - 1]**3
                           + 3. * h[i] * h[i - 1] * hph )\
                     / ( 6 * h[i] * h[i - 1] )
        result += f[i - 1] * ( 2. * h[i - 1]**3 - h[i]**3
                              + 3. * h[i] * h[i - 1]**2)\
                     / ( 6 * h[i - 1] * hph)
        result += f[i + 1] * ( 2. * h[i]**3 - h[i - 1]**3
                              + 3. * h[i - 1] * h[i]**2)\
                     / ( 6 * h[i] * hph )

    if (N + 1) % 2 == 0:
        result += f[N] * ( 2 * h[N - 1]**2
                          + 3. * h[N - 2] * h[N - 1])\
                     / ( 6 * ( h[N - 2] + h[N - 1] ) )
        result += f[N - 1] * ( h[N - 1]**2
                           + 3*h[N - 1]* h[N - 2] )\
                     / ( 6 * h[N - 2] )
        result -= f[N - 2] * h[N - 1]**3\
                     / ( 6 * h[N - 2] * ( h[N - 2] + h[N - 1] ) )
    return result


print "Hello world!"

print 'Argument List:', str(sys.argv)

a = int(sys.argv[1])

b = int(sys.argv[2])
n = int(sys.argv[3])

print 'a = ' + str(a)
print 'b = ' + str(b)
print 'n = ' + str(n)



# Compute the x and y coordinates for points on a quarter of the circle

# Added increment to endpoint to make x include 0 to pi/2 inclusive.
# 
x = np.arange(0, np.pi/2.0 + (np.pi/2.0)/n, (np.pi/2.0)/n)
y = np.sqrt(a*a*np.cos(x)*np.cos(x) + b*b*np.sin(x)*np.sin(x))

print('last element: ' + str(x[len(x) - 1]))
print('pi over 2: ' + str(np.pi/2.0))


perimeter = 1.0
perimeter = 4*simpson_nonuniform(x, y)

print('estimated perimeter: ' + str(perimeter))

# Plot the points using matplotlib
plt.plot(x, y)
plt.show()  # You must call plt.show() to make graphics appear.
