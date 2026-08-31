#Python program to convert USD into INR using functions.
def converter(usd_val):
    inr_val = usd_val * 95.16
    print(usd_val, "USD =", inr_val, "INR")
converter(1)    
converter(50)
converter(100)
