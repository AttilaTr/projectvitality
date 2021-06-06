  #!/bin/bash

sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv -y

python3 -m venv venv
source venv/bin/activate

pip3 install -r server/requirements.txt

python3 -m pytest server --cov=server --cov-report=xml  --junitxml=junit/test-results.xml
python3 -m pytest msdays --cov=msdays --cov-report=xml  --junitxml=junit/test-results.xml
python3 -m pytest msindoor --cov=msindoor --cov-report=xml  --junitxml=junit/test-results.xml
python3 -m pytest msimprovement --cov=msimprovement --cov-report=xml  --junitxml=junit/test-results.xml