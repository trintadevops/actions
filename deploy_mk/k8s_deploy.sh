sudo apt-get install python3 -y
sudo apt-get update
sudo apt-get install python3-pip -y
pip3 install kubernetes
pip3 install docker
pip3 install kubeconfig
python3 ${GITHUB_ACTION_PATH}/k8sdeploy.py
