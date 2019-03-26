# integration test runner written in python to coordinate 
# timing and intricate stuff? lel...
# no idea why this code looks so weird...~.~
import os
import shutil
import subprocess
from tempfile import mkstemp


def init():
    # make a copy of the regimen for the tests
    _, regimen_yml = mkstemp(
        suffix='.yml',
        dir='./assets',
    )
    
    with open('../regimen.yml', 'r') as src, \
            open(regimen_yml, 'w') as dest:
        dest.write(src.read())

    return {
        'regimen_yml': regimen_yml, 
    }


def init_user(
    username, 
    password, 
    mtrain_api_container,
):
    _, vector_script, = mkstemp(
        suffix='.py',
        dir='./assets',
    )

    with open(vector_script, 'w') as fstream:
        fstream.write(
            INIT_USER_SCRIPT_TEMPLATE.format(
                username=username,
                password=password,
            )
        )
     
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


meta = init()

init_user( 
    username=os.environ['MTRAIN_USERNAME'], 
    password=os.environ['MTRAIN_PASSWORD'], 
    mtrain_api_container=os.environ['MTRAIN_CONTAINER'],
)

# so we know where the regimen file is
os.environ['MTRAIN_REGIMEN_YML'] = meta['regimen_yml']

run_tests()
