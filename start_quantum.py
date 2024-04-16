import subprocess
import sys

try:
    import cirq
except ImportError:
    print("installing cirq...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "cirq"])
    import cirq

    print("installed cirq.")
