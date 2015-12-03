import os


def cond_path(subject, task_num, cond_num):
	""" This function returns the path of the condition file you choose 

	Parameter
	---------
	subject: str
		Please specific the subject. For example, you should input 'sub001' if choose the first subject
	task_num: str
		Please specific the subject. For example, you should input 'task001_run001' if choose the first run.
	cond_num: str
		Please specific the subject. For example, you should input 'cond001.txt' if choose the first condition. 

	Return 
	------
	path: str
		This is the path of the condition file that you choose.
	"""

	sub_path = os.path.realpath(subject)
	path = sub_path + '/model/model001/onsets' + '/' + task_num + '/' + cond_num

	return path
    