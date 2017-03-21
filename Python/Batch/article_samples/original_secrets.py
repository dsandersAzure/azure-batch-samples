try:
    input = raw_input
except NameError:
    pass

import azure.storage.blob as azureblob
import azure.batch.batch_service_client as batch
import azure.batch.batch_auth as batchauth
import azure.batch.models as batchmodels

sys.path.append('.')
sys.path.append('..')
import common.helpers  # noqa

# Update the Batch and Storage account credential strings below with the values
# unique to your accounts. These are used when constructing connection strings
# for the Batch and Storage client objects.
secrets_file = os.environ.get('secrets_file', None)
if secrets_file is None:
    raise ValueError('The environment variable "secrets-file" was not set. The app cannot be run.')

try:
    f = open(secrets_file, 'r')
except OSError as ose:
    print('')
    print('An operating system error was returned while opening the secrets file')
    print('Error details: {0}'.format(str(ose)))
    raise

_secrets = None
try:
    _secrets = json.load(f)
except Exception as e:
    raise

f.close()

try:
    _BATCH_ACCOUNT_NAME = _secrets['batch_account_name']
    _BATCH_ACCOUNT_KEY = _secrets['batch_account_key']
    _BATCH_ACCOUNT_URL = _secrets['batch_account_url']

    _STORAGE_ACCOUNT_NAME = _secrets['storage_account_name']
    _STORAGE_ACCOUNT_KEY = _secrets['storage_account_key']
except KeyError as ke:
    print('The key {0} must be in the JSON secrets file.'.format(str(ke)))
    raise

