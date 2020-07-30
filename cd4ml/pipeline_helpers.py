from cd4ml.download_data import run_download_data
from cd4ml.get_problem import get_problem


def download_data(problem_name):
    print('Downloading data')
    problem = get_problem(problem_name)
    run_download_data(problem.pipeline_params)
    print('Done downloading data')


def train_and_validate_model(problem_name):
    print('Training and validating model')
    problem = get_problem(problem_name)
    problem.run_all()
    print('Done training and validating model')
