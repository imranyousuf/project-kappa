def brain_activation(slice, condition):
	""" This function returns the path of the bold according to the task run number 

	Parameter
	---------
	slice: int
		Transverse slice of the brain where slice = 45 gives you, height wise, middle section of the brain.
	condition: int
		0 = house, 1 = scramble, 2 = cat, 3 = shoe, 4 = bottle, 5 = scissors, 6 = chair, 7 = face

	Return
	------
	bold_path: str
	"""
		
	mean_data[~mask] = np.nan
	betas_vols[~mask] = np.nan

	plt.imshow(mean_data[:, :, slice], cmap='gray', alpha=0.5, interpolation = 'nearest')
	plt.imshow(betas_vols[:, :, slice, condition], alpha=0.5, interpolation = 'nearest')