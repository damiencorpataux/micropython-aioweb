import uaioweb
from uaioweb import asyncio

app = uaioweb.App(host='0.0.0.0', port=80)

# root route handler
@app.route('/')
async def handler(r, w):
    w.write(b'HTTP/1.0 200 OK\r\n')
    w.write(b'Content-Type: text/html; charset=utf-8\r\n')
    w.write(b'\r\n')
    await w.drain()
    count = 0
    while True:
        count += 1
        w.write(bytes('<div>Hello world #{}!</div>'.format(count), encoding='utf-8'))
        try:
            await w.drain()
        except:
            break
        await asyncio.sleep(1)

# Start wifi (if applicable)
try:
    import network
    # access point credentials
    AP_SSID = 'Hello AP'
    AP_PASSWORD = 'donthackmebro'
    AP_AUTHMODE = network.AUTH_WPA_WPA2_PSK

    # Create WiFi access point
    wifi = network.WLAN(network.AP_IF)
    wifi.active(True)
    wifi.config(essid=AP_SSID, password=AP_PASSWORD, authmode=AP_AUTHMODE)
    while wifi.active() == False:
        pass
    print(wifi.ifconfig())
except ModuleNotFoundError:
    pass  # running on Python

# Start event loop and create server task
loop = asyncio.get_event_loop()
loop.create_task(app.serve())
loop.run_forever()
