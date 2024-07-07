conda env create --prefix ./autogenenv -f environment.yml

conda create --prefix ./envs jupyterlab=3.2 matplotlib=3.5 numpy=1.21

ERRORS:
  ResolvePackageNotFound:
    - pyautogen

   Dirty solution: (removed from environment.yml)
     pip install pyautogen

ipython kernel install --user --name=autogenenv-kernel


conda activate J:\Projects\ML\AutoGen\autogenenv
NOT WORKING: conda activate autogenenv

ORIGINAL
C:\ProgramData\Anaconda3\python.exe C:\ProgramData\Anaconda3\cwp.py C:\ProgramData\Anaconda3 C:\ProgramData\Anaconda3\python.exe C:\ProgramData\Anaconda3\Scripts\jupyter-notebook-script.py "%USERPROFILE%/"


AutoGen env
python.exe C:\ProgramData\Anaconda3\cwp.py C:\ProgramData\Anaconda3 C:\ProgramData\Anaconda3\python.exe C:\ProgramData\Anaconda3\Scripts\jupyter-notebook-script.py "%USERPROFILE%/"





JUPYTER NOTEBOOK KERNELS

    Option 1: Run Jupyter server and kernel inside the conda environment

    Do something like:

        conda create -n my-conda-env         # creates new virtual env
        conda activate my-conda-env          # activate environment in terminal
        conda install jupyter                # install jupyter + notebook
        jupyter notebook                     # start server + kernel inside my-conda-env

    Jupyter will be completely installed in the conda environment. Different versions of Jupyter can be used for different conda environments, but this option might be a bit of overkill. It is enough to include the kernel in the environment, which is the component wrapping Python which runs the code. The rest of Jupyter notebook can be considered as editor or viewer and it is not necessary to install this separately for every environment and include it in every env.yml file. Therefore one of the next two options might be preferable, but this one is the simplest one and definitely fine.


    Option 2: Create special kernel for the conda environment

    Do something like:

        conda create -n my-conda-env                               # creates new virtual env
        conda activate my-conda-env                                # activate environment in terminal
        conda install ipykernel                                    # install Python kernel in new conda env
        ipython kernel install --user --name=my-conda-env-kernel   # configure Jupyter to use Python kernel

    Then run jupyter from the system installation or a different conda environment:

        conda deactivate          # this step can be omitted by using a different terminal window than before
        conda install jupyter     # optional, might be installed already in system e.g. by 'apt install jupyter' on debian-based systems
        jupyter notebook          # run jupyter from system

    Name of the kernel and the conda environment are independent from each other, but it might make sense to use a similar name.


