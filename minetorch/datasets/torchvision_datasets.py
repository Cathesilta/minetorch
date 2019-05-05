from minetorch import dataset, option
from torchvision import datasets

@dataset('Torchvision MNIST')
@option('fold', help='Absolute fold path to the dataset')
@option('download', help='Whether to download automatcally, defaults True', type='boolean')
def mnist(fold, download):
    return datasets.MNIST(fold, download=True)