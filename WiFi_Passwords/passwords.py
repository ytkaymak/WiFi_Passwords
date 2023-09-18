import subprocess

result = subprocess.check_output(["netsh", "wlan", "show", "profiles"]).decode("utf-8")

profiles = [line.split(":")[1].strip() for line in result.split("\n") if "All User Profile" in line]
for profile in profiles:
    wifi_info = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"]).decode("utf-8")
    
    ssid = None
    key = None
    
    for line in wifi_info.split("\n"):
        if "SSID name" in line:
            ssid = line.split(":")[1].strip()
        elif "Key Content" in line:
            key = line.split(":")[1].strip()
    
    if ssid and key:
        print(f"SSID name: {ssid}")
        print(f"Key Content: {key}\n")