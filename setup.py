import cx_Freeze

executables = [cx_Freeze.Executable("main.py",targetName="RabbitRun.exe")]

cx_Freeze.setup(
	name = "RabbitRun",
	options={"build_exe": {"packages":["pygame"],
							"include_files":["Images","Sounds"]}},
	executables = executables
	)