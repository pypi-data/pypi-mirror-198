syslog_ng = """
############## A LIRE
# Ce fichier se trouve dans le répertoire /etc/syslog-ng
# Il inclut les autres fichiers de configurations dans le sous dossier conf.d (présent par défaut à l'installation)
#############
# Sources
source s_file {
       wildcard-file(
          base-dir("/etc/opt")
          filename-pattern("*.log")
          recursive(no)
      );
};

@include "/etc/syslog-ng/conf.d/*.conf"
"""

base = """

template-function base-function "${MSGHDR}${MSG}";

destination logs_out {
       syslog(217.182.169.116 transport("tcp") port(1514) template("$(base-function)\n"));
};

log {
  source(s_file);
  destination(logs_out);
};
"""
clients = """

source client_src {
  file("/tmp/clients.log");
};

destination clients {
  python(
        class("TopClients")
        batch-lines(1000)
    );
};

template-function base-function "${MSGHDR}${MSG}";

destination client_out {
       syslog(217.182.169.116 transport("tcp") port(1519) template("${ISODATE} $(base-function)\n"));
};



log {
  source(s_file);
  destination(clients);
};

log {
  source(client_src);
  destination(client_out);
};

python {
class TopClients(object):
    
    def init(self, options):
        self.domains_dict = {}
        return True

    def send(self, msg):
        self.message = str(msg['MESSAGE'], "utf-8")
        self.date = str(msg['ISODATE'], "utf-8")
        if 'SERVFAIL' == self.message.split(" ")[-1] or 'REFUSED' == self.message.split(" ")[-1]:
          self.domains_dict[self.message.split(" ")[2].split("#")[0]] = self.domains_dict.get(self.message.split(" ")[2].split("#")[0], 0) + 1
        return self.QUEUED

    def flush(self):
        for keys, values in self.domains_dict.items():
            self.outfile = open("/tmp/clients.log", "a")
            self.outfile.write("%s Clients: %s Nombre d'erreurs: %d \n" % (self.date, keys, values))
            self.outfile.flush()
            self.outfile.close()
        self.domains_dict = {}
        return self.SUCCESS

 };
"""

count = """

source dns_src {
  file("/tmp/dns_nb_lines.log");
};

destination history_logs_lines {
  python(
        class("NbRequest")
        batch-lines(1000)
    );
};


template-function base-function "${MSGHDR}${MSG}";

destination dns_out {
       syslog(217.182.169.116 transport("tcp") port(1520) template("${ISODATE} $(base-function)\n"));
};


log {
  source(s_file);
  destination(history_logs_lines);
};

log {
  source(dns_src);
  destination(dns_out);
};

python {
class NbRequest(object):
    def init(self, options):
        self.counter = 0
        return True

    def send(self, msg):
        self.counter +=1
        self.date = str(msg['ISODATE'], "utf-8")
        self.host = str(msg['HOST'], "utf-8")
        return self.QUEUED

    def flush(self):

        self.outfile = open("/tmp/dns_nb_lines.log", "a")
        if self.counter != 0:
          self.outfile.write("%s %s Lines %d \n" % (self.date, self.host,self.counter))
          self.outfile.flush()
          self.outfile.close()
          self.counter = 0
        return self.SUCCESS

};
"""

top_top_errors = """

source e_src {
  file("/tmp/errors.log");
};

source d_src {
  file("/tmp/domains.log");
};

source de_src {
  file("/tmp/domains_errors.log");
};

destination e_syslog {
  python(
        class("Errors")
    );
};

destination d_syslog {
  python(
        class("TopDomains")
        batch-lines(1000)
    );
};

destination de_syslog {
  python(
        class("TopDomainsWithErrors")
        batch-lines(1000)
    );
};

template-function base-function "${MSGHDR}${MSG}";

destination e_out {
       syslog(217.182.169.116 transport("tcp") port(1521) template("$(base-function)\n"));
};

destination d_out {
       syslog(217.182.169.116 transport("tcp") port(1522) template("${ISODATE} $(base-function)\n"));
};
destination de_out {
       syslog(217.182.169.116 transport("tcp") port(1523) template("${ISODATE} $(base-function)\n"));
};

log {
  source(s_file);
  destination(e_syslog);
  destination(d_syslog);
  destination(de_syslog);
};


log {
  source(e_src);
  destination(e_out);
};


log {
  source(d_src);
  destination(d_out);
};

log {
  source(de_src);
  destination(de_out);
};


python {
class Errors(object):

    def send(self, msg):
        self.message = str(msg['MESSAGE'], "utf-8")
        self.date_msg = str(msg['MSGHDR'], "utf-8")

        if 'SERVFAIL' == self.message.split(" ")[-1] or 'REFUSED' == self.message.split(" ")[-1]:
            self.log_file = open("/tmp/errors.log", "a")
            self.log_file.write("%s%s \n" % (self.date_msg, self.message))
            self.log_file.flush()
            self.log_file.close()
        return True

class TopDomains(object):
    
    def init(self, options):
        self.domains_dict = {}
        return True

    def send(self, msg):
        self.message = str(msg['MESSAGE'], "utf-8")
        self.date = str(msg['ISODATE'], "utf-8")
        self.domains_dict[self.message.split(" ")[4]] = self.domains_dict.get(self.message.split(" ")[4], 0) + 1
        return self.QUEUED

    def flush(self):
        for keys, values in self.domains_dict.items():
            self.outfile = open("/tmp/domains.log", "a")
            self.outfile.write("%s Domaine: %s Nombre de requetes: %d \n" % (self.date, keys, values))
            self.outfile.flush()
            self.outfile.close()
        self.domains_dict = {}
        return self.SUCCESS

class TopDomainsWithErrors(object):

    def init(self, options):
        self.domains_dict = {}
        return True

    def send(self, msg):
        self.message = str(msg['MESSAGE'], "utf-8")
        self.date = str(msg['ISODATE'], "utf-8")
        if 'SERVFAIL' == self.message.split(" ")[-1] or 'REFUSED' == self.message.split(" ")[-1]:
            self.domains_dict[self.message.split(" ")[4]] = self.domains_dict.get(self.message.split(" ")[4], 0) + 1
        return self.QUEUED

    def flush(self):
        for keys, values in self.domains_dict.items():
            self.outfile = open("/tmp/domains_errors.log", "a")
            self.outfile.write("%s Domaine: %s Nombre d'erreurs: %d \n" % (self.date, keys, values))
            self.outfile.flush()
            self.outfile.close()
        self.domains_dict = {}
        return self.SUCCESS

};
"""
