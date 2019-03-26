# python integration test runner...control?
# no idea why this code looks so weird...~.~
import logging
import requests
import shutil
import subprocess
import time


def init_services(mtrain_root):
    daemon = subprocess.Popen(
        ['docker-compose', 'up', ], 
    )
    logging.info('waiting for services to be available...', )
    tic = time.time()
    while time.time() - tic > 600:  # ~10 minutes max wait time
        if requests.get(mtrain_root) \
                .status_code == 200:
            break

        time.sleep(5)


def init_user(
    username, 
    password, 
    mtrain_api_container,
):
    subprocess.run(
        'docker exec {container_name} {command}'.format(
            container_name=mtrain_api_container,
            command='python ./scripts/init_user_script.py {username} {password}' \
                .format(
                    username=username,
                    password=password,
                ),
        ),
        check=True,
        shell=True,
    )


def init_assets(*training_outputs):
    shutil.copyfile(
        '../regimen.yml', 
        './mtrain_regimens_tests/assets/regimen.yml',
    )
    for training_outputs in training_outputs:
        shutil.copyfile(
            training_output,
            './mtrain_regimens_tests/assets/training_output.pkl'
        )


def run_tests():
    subprocess.run(
        'pytest ./mtrain_regimens_tests',
        check=True,
        shell=True,
    )  # inherit parent process context


if __name__ == '__main__':
    import os

    init_services(
        mtrain_root=os.environ['MTRAIN_ROOT'],
    )

    try:
        init_user( 
            username=os.environ['MTRAIN_USERNAME'], 
            password=os.environ['MTRAIN_PASSWORD'], 
            mtrain_api_container=os.environ['MTRAIN_CONTAINER'],
        )
    except:
        pass  # todo make more elegant

    init_assets(os.environ['TRAINING_OUTPUT'], )

    run_tests()
