import os

from nightshift.dashboard import serve

def main():
    root = os.environ.get("NIGHTSHIFT_ROOT", "/var/lib/night-shift")
    port = int(os.environ.get("NIGHTSHIFT_PORT", "8080"))
    serve(root, port)

if __name__ == "__main__":
    main()
