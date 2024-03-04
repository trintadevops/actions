import docker
import os

client = docker.from_env()

PODNAME = os.environ.get('POD_NAME')
WORKSPACE = os.environ.get('WORKSPACE')
GITHUBWORKSPACE = os.environ.get('GITHUB_WORKSPACE')

build = client.images.build(path = GITHUBWORKSPACE, tag = 'harbor-core/library/' + PODNAME)

client.login(registry='harbor-core', username='admin', password='Harbor12345')
push = client.images.push('harbor-core/library/' + "quarkus-social")
print(push)


