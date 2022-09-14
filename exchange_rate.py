def exchange_rate():
    while True:
        try:
            bitcoin_to_dollar = float(input("What is Bitcoin price today? "))
            my_dollars = float(input("How much $ do you have?"))
            res = my_dollars / bitcoin_to_dollar
        except:
            print("Enter a number")
            continue
        return f"You can buy {res} BTC"


print(exchange_rate())
