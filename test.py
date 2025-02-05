import subprocess

ip_address = "127.0.0.1
port = 80

# setting proxy env var
try:
    subprocess.run(["setx", "http_proxy", f"http://{ip_address}:{port}/"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True, check=True)
except subprocess.CalledProcessError as e:
    raise ValueError(f"Unable to set proxy environment variables: {e}")

# unsetting proxy env var
try:
    subprocess.run(["setx", "http_proxy", ""], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True, check=True)
except subprocess.CalledProcessError as e:
    raise ValueError(f"Unable to unset proxy environment variables: {e}")
