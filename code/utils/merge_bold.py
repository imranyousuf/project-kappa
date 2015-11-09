def merge_bold(subject):
	directpath = os.path.realpath(subject)
	runs = ['BOLD/task001_run'+ i + '/bold.nii.gz' for i in ['001','002','003','004','005','006','007','008','009','010','011','012']]
	bolds_list = [nib.load(os.path.join(directpath, runs[i])).get_data() for i in range(len(runs))]
	merged = np.concatenate(bolds_list, axis = 3)
	return merged


