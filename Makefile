SCRIPTS_PATH = ./scripts
VENV_NAME = venv


clean:
	rm -rf ./${VENV_NAME}
	@rm -rf $(shell find . -name '*pycache*')


install:
	cd ${SCRIPTS_PATH}; bash install.sh


run: 
	cd ${SCRIPTS_PATH}; bash run_env_and_start.sh