eval $(minikube docker-env)
pip3 install kubernetes
pip3 install docker
pip3 install kubeconfig
python3 ${GITHUB_ACTION_PATH}/k8sdeploy.py
