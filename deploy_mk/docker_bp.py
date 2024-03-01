import docker
import os

client = docker.from_env()

PODNAME = os.environ.get('POD_NAME')
# WORKSPACE = os.environ.get('WORKSPACE')
# GITHUBWORKSPACE = os.environ.get('GITHUB_WORKSPACE')

# # build = client.images.build(path = GITHUBWORKSPACE, tag = '10.104.178.216/library/' + PODNAME)

client.login(registry='10.96.13.127', username='admin', password='Harbor12345')
push = client.images.push('10.96.13.127/library/' + "quarkus-social")
print(push)


