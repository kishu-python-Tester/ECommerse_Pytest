import configparser


def get_credentials(file_path='config/config.ini'):
    config = configparser.ConfigParser()
    config.read(file_path)

    # Assuming the credentials are under the [Credentials] section
    username = config.get('Credentials', 'username')
    password = config.get('Credentials', 'password')

    return username, password
