import os.path

project_path = os.path.dirname(os.path.abspath(__file__))
apis_path = os.path.join(project_path, 'apis')
datas_path = os.path.join(project_path, 'datas')
logs_path = os.path.join(project_path, 'logs')
reporters_path = os.path.join(project_path, 'reporters')
reporters_html_path = os.path.join(reporters_path, 'html')
reporters_temp_path = os.path.join(reporters_path, 'temp')
test_cases_path = os.path.join(project_path, 'test_cases')
utils_path = os.path.join(project_path, 'utils')

if __name__ == '__main__':
    print(project_path)