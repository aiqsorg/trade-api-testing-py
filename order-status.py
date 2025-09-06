from moomoo import *

trd_ctx = OpenSecTradeContext(host='127.0.0.1', port=11111)

print("=== Checking Current Orders ===")
try:
    ret, current_orders = trd_ctx.order_list_query(trd_env=TrdEnv.SIMULATE)
    print(f"Current orders (ret={ret}):")
    print(f"Total orders: {len(current_orders)}")

    if len(current_orders) > 0:
        # Show specific columns instead of the entire DataFrame
        for i, order in current_orders.iterrows():
            print(
                f"Order {i + 1}: Status={order['order_status']}, Code={order['code']}, Qty={order['qty']}, Price={order['price']}")
    else:
        print("No orders found")

except Exception as e:
    print(f"Error getting current orders: {e}")

print("\n=== Account Balance ===")
try:
    ret, balance = trd_ctx.accinfo_query(trd_env=TrdEnv.SIMULATE)  # Fixed method name
    print(f"Cash: {balance['cash'][0]}")
    print(f"Total Assets: {balance['total_assets'][0]}")
except Exception as e:
    print(f"Error getting balance: {e}")

trd_ctx.close()