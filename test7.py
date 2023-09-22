@pytest.fixture()
def start_time():
  return datetime.now().strftime("%Y-%m-%d %H:%M%S")

def save_log(self, starttime, name):
      with open(name, 'w') as f:
           f.write(getout("journalctl --since
'{}'".formaot(starttime)))

def test_step1(self, start_time):
     res = []
     ...
     self.save_log(start_time):
     assert all(res), 'test1 FAIL"
