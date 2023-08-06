import os

from production import config_files_data

if __name__ == '__main__':
    # config sample
    with(open('config.py', 'w')) as file:
        file.write(config_files_data.config_sample)
    if os.path.exists('config.py'):
        from output import directories
    # create directories
    directories.create_base_dir()
    if os.path.exists('logs') and os.path.exists('data'):
        from output.database.database_base import Base, engine
    # Base de données vide
    Base.metadata.create_all(engine)
    '''#frontend
    FrontendShell.install()
    #nginx
    NginxShell.install_nginx('network')
    #grafana
    GrafanaShell.install_grafana()
    #loki
    GrafanaShell.install_loki()
    #promtail
    GrafanaShell.install_promtail()
    #syslog
    SyslogShell.install_syslog()'''
