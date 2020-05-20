# The number of nook purchase price periods
PRICE_PERIOD_COUNT = 12

# Alternating 'AM' 'PM' labels
PRICE_TODS = [["AM", "PM"][i % 2] for i in range(PRICE_PERIOD_COUNT)]
PRICE_DAYS = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]
PRICE_PERIODS = [x for x in range(PRICE_PERIOD_COUNT)]

# The y range of price graphs
PRICE_Y_LIM = [0, 701]

# TEXT SIZE CONSTANTS
LABEL_SIZE = 16
