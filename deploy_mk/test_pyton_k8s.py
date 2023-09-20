
# Importando uma Classe (Para tratativas com o sistema operacional)
import os
# Classe subprocess para execução de comandos no SO
import subprocess

from kubeconfig import KubeConfig
conf = KubeConfig()
print(conf.view())

# Classe do Kubernetes
from kubernetes import config, client
from kubernetes.client import Configuration
from kubernetes.client.api import core_v1_api
from kubernetes.client.rest import ApiException
from kubernetes.stream import stream
import kubernetes.client

import re 
from os import path
import yaml


# GITHUB_WORKSPACE =  "/home/trinta"
# FILE_DEPLOYMENT = os.environ.get('FILE_DEPLOYMENT')

# The default credential first checks environment variables for configuration as described above.
# If environment configuration is incomplete, it will try managed identity.

from kubernetes import client, config

SECRET=os.environ["KUBE"]
# Configs can be set in Configuration class directly or using helper utility
print (SECRET)
config.load_kube_config(os.environ["KUBE"])

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


# with open(path.join(path.dirname(__file__), GITHUB_WORKSPACE + "/" + FILE_DEPLOYMENT)) as f:
#     dep = yaml.safe_load(f)
#     k8s_apps_v1 = client.AppsV1Api()
#     resp = k8s_apps_v1.create_namespaced_deployment(body=dep, namespace="default")
#     print("Deployment created. status='%s'" % resp.metadata.name)