from output import directories
from output.database_base import engine, Base
from output.tools import config_files_data
from output.tools.frontend_shell import FrontendShell
from output.tools.grafana_shell import GrafanaShell
from output.tools.nginx_shell import NginxShell
from output.tools.syslog_shell import SyslogShell

if __name__ == '__main__':
    # config sample
    print(config_files_data.config_sample)
    print("************Veuillez copier-coller ce qu'il y a ci-dessus dans un fichier config.py*******************")
    # create directories
    directories.create_base_dir()
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
