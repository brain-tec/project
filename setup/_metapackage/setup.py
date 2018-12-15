import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-project",
    description="Meta package for oca-project Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-project_description',
        'odoo12-addon-project_key',
        'odoo12-addon-project_role',
        'odoo12-addon-project_task_add_very_high',
        'odoo12-addon-project_task_code',
        'odoo12-addon-project_task_default_stage',
        'odoo12-addon-project_task_material',
        'odoo12-addon-project_task_pull_request',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
