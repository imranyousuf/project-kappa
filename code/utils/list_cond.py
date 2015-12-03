import os

def list_every_cond(subject, task_num):
	""" 
	This function returns condition list.

	Parameter
	---------
	subject: str 
		Please specify the number of the subject. For example, you should input 'sub001' if choose the first subject.
	task_num: task_num
		Please specify the number of the task. For example, you should input 'task001_run001' if choose the first subject.


	Returns 
	------
	condition: list
		It lists each conditions 

	"""

	sub_path = os.path.realpath(subject)
	sub_path_cond = sub_path + '/model/model001/onsets' + '/' + task_num
	condition = [ i for i in os.listdir(sub_path_cond) if not (i.startswith('.'))]

	return condition
