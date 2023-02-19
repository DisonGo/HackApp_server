SCRIPTS_PATH = ./scripts
VENV_NAME = venv


clean:
	rm -rf ./${VENV_NAME}
	@rm -rf $(shell find . -name '*pycache*')


install:
	cd ${SCRIPTS_PATH}; bash install.sh


run_data: 
	cd ${SCRIPTS_PATH}; bash run_data_server.sh


run_auth:
	cd ${SCRIPTS_PATH}; bash run_auth_server.sh