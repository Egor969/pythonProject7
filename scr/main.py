import utils
from os import path


text = path.join('..', 'scr', 'operations.json')
date = utils.open_file(text)
date = utils.chek_state_and_sorted(date)

for i in utils.output_last_operations(date):
    print(i)
