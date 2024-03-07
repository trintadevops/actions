sudo apt-get update
sudo apt-get install python3 python3-pip maven -y
pip3 install kubernetes
pip3 install docker
pip3 install kubeconfig
echo "############### INSTALACAO MAVEN WRAPER #################"
mvn wrapper:wrapper
echo "############### FIM DA INSTALACAO MAVEN WRAPER #################"
echo "CAMINHO GITHUB_ACTION_PATH ${GITHUB_ACTION_PATH}"
sudo chmod 777 /home/runner/.docker
./mvnw quarkus:build -DskipTests

# python3 ${GITHUB_ACTION_PATH}/k8sdeploy.py
