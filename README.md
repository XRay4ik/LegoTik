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

```
**📝copy data from one file to another**
_⚠️Attention! For everything to work, you need to have 2 files! Otherwise, it will give an error: files not found!_

```python

from LegoTik import Lego

Lego.init()

Lego.copyring("firts.txt", "second.txt")

```

**🛍️compress file (ZIP)**

```python

from LegoTik import Lego

Lego.init()

Lego.zip_load("myfile.txt")

```

_💡Please note that the file extension is not required 'txt', the file can have ABSOLUTELY any extension, the main thing is that it does not create errors and conflicts between iterations_
