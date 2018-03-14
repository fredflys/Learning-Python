import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER_HOME = '%s\\var\\users' % BASE_DIR

USER_ACCOUNT = {
    'username':
        {'password':md5,
         'storage_limit':2097152}
}
