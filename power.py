import uhubctl

hubs = uhubctl.discover_hubs()

for hub in hubs:
    print(f"Found hub: {hub}")

    for port in hub.ports:
        print(f"   Found port: {port}")