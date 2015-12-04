# This function is from lecture of Day13
import scipy.stats
from scipy.stats import gamma
import numpy as np

def hrf(tr_times):
    """ Return values for HRF at given times """

    # Gamma pdf for the peak
    peak_values = gamma.pdf(tr_times, 6)
    # Gamma pdf for the undershoot
    undershoot_values = gamma.pdf(tr_times, 12)
    # Combine them
    values = peak_values - 0.35 * undershoot_values
    # Scale max to 0.6
    return values / np.max(values) * 0.6
