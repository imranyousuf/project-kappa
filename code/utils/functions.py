def vol_std(data):

    T = data.shape[-1]
    std_values = np.zeros(T)

    for i in range(T):
        std_values[i] = np.std(data[...,i])

    return std_values


def iqr_outliers(arr_1d, iqr_scale=1.5):
   
   
    q75, q25 = np.percentile(arr_1d, [75 ,25])
    iqr = q75 - q25
    upper = q75 + iqr * iqr_scale
    lower = q25 - iqr * iqr_scale
    upper_mask = arr_1d > upper
    lower_mask = arr_1d < lower
    upper_indice = np.nonzero(upper_mask)
    lower_indice = np.nonzero(lower_mask)
    outlier_indices = np.append(upper_indice, lower_indice)
    return np.sort(outlier_indices), (lower, upper)



def vol_rms_diff(arr_4d):
 
    T = arr_4d.shape[-1]
    rms_values = np.zeros(T-1)
    for i in range(T - 1):
        diff_vol = arr_4d[..., i + 1] - arr_4d[..., i]
        rms_values[i] = np.sqrt(np.mean(diff_vol ** 2))

    return rms_values


def extend_diff_outliers(diff_indices):
  
    extended_indices = np.sort(np.tile(diff_indices,2))

    for i in range(len(extended_indices)):
        if i % 2 == 1:
            extended_indices[i] = extended_indices[i] + 1

    return np.unique(extended_indices)