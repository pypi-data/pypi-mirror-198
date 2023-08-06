from setuptools import find_packages, setup
setup(
    name='updateMondayItemLib',
    packages=find_packages(),
    version='0.1.2',
    description='Update the existing items or create new items on monday board ',
    author='Bilal Ashraf',
    license='MIT',
    long_description="This package allows you to update columns against item on monday.com board.It takes following parameters apiKey,apiUrl,board_id,item_id, **columnValuesDict. Columns ID and their values are passed as key value pair in dictionary.It also allows you to create new items on monday.com board.",
    long_description_content_type='text/markdown'
)