#using pathlib
from pathlib import Path

file_name = Path("file.txt")
if file_name.exists():
    print("exists") 
else:
    print("does not exist") 