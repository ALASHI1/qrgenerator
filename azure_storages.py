from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    location = 'media'
    file_overwrite = False

class AzureStaticStorage(AzureStorage):
    account_name = 'qrstoragebenshi' # Must be replaced by your storage_account_name
    account_key = 'u4r5AdcdBGI8DThRQZc7zfM8ndgPGQSqTwwM79G28rQI5hh3TDg4rO4vmrJPvAROlUCHuYn5Gy+0+AStORZMnA==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    container_name = 'static'
    expiration_secs = None