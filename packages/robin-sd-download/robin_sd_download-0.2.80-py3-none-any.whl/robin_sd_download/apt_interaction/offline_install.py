# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import subprocess


def install_sshpass():
    try:
        subprocess.run(["sshpass", "-V"], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("sshpass is already installed.")
    except subprocess.CalledProcessError:
        print("sshpass not found. Attempting to install...")
        try:
            if sys.platform.startswith("linux"):
                subprocess.run(["sudo", "apt-get", "update"], check=True)
                subprocess.run(["sudo", "apt-get", "install",
                               "-y", "sshpass"], check=True)
                print("sshpass installed successfully.")
            else:
                print(
                    "Unsupported platform for sshpass installation. Please install sshpass manually.")
                return
        except subprocess.CalledProcessError as e:
            print(f"Error during sshpass installation: {e}")
            return


def get_remote_ip():
    try:
        detected_ip = subprocess.check_output(
            ['hostname', '-I']).decode('utf-8').strip()
    except subprocess.CalledProcessError:
        detected_ip = None

    if detected_ip:
        user_confirmation = input(
            f"Detected target IP address is {detected_ip}. Is this correct? (yes/no): ").strip().lower()
        if user_confirmation == 'yes':
            return detected_ip

    remote_ip = input("Please enter the IP address of the target device: ")
    return remote_ip


def offline_install():
    """Installs the software on the remote machine.

    Returns:
        bool: True if the software was successfully installed, False otherwise.
    """
    # # Try to find remote IP of target device, or prompt user to enter it
    # remote_ip = get_remote_ip()

    # # Prompt user to enter username for remote device
    # remote_username = input(
    #     "Please enter the username for the target device: ")

    # # prompt user to enter pass for remote device
    # remote_pass = input(
    #     "Please enter the password for the target device: ")

    # # Check if sshpass is installed (install this , when downloading the robin_sd_download package -> sudo apt-get install sshpass)
    # install_sshpass()

    # # Copy generated zip file in download folder to remote system
    # subprocess.run(['sudo', 'sshpass', '-p', remote_pass, 'scp', '-o', 'StrictHostKeyChecking=no', '-o',
    #                'UserKnownHostsFile=/dev/null', zipfile_path, f'{remote_username}@{remote_ip}:/home/{remote_username}/'], check=True)

    # Unzip the file

    # Make backups

    # Should We Run an Update?

    # Run selected options...

    # Running Cleanup
