import os


def path_bold(subject, task_num):
	""" This function returns the path of the bold according to the task run number 

	Parameter
	---------
	subject: str
		Please specific the subject. For example, you should input 'sub001' if choose the first subject
	task_num: str
		Please specific the subject. For example, you should input 'task001_run001' if choose the first run.

	Return
	------
	bold_path: str
		this is the path of the bold.
	"""

	sub_path = os.path.realpath(subject)
	bold_path = sub_path + '/BOLD' + '/' + task_num

	return bold_path