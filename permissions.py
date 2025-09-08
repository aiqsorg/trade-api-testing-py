from moomoo import *

trd_ctx = OpenSecTradeContext(host='127.0.0.1', port=11111)

# Check what accounts/markets you have access to
ret, acc_list = trd_ctx.get_acc_list()
print(f"Account list ret: {ret}")
if ret == 0:
    print("Available accounts:")
    print(acc_list)
    print("\nLook for 'trd_market' column - should include US")

trd_ctx.close()