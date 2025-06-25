import subprocess
import os
import re
FLAG_PATH = "/ctf/flag.txt"
if not os.path.exists(FLAG_PATH):
    os.makedirs(os.path.dirname(FLAG_PATH), exist_ok=True)
    with open(FLAG_PATH, "w") as f:
        f.write("ACTF{c0mm@Nd_1nj3c710n}")

def check_waf(input_str: str) -> None:
    forbidden = r"[;|&&$()]"
    forbidden2 = r"(rm -rf /|format|mkfs|dd if=/dev/zero|rm|mv)"
    if re.search(forbidden, input_str):
        raise ValueError("WAF ALERT! Не пытайся взломать меня больше...")
    if re.search(forbidden2, input_str):
        raise ValueError("WAF ALERT! Пожалуйста! Не разрушай всё вокруг...")
def run_ping_command(host: str) -> str:
    check_waf(host)
    command = f"ping -c 2 -W 1 -w 2 {host}"
    try:
        result = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT, timeout=5)
        return result
    except subprocess.TimeoutExpired:
        return "Ping timed out after 5 seconds."
    except subprocess.CalledProcessError as e:
        return e.output