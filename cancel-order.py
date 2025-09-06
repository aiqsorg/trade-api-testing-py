from moomoo import *

trd_ctx = OpenSecTradeContext(host='127.0.0.1', port=11111)

print("=== Using cancel_all_order method ===")
ret, result = trd_ctx.cancel_all_order(trd_env=TrdEnv.SIMULATE)

if ret == 0:
    print("Success! All orders canceled")
    print(f"Result: {result}")
else:
    print(f"Failed to cancel orders: {result}")

# Verify cancellation worked
print("\n=== Verifying Orders Canceled ===")
ret, orders = trd_ctx.order_list_query(trd_env=TrdEnv.SIMULATE)
if ret == 0:
    print(f"Remaining orders: {len(orders)}")
    if len(orders) == 0:
        print("All orders successfully canceled!")
    else:
        print("Some orders still remain:")
        for i, order in orders.iterrows():
            print(f"  {order['code']}: {order['order_status']}")

trd_ctx.close()