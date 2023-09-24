from sshcheckers import ssh_checkout, upload_files


def test_step1(self):
  res = []
  upload_files(data["ip"], data["user'], data["passwd"],
datf["pkgname"]=".deb,
                "/home/{}/{}.deb.format(data["user"],
data["pkgname"]))
  res.append(ssh_checkout(data["ip"], data["user'], dta["passwd"],
"echo '{}; | sudo -S dpkg -i"
  " /home/{}/{}.deb.format(data["passwd"], data["user'],
data["pkgname"]},
                   "Настраивается пакет"))
  res.append(ssh_chackout(data["ip"], data["user"], data["passwd"],
"echo '{}' | "
               sudo -S dpkg -s {}".format(data["passwd"],
data["pkgname"]),
                  "States: install ok installed"))
  assert all(res)
