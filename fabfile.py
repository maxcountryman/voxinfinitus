from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['arkham.voxinfinitus.net']

def pack():
    local('tar czf /tmp/my_project.tgz .', capture=False)

def deploy():
    put('/tmp/my_project.tgz', '/tmp/')
    with cd('/srv/django/my_project/'):
        run('tar xzf /tmp/my_project.tgz')
        run('touch app.wsgi')

