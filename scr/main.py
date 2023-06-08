from utils.services import load_json, get_last_five_successful_operations, sort_by_date, print_info

filename = 'data/operation.json'

if __name__ == '__main__':
    last_5 = get_last_five_successful_operations(sort_by_date(load_json(filename)))
    print_info(last_5)