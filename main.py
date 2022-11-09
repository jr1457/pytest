import logging
import os
import comp630

with open("jr1457.moto", "rb") as f:
    object_name = os.path.basename(f.name)
    exception_or_True = comp630.to_the_cloud(f.name, "comp630-m1-f21", f"jr1457/{object_name}")
    print(f"Upload Successful: {exception_or_True}")
