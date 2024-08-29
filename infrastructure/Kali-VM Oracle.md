# Kali-VM Oracle

> Vidath Dissanayake | Sri Lanka  
> Tags: #infrastructure
> Links: [Infrastructure](Infrastructure.md)
> Sources:

Create a VM with Ubuntu Minimal.

Change `/etc/apt/sources.list` to [my source.list file](https://raw.githubusercontent.com/VidathD/kali-setup/main/files/etc/apt/sources.list). Note that this is configured to use **Kali-Last-Snapshot** repos. 

You can do this by,
```bash
# change to /etc/apt directory
cd /etc/apt
# make a backup of current sources.list file
sudo mv souces.list sources.list.bak
# download the new file
sudo wget https://raw.githubusercontent.com/VidathD/kali-setup/main/files/etc/apt/sources.list -O sources.list
```

Download and install the Kali Keyrings.

```bash
# change to home directory
cd ~
# make Downloads directory
mkdir Downloads
# change to Downloads directory
cd Downloads
# Download keyring. change {YEAR} to current year. 
wget https://http.kali.org/kali/pool/main/k/kali-archive-keyring/kali-archive-keyring_{YEAR}.1_all.deb
# install keyring. #agin, replace {YEAR}
sudo apt install ./kali-archive-keyring_{YEAR}.1_all.deb
```

Update sources with `sudo apt update`.

Run `sudo apt full-upgrade`

If it fails, hold the conflicting packages with `sudo apt mark hold {PACKAGE}S`