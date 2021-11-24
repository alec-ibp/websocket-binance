import websocket
import json

closes, highs, lows = [], [], []


def on_message(ws: websocket.WebSocketApp, message: str):
    json_message = json.loads(message)
    candle = json_message['k']
    is_candle_closed = candle['x']
    close = candle['c']
    high = candle['h']
    low = candle['l']
    vol = candle['v']

    if is_candle_closed:
        closes.append(float(close))
        highs.append(float(high))
        lows.append(float(low))
    
        print(closes)
        print(highs)
        print(lows)


def on_close(ws: websocket.WebSocketApp):
    print('close')


if __name__ == '__main__':
    cc = 'btcusdt'
    interval = '1m'
    socket = f'wss://stream.binance.com:9443/ws/{cc}@kline_{interval}'
    ws = websocket.WebSocketApp(socket, on_message=on_message, on_close=on_close)

    ws.run_forever()
