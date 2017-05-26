from StockPool import StockPool
import time

# List of stock watch list
watch_list = ['AAPL','CLDR','PYPL','NVDA','AMZN','GOOGL','SNE','FB','ATVI','EA','JD']
private_list =  {
    'yicong_private': ['AAPL','CLDR','PYPL'],
    'stockcat_test_channel':['NVDA','AMZN','GOOGL']
}
buying_price = [0,0]
init_change = [0,0]

def init():
    my_stock_pool = StockPool(watch_list, buying_price, init_change, private_list)
    return my_stock_pool

def main():
    my_stock_pool = init()
    my_stock_pool.run()
        
if __name__ == "__main__":
    main()