from moomoo import *

trd_ctx = OpenSecTradeContext(host='127.0.0.1', port=11111)

print("=== Checking Current Orders ===")
try:
    ret, current_orders = trd_ctx.order_list_query(trd_env=TrdEnv.SIMULATE)
    print(f"Current orders (ret={ret}):")
    print(current_orders)
except Exception as e:
    print(f"Error getting current orders: {e}")

print("\n=== Checking Order History ===")
try:
    ret, order_history = trd_ctx.history_order_list_query(trd_env=TrdEnv.SIMULATE)
    print(f"Order history (ret={ret}):")
    print(order_history)
except Exception as e:
    print(f"Error getting order history: {e}")

print("\n=== Account Balance ===")
try:
    ret, balance = trd_ctx.get_funds(trd_env=TrdEnv.SIMULATE)
    print(f"Account balance (ret={ret}):")
    print(balance)
except Exception as e:
    print(f"Error getting balance: {e}")

print("\n=== Current Positions ===")
try:
    ret, positions = trd_ctx.position_list_query(trd_env=TrdEnv.SIMULATE)
    print(f"Current positions (ret={ret}):")
    print(positions)
except Exception as e:
    print(f"Error getting positions: {e}")

trd_ctx.close()