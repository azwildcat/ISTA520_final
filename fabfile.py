# A script that sets up the iRODS environment on the server
# For more information, check https://pods.iplantcollaborative.org/wiki/display/start/Using+icommands
from fabric.api import *
env.user =  'jorgeorodriguez'
env.host = ['login.hpc.arizona.edu']
def setup_icommands():
    run("wget -c http://www.iplantcollaborative.org/sites/default/files/irods/icommands.x86_64.tar.bz2")
    run("bunzip2 icommands.x86_64.tar.bz2")
    run("tar -xvf icommands.x86_64.tar")
    #export PATH=~/icommands:${PATH}
    run("echo export PATH=~/icommands:'${PATH}' >> ~/.bashrc")
    # Setting up Bash autocomplete for icommands
    run("wget -c https://pods.iplantcollaborative.org/wiki/download/attachments/6720192/i-commands-auto.bash")
    run("mv i-commands-auto.bash .i-commands-auto.bash")
    run("echo source .i-commands-auto.bash >> ~/.bashrc")
    #run("")
    #run("")

def setup_sift():
    run("wget -c http://www.vlfeat.org/download/vlfeat-0.9.17-bin.tar.gz")
    run("tar -xvf vlfeat-0.9.17-bin.tar.gz")
    run("rm -f vlfeat-0.9.17-bin.tar.gz")
    
    run("cp ~/.bashrc ~/.bashrc_before_sift")
    run("echo export PATH=~/vlfeat-0.9.17/:'${PATH}' >> ~/.bashrc")
   
    # The last command throws "out: make: *** No targets specified and no makefile found.  Stop." error
    # followed by "Fatal error: run() received nonzero return code 2 while executing!
    # Requested: make
    # Executed: /bin/bash -l -c "make"  "
    #run("cd vlfeat-0.9.17")
    #run("make")
