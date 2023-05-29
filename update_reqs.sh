

pip install pip pip-tools --upgrade

# update reqs
pip-compile requirements.in --verbose --upgrade --resolver=backtracking --extra-index-url https://download.pytorch.org/whl/cpu 

# install and test
pip install -r requirements.txt
pip install pytest
pytest tests