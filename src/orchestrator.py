import yaml
import requests
import time

def load_config(path='src/config.yaml'):
    with open(path) as f:
        return yaml.safe_load(f)

def demo(agent):
    base = f"http://{agent['host']}:{agent['api_port']}/api/v1"

    print("▶ Opening URL in VM…")
    requests.post(f"{base}/open_url", json={'url': 'https://www.google.com'})
    time.sleep(3)

    print("▶ Drawing curve in VM…")
    requests.post(f"{base}/draw_curve", json={})
    print("✅ All done! Check your VNC session for Chrome + the star-drawing.")

if __name__ == '__main__':
    cfg = load_config()
    # pick your vm-optimus-1 entry
    agent = next(a for a in cfg['agents'] if a['name']=='vm-optimus-1')
    demo(agent)
