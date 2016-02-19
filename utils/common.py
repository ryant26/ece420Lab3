from subprocess import call

def run_datagen(problem_size):
	call(["../bin/datagen", "-s", str(problem_size)])

def run_main(threads):
	call(["../bin/main", str(threads)])

def run_serialtester():
	call(["../bin/serialtester"])

def cleanup():
	call(["rm", "-f", "data_input"])
	call(["rm", "-f", "*.txt"])


def get_runtime():
	with open('data_output', 'rb') as f:
		for i, line in enumerate(f):
			if i == 2:
				return float(line.strip())
