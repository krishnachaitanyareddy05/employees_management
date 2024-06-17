from setuptools import setup, find_packages

setup(
    name='django-employee-management',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='A reusable Django app for managing employees.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/krishnachaitanyareddy05/django-employee-management',
    author='MORTHALA KRISHNA CHAITANYA REDDY',
    author_email='krishnachaitanyareddy05@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 5.0.6',  # Replace with your Django version
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'django>=3.2',
    ],
)
