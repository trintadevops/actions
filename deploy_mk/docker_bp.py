import docker
import os

client = docker.from_env()

PODNAME = os.environ.get('POD_NAME')
# WORKSPACE = os.environ.get('WORKSPACE')
# GITHUBWORKSPACE = os.environ.get('GITHUB_WORKSPACE')

# # build = client.images.build(path = GITHUBWORKSPACE, tag = 'harbor-portal.harbor.svc.cluster.local/library/' + PODNAME)

client.login(registry='harbor-core.harbor.svc.cluster.local', username='admin', password='Harbor12345')
push = client.images.push('harbor-core.harbor.svc.cluster.local/library/' + "quarkus-social")
print(push)


