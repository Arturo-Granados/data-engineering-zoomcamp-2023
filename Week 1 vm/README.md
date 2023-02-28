# GCP VM SET UP

May be this is one of the most important part of this course, because in the following weeks we will working with this vm, so is really 
important this set up. 

## Pre-Requisites

    Have a GCP account 

    Git in the local computer

    Optional: If you are using windows, have windows subsystem for linux(WSL) will do some easier tasks.

# Now that we have the prerequisites already we can continue with the set up procces

## Step 1. SSH key generation.

    Create .ssh dir: mkdir .ssh

    Change the directory to .ssh directory: cd .ssh

    Genarate ssh key: ssh-keygen -t rsa -f <filename> -C <yourname> -b 2048

    SSH keys generation: https://cloud.google.com/compute/docs/connect/create-ssh-keys?hl=es-419

    acces to ssh key: cat gcp.pub

    copy the ssh key value and add in metadata section in gcp compute engine


## Step 2. Create a VM 

    Go to GCP console, in the section compute engine/ VM instances, clic new instance. The create a new VM with ubuntu operative sistem and 30 gb of memory.

## Step 3. Conection with local machine
    In the VM instaces tab we can found our vm runnig, well we need to copy the external IP value to conect the vm with our local machine.

    ssh -i ~/.ssh/gcp arturo@<external IP>

## Step 4. Configure VM and set up local    

    install with the command:

    wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh

    or the lasted version

    Install anaconda: https://www.anaconda.com/products/distribution

    Then go to the anaconda bash:

    bash Anaconda3-2022.10-Linux-x86_64.sh

    and accept all terms and conditions

    Create the config file in .ssh dir:

        touch config

        code config

        this file contains:
            
            1. HOST: the name of the vm 
            2. HostName: external IP (this ip chages every time that the vm is restarted)
            3. User: The name of the user in the ssh keys
            4. IdentityFile: The path where is the gcp.pub file

    














    