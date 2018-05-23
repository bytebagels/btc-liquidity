
def get_volume(bids):
    """
    Get exchange volume from orderbook
    """
    volume = 0.0

    for i in range(len(bids)):
        volume +=  float(bids[i][1]) * float(bids[i][0])

    return volume

def get_volume_(asks):
    """
    Get exchange volume from orderbook
    """
    volume = 0.0

    for i in range(len(asks)):
        volume +=  float(asks[i][1]) / float(asks[i][0])

    return volume
