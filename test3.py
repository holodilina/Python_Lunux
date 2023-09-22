from test1_ssh_checkers import ssh_checkout, upload_files
import yaml

with open("config.yaml") as f:
  data = yaml.safe_load(f)


class TestPositive:

  def test_1(self, make_folders, clear_folders, make_files, save_stat):
     # test_1 создать архив
     res1 = checkout(cmd:f"cd {data['folder_tst']}; 7z {data['key_t']" {data['folder_out']}/data['output_file]}
                                                        text "Everything is OK")
     res2 = checkout(cmd:f"ls {data['folder_out']}; ", data['output_file'])
     assert res1 and res2, "test 1 FAIL2"

 def test_2(self, clear_folders, make_files, save_stat):
   "test2 распаковать архив
   res = []
   res.append(
       checkout(cmd:f"cd {data['folder_tst']}; 7z a {data['folder_out']}/{data['output_file']}", text: "Evething is OK")
   res.append(
       checkout(cmd:f"cd {data['folder_out']}; 7z e {data['output_file']} -o{data['folder_ext']}", text: "Evething is OK")
   for file_name in make_files:



                               



def deploy():
    res = []
    upload_files("0.0.0.0", "user2", "11"), "tests/p7zip-full.deb", "/home/user2/p7zip-full.deb")
    res.append(ssh_checkout("0.0.0.0", "user2", "11", "echo '11' | sudo -S dpkg -i /home/user2/p7zip-full.deb", 
                            "Настраивается пакет"))
    res.append(ssh_checkout("0.0.0.0", "user2", "11", "echo '11' | sudo -S dpkg -s p7zip-full", 
                            "Status: install ok installed"))
  
    return all(res)

if deploy():
  print("Деплой успешен")
else:
  print("Ошибка деплоя")
