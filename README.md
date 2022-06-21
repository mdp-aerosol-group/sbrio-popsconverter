# SBRIO POPS converter
Instructions and scripts to extract the binary files from SBRIO version of the POPS into ```.csv``` files for subsequent processing.

## 1. Install the Software
These steps only have to be performed once. After successful install, run the scripts via step 2.

### Clone this repo

```bash
git clone git@github.com:mdp-aerosol-group/sbrio-popsconverter.git
```

### Copy the script files
Place the script files in the ```level 1/pops/``` directory. Note that PATH-TO-DIRECTORY is the sub-path to where the ```level 1``` folder resides. Note that this is any folder in your standard user directory.

```bash
cp sbrio-popsconverter/src/convert.py PATH-TO-DIRECTORY/level 1/pops/
cp sbrio-popsconverter/src/mypeaks.py PATH-TO-DIRECTORY/level 1/pops/
```

### Create a dedicated toolbox 

```bash
[user@localhost ~]$ toolbox create popsconvert -d fedora
Created container: popsconvert
Enter with: toolbox enter popsconvert
```

### Enter the toolbox

```bash
[user@localhost ~]$ toolbox enter popsconvert
⬢[user@toolbox ~]$ 
```

### Install dependencies

```bash
⬢[user@toolbox ~]$ sudo dnf install python3-pip

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.

Fedora 36 - x86_64                                                        19 MB/s |  81 MB     00:04    
Fedora 36 openh264 (From Cisco) - x86_64                                 1.7 kB/s | 2.5 kB     00:01    
Fedora Modular 36 - x86_64                                               4.0 MB/s | 2.4 MB     00:00    
Fedora 36 - x86_64 - Updates                                              14 MB/s |  18 MB     00:01    
Fedora Modular 36 - x86_64 - Updates                                     3.3 MB/s | 2.2 MB     00:00    
Dependencies resolved.
=========================================================================================================
 Package                        Architecture       Version                      Repository          Size
=========================================================================================================
Installing:
 python3-pip                    noarch             21.3.1-2.fc36                fedora             1.8 M
Installing weak dependencies:
 libxcrypt-compat               x86_64             4.4.28-1.fc36                fedora              90 k
 python3-setuptools             noarch             59.6.0-2.fc36                fedora             936 k

Transaction Summary
=========================================================================================================
Install  3 Packages

Total download size: 2.8 M
Installed size: 14 M
Is this ok [y/N]: 
```

Answer y and hit ENTER

```bash
Downloading Packages:
(1/3): libxcrypt-compat-4.4.28-1.fc36.x86_64.rpm                         307 kB/s |  90 kB     00:00    
(2/3): python3-setuptools-59.6.0-2.fc36.noarch.rpm                       3.0 MB/s | 936 kB     00:00    
(3/3): python3-pip-21.3.1-2.fc36.noarch.rpm                              5.7 MB/s | 1.8 MB     00:00    
---------------------------------------------------------------------------------------------------------
Total                                                                    5.4 MB/s | 2.8 MB     00:00     
Running transaction check
Transaction check succeeded.
Running transaction test
Transaction test succeeded.
Running transaction
  Preparing        :                                                                                 1/1 
  Installing       : python3-setuptools-59.6.0-2.fc36.noarch                                         1/3 
  Installing       : libxcrypt-compat-4.4.28-1.fc36.x86_64                                           2/3 
  Installing       : python3-pip-21.3.1-2.fc36.noarch                                                3/3 
  Running scriptlet: python3-pip-21.3.1-2.fc36.noarch                                                3/3 
  Verifying        : libxcrypt-compat-4.4.28-1.fc36.x86_64                                           1/3 
  Verifying        : python3-pip-21.3.1-2.fc36.noarch                                                2/3 
  Verifying        : python3-setuptools-59.6.0-2.fc36.noarch                                         3/3 

Installed:
  libxcrypt-compat-4.4.28-1.fc36.x86_64                  python3-pip-21.3.1-2.fc36.noarch               
  python3-setuptools-59.6.0-2.fc36.noarch               

Complete!
⬢[user@toolbox ~]$ 
```

### Navigate to the folder
```bash
⬢[user@toolbox ~]$ cd PATH-TO-DIRECTORY/level\ 1/pops/
⬢[user@toolbox pops]$ 
```

### Create a virtual environment
```bash
⬢[user@toolbox pops]$  python3 -m venv . 
```

### Activate virtual environment
```bash
⬢[user@toolbox pops]$ source bin/activate
(pops) ⬢[user@toolbox pops]$ 
```

### Install Python Dependencies
Make sure the environment is activated

```bash
(pops) ⬢[user@toolbox pops]$ pip3 install pytz Pillow numpy pandas scipy matplotlib
Collecting pytz
  Using cached pytz-2022.1-py2.py3-none-any.whl (503 kB)
Collecting Pillow
  Using cached Pillow-9.1.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
Collecting numpy
  Downloading numpy-1.22.4-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
     |████████████████████████████████| 16.8 MB 2.8 MB/s            
Collecting pandas
  Downloading pandas-1.4.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.7 MB)
     |████████████████████████████████| 11.7 MB 41.5 MB/s            
Collecting scipy
  Downloading scipy-1.8.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (42.2 MB)
     |████████████████████████████████| 42.2 MB 28.4 MB/s            
Collecting matplotlib
  Downloading matplotlib-3.5.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.9 MB)
     |████████████████████████████████| 11.9 MB 44.8 MB/s            
Collecting python-dateutil>=2.8.1
  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
     |████████████████████████████████| 247 kB 45.3 MB/s            
Collecting kiwisolver>=1.0.1
  Downloading kiwisolver-1.4.3-cp310-cp310-manylinux_2_12_x86_64.manylinux2010_x86_64.whl (1.6 MB)
     |████████████████████████████████| 1.6 MB 39.2 MB/s            
Collecting pyparsing>=2.2.1
  Using cached pyparsing-3.0.9-py3-none-any.whl (98 kB)
Collecting fonttools>=4.22.0
  Downloading fonttools-4.33.3-py3-none-any.whl (930 kB)
     |████████████████████████████████| 930 kB 29.8 MB/s            
Collecting cycler>=0.10
  Downloading cycler-0.11.0-py3-none-any.whl (6.4 kB)
Collecting packaging>=20.0
  Downloading packaging-21.3-py3-none-any.whl (40 kB)
     |████████████████████████████████| 40 kB 19.9 MB/s            
Collecting six>=1.5
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, pyparsing, pytz, python-dateutil, Pillow, packaging, numpy, kiwisolver, fonttools, cycler, scipy, pandas, matplotlib
Successfully installed Pillow-9.1.1 cycler-0.11.0 fonttools-4.33.3 kiwisolver-1.4.3 matplotlib-3.5.2 numpy-1.22.4 packaging-21.3 pandas-1.4.2 pyparsing-3.0.9 python-dateutil-2.8.2 pytz-2022.1 scipy-1.8.1 six-1.16.0
```

# 2. Running the Script
- Save the directory with files containing ```YYYYMMDD_XXX_POPS_Peak.bin``` in ```PATH-TO-DIRECTORY/level\ 1/pops/```.
- Edit the file ```convert.py``` such that mypath points to this directory.
```python
def convert():
    print('Greetings from the POPS Converter')
    mypath = '20220620/'
```
- Enter toolbox and run the converter
```bash
[user@localhost ~]$ toolbox enter popsconvert
⬢[user@toolbox ~]$ cd PATH-TO-DIRECTORY/level\ 1/pops/
⬢[user@toolbox pops]$ source bin/activate
(pops) ⬢[user@toolbox pops]$ python3 convert.py 
Greetings from the POPS Converter
20220620_049_POPS_Peak.bin
Here
20220620_048_POPS_Peak.bin
Here
(pops) ⬢[user@toolbox pops]$ 
```
- The script will print the current file it is processing
- Exit the toolbox with CTRL-D 
```bash
(pops) ⬢[user@toolbox pops]$ CTRL-D
[user@localhost ~]
```

- After the script has completed, the script will have written files ```YYYYMMDD_XXX_POPS_Peak.csv``` into the local directory. Move these files into a folder ```PATH-TO-DIRECTORY/level\ 2/pops/YYYYMMDD/```

