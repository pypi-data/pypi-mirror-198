import timeit
from time import time
import numpy as np
import pandas as pd
import matplotlib.pylab as plt

"""
future version:
- expand to include data which is 2d like in the case of dataframe
- expand to check entire functions instead of single operation
- expand to include space complexity
- expand to include line profiler
- expand to include memory profiler
"""


## example function
""" 
def power2(n):
    return [i**2 for i in n]
 """        
def function_timer(somefunc):
    start = timeit.default_timer()
    somefunc
    stop = timeit.default_timer()
    return stop-start

def repeatNshuffle(data,repeat):
    newdata = np.repeat(data,repeat)
    np.random.shuffle(newdata)
    return newdata

def timefor_VariedN(func, data):

    #n_test_size = [len(data)]
    #n_test_size.extend([10**i for i in range(2,5)])
    n_test_size = [i for i in range(100,10000,1000)]

    # for loop converted to list comprehenion for faster execution
    execution_time = [function_timer(                       #calling function that calculates the execution time
                        func(                               #calling the function passed by the user
                            repeatNshuffle(data,i/len(data))))
                            #np.repeat(data,i/len(data))))  #create multiple samples of data with varied size
                                    for i in n_test_size]
    """ 
    execution_time = dict()
    for i in n_test_size:
        test_n = np.repeat(data,i/len(data))
        execution_time[f'{len(test_n)}'] = function_timer(func(test_n)) """
    table= pd.DataFrame.from_dict({'data_size': n_test_size, 'time_taken': execution_time})
    table['rolling_mean'] = table.time_taken.rolling(2).mean()
    return table

def plot_time_execution(table,color='',legend_label=''):
        x = table.data_size
        y = table.time_taken
        #find line of best fit
        a, b = np.polyfit(x, y, 1)
        #add points to plot
        #plt.scatter(x, y, color='purple')
        #add line of best fit to plot
        plt.plot(x, a*x+b, color=color, label=legend_label, linestyle='--', linewidth=2)
        plt.legend()

if __name__ == "__main__":
    unsorted_list = np.random.randint(100,10000,1000)
    builtin_sort = timefor_VariedN(sorted,unsorted_list)
    numpy_sort = timefor_VariedN(np.sort,unsorted_list)
    plot_time_execution(builtin_sort, color = 'red',legend_label='builtin')
    plot_time_execution(numpy_sort, color ='blue',legend_label = 'numpy')
