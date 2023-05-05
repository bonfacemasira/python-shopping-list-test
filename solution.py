import collections

thisdict = {
    "Toilex": 12,
    "Fresh fri": 7,
    "Fresh fri": 7,
    "Toilex": 12,
    "Fresh fri": 7,
    "Fresh fri": 7,
    "Keringet": 5,
    "Lentils": 10,
    "Toilex": 12,
}

def solution(data):
        count = 0
        for key, value in data.items():
            count += 1
            net_price = value*count
            print(f'{key}: Quantity is: {count} Price is: {value}')
            print(f'Net Price: {net_price}')


solution(thisdict)