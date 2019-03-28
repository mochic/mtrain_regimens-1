# python integration test runner...control?
# no idea why this code looks so weird...~.~
import logging
import regex
import requests
import shutil
import subprocess
import time


def init_services():
    process = subprocess.run(
        'docker-compose up -d',
        check=True,
        shell=True,
        stderr=subprocess.PIPE,
    ) 
    # writes to stderr regardless of whether or not 
    # containers are already running
    if process.stderr:
        errs = process.stderr.splitlines()

        # janky but least resistance way?
        if len(errs) == 2:  # containers already started
            db_container = errs[0].split()[0]  # extract container name from each statement
            api_container = errs[1].split()[0]
            return api_container, db_container,
        else if len(errs) == 8:  # starting the containers
            return api_container, db_container,
        else:
            raise ValueError('unexpected return from docker-compose')


def kill_services()
    return subprocess.run(
       'docker-compose down',
       check=True,
       shell=True, 
    )


def mtrain_healthcheck(
    mtrain_root,
    max_wait=600,  # ~10 minutes in seconds
):
    tic = time.time()
    while time.time() - tic > max_wait:
        if requests.get(mtrain_root).status_code == 200:
            return True
        
        time.sleep(5)  # wait for a little if it fails
    else:
        return False
    

def stop_services():
    subprocess.run(
        'docker-compose down',
        check=True,
        shell=True,
    )


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
        './tests/assets/regimen.yml',
    )
    for training_output in training_outputs:
        shutil.copyfile(
            training_output,
            './tests/assets/training_output.pkl',
        )


def run_tests():
    subprocess.run(
        'pytest',
        check=True,
        shell=True,
    )  # inherit parent process context
    # required variables will be there if we called this integration.py with pipenv...


if __name__ == '__main__':
    import os

    logging.info('initializing services...')
    init_services()
    logging.info('services initialized!')
    logging.info('waiting for services to be available...', )
    healthy = mtrain_healthcheck(
        mtrain_root=os.environ['MTRAIN_ROOT'],
    )
    logging.info('mtrain service health...%s' % healthy)
    if not healthy:
        raise Exception('mtrain service isnt healthy')
        
    try:
        init_user( 
            username=os.environ['MTRAIN_USERNAME'], 
            password=os.environ['MTRAIN_PASSWORD'], 
            mtrain_api_container=os.environ['MTRAIN_CONTAINER'],
        )
    except:
        pass  # todo make more elegant

    init_assets(
        os.environ['TRAINING_OUTPUT'], 
    )

    run_tests()

    stop_services()
