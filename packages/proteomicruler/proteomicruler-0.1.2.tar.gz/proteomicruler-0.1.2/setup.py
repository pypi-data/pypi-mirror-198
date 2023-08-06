# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['proteomicruler']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.4.3,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'scipy>=1.9.0,<2.0.0',
 'seaborn>=0.11.2,<0.12.0',
 'uniprotparser>=1.0.7,<2.0.0']

setup_kwargs = {
    'name': 'proteomicruler',
    'version': '0.1.2',
    'description': 'Estimate copy number from deep profile MS experiment using the Proteomic Ruler algorithm from Wiśniewski, J. R., Hein, M. Y., Cox, J. and Mann, M. (2014) A “Proteomic Ruler” for Protein Copy Number and Concentration Estimation without Spike-in Standards. Mol Cell Proteomics 13, 3497–3506.',
    'long_description': 'Proteomic Ruler\n--\n\nAn implementation of the same algorithm from Perseus `Wiśniewski, J. R., Hein, M. Y., Cox, J. and Mann, M. (2014) A “Proteomic Ruler” for Protein Copy Number and Concentration Estimation without Spike-in Standards. Mol Cell Proteomics 13, 3497–3506.` used for estimation of protein copy number from deep profile experiment.\n\nRequirements\n--\n\nPython >= 3.9\n\nInstallation\n--\n```bash\npip install proteomicruler\n```\n\nUsage\n--\n\nIn order to use the package, it is required that the input data is loaded into a `pandas.DataFrame` object. The following\nbasic parameters are also required:\n- `accession_id_col` - column name that contains protein accession ids\n- `mw_col` - column name that contains molecular weight of proteins\n- `ploidy` - ploidy number\n- `total_cellular_protein_concentration` - total cellular protein concentration used for calculation of total volume\n- `intensity_columns` - list of column names that contain sample intensities\n\n```python\nimport pandas as pd\n\naccession_id_col = "Protein IDs"\n# used as unique index and to directly fetch mw data from UniProt\n\nmw_col = "Mass"\n# molecular weight column name\n\nploidy = 2\n# ploidy number\n\ntotal_cellular_protein_concentration = 200\n# cellular protein concentration used for calculation of total volume\n\nfilename = r"example_data\\example_data.tsv" # example data from Perseus\ndf = pd.read_csv(filename, sep="\\t")\n\n# selecting intensity columns\nintensity_columns = df.columns[57:57+16] # select 16 columns starting from column 57th that contain sample intensity\n\n\n\n```\n\nIf the data does not contain molecular weight information, it is required to fetch it from UniProt.\n\n```python\nfrom proteomicRuler.ruler import add_mw\n\ndf = add_mw(df, accession_id_col)\ndf = df[pd.notnull(df[mw_col])]\ndf[mw_col] = df[mw_col].astype(float)\n```\n\nThe RuleR object can be created by passing the `DataFrame` object and the required parameters.\n\n```python\nfrom proteomicRuler.ruler import Ruler\n\nruler = Ruler(df, intensity_columns, mw_col, accession_id_col, ploidy, total_cellular_protein_concentration) #\nruler.df.to_csv("output.txt", sep="\\t", index=False)\n```\n',
    'author': 'Toan K. Phung',
    'author_email': 'toan.phungkhoiquoctoan@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/noatgnu/proteomicRuler',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
