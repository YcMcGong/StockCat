from StockPool import StockPool
import time

# List of stock watch list
watch_list = ['AAPL','CLDR','PYPL','NVDA','AMZN','GOOGL','SNE','FB','ATVI','EA','JD']
buying_price = [0,0]
init_change = [0,0]

def init():
    my_stock_pool = StockPool(watch_list, buying_price, init_change)
    return my_stock_pool

def main():
    my_stock_pool = init()
    my_stock_pool.run()
        
if __name__ == "__main__":
    main()