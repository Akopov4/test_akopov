import yaml
import os

file = f'{os.path.dirname(os.path.abspath(__file__))}/config/configs.yaml'
request_data = f'{os.path.dirname(os.path.abspath(__file__))}/tests/api_tests/data/data.yaml'
with open(file, 'r') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

EMAIL = config['email']
PASSWORD = config['password']
LOG_IN_PAGE = config['log_in_page']
UNICORNS_ENDPOINT = config['unicorns_end_point']


with open(request_data,'r') as rd:
    data = yaml.load(rd, Loader=yaml.FullLoader)

POST_BODY = data['post_body']
UPDATE_BODY = data['update_body']