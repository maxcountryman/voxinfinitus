from fabric.api import *

env.hosts = ['arkham.voxinfinitus.net']
env.project_path = '/srv/python-environments/voxinfinitus'
env.socket_path = '/tmp/cherokee/'

def deploy():
    "Push local changes to server, pull changes on server, destroy our socket"
    local('git push origin master;')
    run('cd %(project_path)s/; git pull origin master;' % env, pty=True)
    refresh_socket()

def refresh_socket():
    "Refresh our socket, restart uWSGI"
    run('rm %(socket_path)s/voxi-live.sock;' % env, pty=True)

def ps_cherokee():
    run("ps -e -O rss,pcpu | grep cherokee")

def ps_wsgi():
    run("ps -e -O rss,pcpu | grep uwsgi")

