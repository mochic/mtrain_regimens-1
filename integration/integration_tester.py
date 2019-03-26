# integration test runner written in python to coordinate 
# timing and intricate stuff? lel...
# no idea why this code looks so weird...~.~
import subprocess


def init_user(
    username, 
    password, 
    mtrain_api_container,
):   
    subprocess.run(
        'docker exec {container_name} {command}'.format(
            container_name=mtrain_api_container,
            command='python init_user_script.py {username} {password}' \
                .format(
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


if __name__ == '__main__':
    import os

    try:
        init_user( 
            username=os.environ['MTRAIN_USERNAME'], 
            password=os.environ['MTRAIN_PASSWORD'], 
            mtrain_api_container=os.environ['MTRAIN_CONTAINER'],
        )
    except:
        pass  # todo make more elegant

    run_tests()
