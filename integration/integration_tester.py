# integration test runner written in python to coordinate 
# timing and intricate stuff? lel...
# no idea why this code looks so weird...~.~
import os
import subprocess


def init_regimen(mtrain_api_container):
    subprocess.run(
        'docker cp ../regimen.yml %s:/home/mtrain/app/mtrain_api' % \
            mtrain_api_container,
        check=True,
        shell=True,
    )


def init_user(
    username, 
    password, 
    mtrain_api_container,
):   
    subprocess.run(
        'docker cp {src} {dest}'.format(
            src='init_user_script.py',
            dest='%s:/home/mtrain/app/mtrain_api' % \
                mtrain_api_container,
        ),
        check=True,
        shell=True,
    )

    subprocess.run(
        'docker exec {container_name} {command}'.format(
            container_name=mtrain_api_container,
            command='python {script} {username} {password}' \
                .format(
                    script='init_user_script.py',
                    username=username,
                    password=password,
                ),
        ),
        check=True,
        shell=True,
    )


def run_tests():
    subprocess.run(
        'pytest ./mtrain_regimens_tests',
        check=True,
        shell=True,
    )  # inherit parent process context


init_regimen(
    mtrain_api_container=os.environ['MTRAIN_CONTAINER'],
)

try:
    init_user( 
        username=os.environ['MTRAIN_USERNAME'], 
        password=os.environ['MTRAIN_PASSWORD'], 
        mtrain_api_container=os.environ['MTRAIN_CONTAINER'],
    )
except:
    pass  # todo make more elegant

run_tests()
