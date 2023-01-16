
from env import *
if environment == "kaggle":
    from custom_config_kaggle import *
elif environment == "colab":
    from custom_config_colab import *
elif environment == "local":
    from custom_config_local import *
