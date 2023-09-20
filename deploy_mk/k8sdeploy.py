
# Importando uma Classe (Para tratativas com o sistema operacional)
import os
# Classe subprocess para execução de comandos no SO
import subprocess
import base64

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

# token=(os.environ['TOKEN_K8S'])
print=("TESTANDO A VARIAVEL" (os.environ['TOKEN']))

# Configuration = client.Configuration()
# Configuration.host = "https://192.168.0.50:6443"
# Configuration.verify_ssl = False
# Configuration.api_key = {"authorization": "Bearer " + Token}
# ApiClient = client.ApiClient(Configuration)


# GITHUB_WORKSPACE =  os.environ.get('GITHUB_WORKSPACE')
# FILE_DEPLOYMENT = os.environ.get('FILE_DEPLOYMENT')

# The default credential first checks environment variables for configuration as described above.
# If environment configuration is incomplete, it will try managed identity.

# from kubernetes import client, config

# # Configs can be set in Configuration class directly or using helper utility
# config.load_kube_config()

# v1 = client.CoreV1Api(ApiClient)
# print("Listing pods with their IPs:")
# ret = v1.list_pod_for_all_namespaces(watch=False)
# for i in ret.items:
#     print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


# with open(path.join(path.dirname(__file__), GITHUB_WORKSPACE + "/" + FILE_DEPLOYMENT)) as f:
#     dep = yaml.safe_load(f)
#     k8s_apps_v1 = client.AppsV1Api()
#     resp = k8s_apps_v1.create_namespaced_deployment(body=dep, namespace="default")
#     print("Deployment created. status='%s'" % resp.metadata.name)