import threading
import time
import uvicorn
from app import app

def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8000)

# Start server in a separate thread
server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()

# Wait until server is up
import requests
for i in range(20):
    try:
        requests.get("http://127.0.0.1:8000/chat?query=ping")
        print("Server is up!")
        break
    except:
        time.sleep(1)
else:
    print("Server failed to start in time.")
    exit(1)

# Keep main thread alive so server stays running
server_thread.join()
