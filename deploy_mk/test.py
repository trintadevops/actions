# Copyright 2018 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This example demonstrates the communication between a remote cluster and a
server outside the cluster without kube client installed on it.
The communication is secured with the use of Bearer token.
"""

from kubernetes import client, config


def main():
    # Define the bearer token we are going to use to authenticate.
    # See here to create the token:
    # https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/
    aToken = "eyJhbGciOiJSUzI1NiIsImtpZCI6IktEMURhWUVYWm1ELVZHM3VSRmlWYURiZW9vaUpieTZXVUNfYjNhaFhtUDQifQ.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJrdWJlLXN5c3RlbSIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VjcmV0Lm5hbWUiOiJhZG1pbi11c2VyLXNhLXRva2VuIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZXJ2aWNlLWFjY291bnQubmFtZSI6ImFkbWluLXVzZXIiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC51aWQiOiIwYTAyZTdmNS02NmJmLTRiYzItYmY1NS0xZWE3ZTFjMWMzNTYiLCJzdWIiOiJzeXN0ZW06c2VydmljZWFjY291bnQ6a3ViZS1zeXN0ZW06YWRtaW4tdXNlciJ9.aIUsXZS0uQGF_Jq0v8Z1Kb-0bBLk0_FBaFipMMmda4UU77wdMCsnUI4XVnbrTqo8PqCD1TSm3i_W-siBU8IqqQe_AyTKKk6PN_h3Nzos0VwI2blCCSnw64-aluu-QQSv4qAw0AY9FZCb779NlCprGdeDzCzMtZn4eygOGPiEgBjam0Xu4nJKdM9m7EVfKCHuqEovnD4VvnKJNNMyqxvx_P36wWfQ1eTGRtN87vTc-UH1uKVu68hBfzzAgV08UMVfFwveUmcyACOLOH-6GHcRuToGTsJ3X5uV2YVHSVInWwgzQ1IMbsKqEMuNRAqJB0isttLAAZHJIsec80dSi-M4UA"

    # Create a configuration object
    aConfiguration = client.Configuration()

    # Specify the endpoint of your Kube cluster
    aConfiguration.host = "https://192.168.0.50:6443"

    # Security part.
    # In this simple example we are not going to verify the SSL certificate of
    # the remote cluster (for simplicity reason)
    aConfiguration.verify_ssl = False
    # Nevertheless if you want to do it you can with these 2 parameters
    # configuration.verify_ssl=True
    # ssl_ca_cert is the filepath to the file that contains the certificate.
    # configuration.ssl_ca_cert="certificate"

    aConfiguration.api_key = {"authorization": "Bearer " + aToken}

    # Create a ApiClient with our config
    aApiClient = client.ApiClient(aConfiguration)

    # Do calls
    v1 = client.CoreV1Api(aApiClient)
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print(f"{i.status.pod_ip}\t{i.metadata.namespace}\t{i.metadata.name}")


if __name__ == '__main__':
    main()
    main()