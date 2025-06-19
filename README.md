# 📦 LegoTik

**LegoTik** is a simple and powerful Python library that allows you to:

- Work with files;
- Connect to FTP servers;
- Download content via URL;
- Log system events;
- Compress files into ZIP;
- Manage arrays and directories.

---

**📓licence**:
  {MIT}
**dependencies**:
  _pip install colorama_

  
## 🚀 Quick Start

```python
from LegoTik import Lego

Lego.init()  # Required before using other functions

Lego.add("starting.txt", "hello!")  # Create a file and write data

Lego.read_log()  # Read logs (you can pass True to clear logs)

