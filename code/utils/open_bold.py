def open_bold (subject):
	""" Find all task_run files from a subject BOLD """ 

	sub_path = os.path.realpath(subject)
	sub_path_BOLD = sub_path + '/BOLD'
	task_run = [ i for i in os.listdir(sub_path_BOLD) if not (i.startswith('.'))]

	return task_run