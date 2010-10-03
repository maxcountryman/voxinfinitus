from fabric.api import *

env.hosts = ['arkham.voxinfinitus.net']
env.project_path = '/srv/python-environments/voxinfinitus'
env.staging_path = '/home/max/voxinfintius'
env.socket_path = '/tmp/cherokee'
env.memcached_path ='/etc/rc.d/memcached' #this should be the init

def deploy():
    "Push local changes to GitHub, pull changes on server, destroy our socket"
    local('git push origin master;')
    run('cd %(project_path)s/; git pull origin master;' % env, pty=True)
    refresh_settings()
    refresh_socket()

def staging():
    "Pull changes from GitHub to the staging server"
    run('cd %(staging_path)s/; git pull origin master;' % env, pty=True)

def refresh_settings():
    "Use scp to update our settings.py"
#    local('scp settings.py %(hosts)s:%(project_path)s/settings.py' % env)

def refresh_socket():
    "Refresh our socket, restart uWSGI"
    run('sudo rm %(socket_path)s/voxi-live.sock' % env, pty=True)

def restart_memcached():
    "Restart Memcached"
    run('sudo %(memcached_path)s restart' % env, pty=True)

def pip_requirements():
    "Install requirements.txt"
    run('pip -E voxinfinitus install -r %(project_path)s/requirements.txt' % env, pty=True)

def ps_cherokee():
    run("ps -e -O rss,pcpu | grep cherokee")

def ps_memcahced():
    run("ps -e -O rss,pcpu | grep memcached")

def ps_wsgi():
    run("ps -e -O rss,pcpu | grep uwsgi")

