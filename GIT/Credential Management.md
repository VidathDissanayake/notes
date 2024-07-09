> Vidath Dissanayake | Sri Lanka
> Links: [GIT](GIT.md)

# Linux

Download the GCM deb package from https://github.com/git-ecosystem/git-credential-manager/releases/latest

Run 
```bash
sudo dpkg -i <path-to-package>
git-credential-manager configure
git config --global credential.credentialStore secretservice
```
Then try to commit and push. It will prompt for login. Login with browser. It will remember after that.