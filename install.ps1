$packs = @('prettytable', 'matplotlib', 'numpy', 'inquirer', 'scipy', 'sympy')
$packs | ForEach-Object { pip install $PSItem }

<# Requirements
    prettytable==3.9.0
    matplotlib==3.8.2
    numpy==1.26.3
    inquirer==3.2.1
    icecream==2.1.3
    scipy==1.12.0
#>
