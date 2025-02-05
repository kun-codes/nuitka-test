import subprocess
import threading

def set_proxy(ip_address, port):
    try:
        subprocess.run([
            "setx", "http_proxy", f"http://{ip_address}:{port}/"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True, check=True)
        print("Proxy set successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Unable to set proxy environment variables: {e}")

def unset_proxy():
    try:
        subprocess.run([
            "setx", "http_proxy", ""
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True, check=True)
        print("Proxy unset successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Unable to unset proxy environment variables: {e}")

def manage_proxy(ip_address, port):
    set_proxy(ip_address, port)
    unset_proxy()

# Parameters
ip_address = "127.0.0.1"
port = 80

# Create and start a thread for managing the proxy
proxy_thread = threading.Thread(target=manage_proxy, args=(ip_address, port))
proxy_thread.start()

# Wait for the thread to finish
proxy_thread.join()
