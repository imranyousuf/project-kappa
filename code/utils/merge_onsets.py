def merge_onsets(subject, condition):
	sub_path = os.path.realpath(subject)
	runs_path = ['model/model001/onsets/task001_run'+ i + '/' +  condition + '.txt' for i in ['001','002','003','004','005','006','007','008','009','010','011', '012']]
	cond_list = [np.loadtxt(os.path.join(sub_path, runs_path[i]))[:,:2] for i in range(len(runs_path))]
	merged = np.concatenate(cond_list, axis = 0)       
	return merged


def merge_onsets_5(subject, condition):
        sub_path = os.path.realpath(subject)
        runs_path = ['model/model001/onsets/task001_run'+ i + '/' +  condition + '.txt' for i in ['001','002','003','004','005','006','007','008','009','010','011']]
        cond_list = [np.loadtxt(os.path.join(sub_path, runs_path[i]))[:,:2] for i in range(len(runs_path))]
        merged = np.concatenate(cond_list, axis = 0)       
        return merged

#write code that joined_path’s, that way we don’t have to have this shit -> os.path.join(sub_path, runs_path[i])
