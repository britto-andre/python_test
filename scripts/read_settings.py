import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv('USERNAME'))
print(os.getenv('variavel'))
print(os.getenv('ROOT_URL'))