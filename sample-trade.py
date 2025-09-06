from moomoo import *

trd_ctx = OpenSecTradeContext(host='127.0.0.1', port=11111)
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

print("=== Current Account Balance Details ===")
ret, balance = trd_ctx.accinfo_query(trd_env=TrdEnv.SIMULATE)
if ret == 0:
    print("Key balance information:")
    try:
        print(f"  Power: {balance['power'][0]}")
        print(f"  Net Cash Power: {balance['net_cash_power'][0]}")
        print(f"  Available Cash: {balance['available_funds'][0] if 'available_funds' in balance.columns else 'N/A'}")
    except:
        print("  Full balance data:", balance.columns.tolist())

print("\n=== Place Valid Market Order (100 shares minimum) ===")
ret, price_data = quote_ctx.get_market_snapshot('HK.00700')
if ret == 0:
    current_price = float(price_data['last_price'][0])
    print(f"Current Tencent price: {current_price}")

    # Place valid order with 100 shares (1 board lot)
    print("Placing market order for 100 shares...")
    ret, market_order = trd_ctx.place_order(
        price=current_price + 2,  # Well above market price to ensure fill
        qty=100,  # Valid board lot
        code="HK.00700",
        trd_side=TrdSide.BUY,
        trd_env=TrdEnv.SIMULATE
    )
    print(f"Market order result: {market_order}")

    print("\n=== Check if Order Filled ===")
    import time

    time.sleep(2)  # Wait a moment

    ret, positions = trd_ctx.position_list_query(trd_env=TrdEnv.SIMULATE)
    if ret == 0 and len(positions) > 0:
        print("🎉 SUCCESS! You now own shares:")
        print(positions)
    else:
        print("Order still pending...")

quote_ctx.close()
trd_ctx.close()