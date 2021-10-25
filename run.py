import os
from app import app, io

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    io.run(app, host='0.0.0.0', port=port)