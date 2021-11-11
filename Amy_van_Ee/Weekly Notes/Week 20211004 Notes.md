# Weekly Notes: 2021-10-04

- https://github.com/numpy/numpy/issues/12016
- still issues with installing ProgLearn it seems?

PS C:\Users\Amy\Documents\Python\Neuro Data Design\ProgLearn> pip install -r requirements.txt
Requirement already satisfied: keras>=2.3.1 in c:\users\amy\appdata\local\programs\python\python39\lib\site-packages (from -r requirements.txt (line 1)) (2.6.0)
Requirement already satisfied: tensorflow>=1.19.0 in c:\users\amy\appdata\local\programs\python\python39\lib\site-packages (from -r requirements.txt (line 2)) (2.6.0)
Requirement already satisfied: scikit-learn>=0.22.0 in c:\users\amy\appdata\local\programs\python\python39\lib\site-packages (from -r requirements.txt (line 3)) (1.0)
Collecting scipy==1.4.1
  Using cached scipy-1.4.1.tar.gz (24.6 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
    Preparing wheel metadata ... error
    ERROR: Command errored out with exit status 1:
     command: 'C:\Users\Amy\AppData\Local\Programs\Python\Python39\python.exe' 'C:\Users\Amy\AppData\Local\Programs\Python\Python39\lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py' prepare_metadata_for_build_wheel 'C:\Users\Amy\AppData\Local\Temp\tmpe7qtz4x_'
         cwd: C:\Users\Amy\AppData\Local\Temp\pip-install-3ea1zm_y\scipy_b0b8fdfafcbb4a34887258bed58de37a
    Complete output (195 lines):
    setup.py:418: UserWarning: Unrecognized setuptools command ('dist_info --egg-base C:\Users\Amy\AppData\Local\Temp\pip-modern-metadata-8assu1ok'), proceeding with generating Cython sources and expanding templates     
      warnings.warn("Unrecognized setuptools command ('{}'), proceeding with "
    Running from scipy source directory.
    lapack_opt_info:
    lapack_mkl_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries mkl_rt not found in ['C:\\Users\\Amy\\AppData\\Local\\Programs\\Python\\Python39\\lib', 'C:\\', 'C:\\Users\\Amy\\AppData\\Local\\Programs\\Python\\Python39\\libs']
      NOT AVAILABLE

    openblas_lapack_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries openblas not found in ['C:\\Users\\Amy\\AppData\\Local\\Programs\\Python\\Python39\\lib', 'C:\\', 'C:\\Users\\Amy\\AppData\\Local\\Programs\\Python\\Python39\\libs']
    get_default_fcompiler: matching types: '['gnu', 'intelv', 'absoft', 'compaqv', 'intelev', 'gnu95', 'g95', 'intelvem', 'intelem', 'flang']'
    customize GnuFCompiler
    Could not locate executable g77
    Could not locate executable f77
    customize IntelVisualFCompiler
    Could not locate executable ifort
    Could not locate executable ifl
    customize AbsoftFCompiler
    Could not locate executable f90
    customize CompaqVisualFCompiler
    Could not locate executable DF
    customize IntelItaniumVisualFCompiler
    Could not locate executable efl
    customize Gnu95FCompiler
    Could not locate executable gfortran
    Could not locate executable f95
    customize G95FCompiler
    Could not locate executable g95
    customize IntelEM64VisualFCompiler
    customize IntelEM64TFCompiler
    Could not locate executable efort
    Could not locate executable efc
    customize PGroupFlangCompiler
    Could not locate executable flang
    don't know how to compile Fortran code on platform 'nt'
      NOT AVAILABLE

    openblas_clapack_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries openblas,lapack not found in ['C:\\Users\\Amy\\AppData\\Local\\Programs\\Python\\Python39\\lib', 'C:\\', 'C:\\Users\\Amy\\AppData\\Local\\Programs\\Python\\Python39\\libs']
      NOT AVAILABLE

    flame_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries flame not found in ['C:\\Users\\Amy\\AppData\\Local\\Programs\\Python\\Python39\\lib', 'C:\\', 'C:\\Users\\Amy\\AppData\\Local\\Programs\\Python\\Python39\\libs']
      NOT AVAILABLE

    atlas_3_10_threads_info:
    Setting PTATLAS=ATLAS
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in C:\Users\Amy\AppData\Local\Programs\Python\Python39\lib
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries tatlas,tatlas not found in C:\Users\Amy\AppData\Local\Programs\Python\Python39\lib
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in C:\
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries tatlas,tatlas not found in C:\
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in C:\Users\Amy\AppData\Local\Programs\Python\Python39\libs
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries tatlas,tatlas not found in C:\Users\Amy\AppData\Local\Programs\Python\Python39\libs
    <class 'numpy.distutils.system_info.atlas_3_10_threads_info'>
      NOT AVAILABLE

    atlas_3_10_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in C:\Users\Amy\AppData\Local\Programs\Python\Python39\lib
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries satlas,satlas not found in C:\Users\Amy\AppData\Local\Programs\Python\Python39\lib
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in C:\
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries satlas,satlas not found in C:\
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in C:\Users\Amy\AppData\Local\Programs\Python\Python39\libs
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries satlas,satlas not found in C:\Users\Amy\AppData\Local\Programs\Python\Python39\libs
    <class 'numpy.distutils.system_info.atlas_3_10_info'>
      NOT AVAILABLE

    atlas_threads_info:
    Setting PTATLAS=ATLAS
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in C:\Users\Amy\AppData\Local\Programs\Python\Python39\lib
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries ptf77blas,ptcblas,atlas not found in C:\Users\Amy\AppData\Local\Programs\Python\Python39\lib
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in C:\
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries ptf77blas,ptcblas,atlas not found in C:\
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in C:\Users\Amy\AppData\Local\Programs\Python\Python39\libs
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries ptf77blas,ptcblas,atlas not found in C:\Users\Amy\AppData\Local\Programs\Python\Python39\libs
    <class 'numpy.distutils.system_info.atlas_threads_info'>
      NOT AVAILABLE

    atlas_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in C:\Users\Amy\AppData\Local\Programs\Python\Python39\lib
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries f77blas,cblas,atlas not found in C:\Users\Amy\AppData\Local\Programs\Python\Python39\lib
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in C:\
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries f77blas,cblas,atlas not found in C:\
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack_atlas not found in C:\Users\Amy\AppData\Local\Programs\Python\Python39\libs
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries f77blas,cblas,atlas not found in C:\Users\Amy\AppData\Local\Programs\Python\Python39\libs
    <class 'numpy.distutils.system_info.atlas_info'>
      NOT AVAILABLE

    accelerate_info:
      NOT AVAILABLE

    lapack_info:
    No module named 'numpy.distutils._msvccompiler' in numpy.distutils; trying from distutils
    customize MSVCCompiler
      libraries lapack not found in ['C:\\Users\\Amy\\AppData\\Local\\Programs\\Python\\Python39\\lib', 'C:\\', 'C:\\Users\\Amy\\AppData\\Local\\Programs\\Python\\Python39\\libs']
      NOT AVAILABLE

    C:\Users\Amy\AppData\Local\Temp\pip-build-env-s15gckug\overlay\Lib\site-packages\numpy\distutils\system_info.py:1712: UserWarning:
        Lapack (http://www.netlib.org/lapack/) libraries not found.
        Directories to search for the libraries can be specified in the
        numpy/distutils/site.cfg file (section [lapack]) or by setting
        the LAPACK environment variable.
      if getattr(self, '_calc_info_{}'.format(lapack))():
    lapack_src_info:
      NOT AVAILABLE

    C:\Users\Amy\AppData\Local\Temp\pip-build-env-s15gckug\overlay\Lib\site-packages\numpy\distutils\system_info.py:1712: UserWarning:
        Lapack (http://www.netlib.org/lapack/) sources not found.
        Directories to search for the sources can be specified in the
        numpy/distutils/site.cfg file (section [lapack_src]) or by setting
        the LAPACK_SRC environment variable.
      if getattr(self, '_calc_info_{}'.format(lapack))():
      NOT AVAILABLE

    Traceback (most recent call last):
      File "C:\Users\Amy\AppData\Local\Programs\Python\Python39\lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py", line 349, in <module>
        main()
      File "C:\Users\Amy\AppData\Local\Programs\Python\Python39\lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py", line 331, in main
        json_out['return_val'] = hook(**hook_input['kwargs'])
      File "C:\Users\Amy\AppData\Local\Programs\Python\Python39\lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py", line 151, in prepare_metadata_for_build_wheel
        return hook(metadata_directory, config_settings)
      File "C:\Users\Amy\AppData\Local\Temp\pip-build-env-s15gckug\overlay\Lib\site-packages\setuptools\build_meta.py", line 166, in prepare_metadata_for_build_wheel
        self.run_setup()
      File "C:\Users\Amy\AppData\Local\Temp\pip-build-env-s15gckug\overlay\Lib\site-packages\setuptools\build_meta.py", line 258, in run_setup
        super(_BuildMetaLegacyBackend,
      File "C:\Users\Amy\AppData\Local\Temp\pip-build-env-s15gckug\overlay\Lib\site-packages\setuptools\build_meta.py", line 150, in run_setup
        exec(compile(code, __file__, 'exec'), locals())
      File "setup.py", line 540, in <module>
        setup_package()
      File "setup.py", line 536, in setup_package
        setup(**metadata)
      File "C:\Users\Amy\AppData\Local\Temp\pip-build-env-s15gckug\overlay\Lib\site-packages\numpy\distutils\core.py", line 137, in setup
        config = configuration()
      File "setup.py", line 435, in configuration
        raise NotFoundError(msg)
    numpy.distutils.system_info.NotFoundError: No lapack/blas resources found.
    ----------------------------------------
WARNING: Discarding https://files.pythonhosted.org/packages/04/ab/e2eb3e3f90b9363040a3d885ccc5c79fe20c5b8a3caa8fe3bf47ff653260/scipy-1.4.1.tar.gz#sha256=dee1bbf3a6c8f73b6b218cb28eed8dd13347ea2f87d572ce19b289d6fd3fbc59 (from https://pypi.org/simple/scipy/) (requires-python:>=3.5). Command errored out with exit status 1: 'C:\Users\Amy\AppData\Local\Programs\Python\Python39\python.exe' 'C:\Users\Amy\AppData\Local\Programs\Python\Python39\lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py' prepare_metadata_for_build_wheel 'C:\Users\Amy\AppData\Local\Temp\tmpe7qtz4x_' Check the logs for full command output.
ERROR: Could not find a version that satisfies the requirement scipy==1.4.1 (from versions: 0.8.0, 0.9.0, 0.10.0, 0.10.1, 0.11.0, 0.12.0, 0.12.1, 0.13.0, 0.13.1, 0.13.2, 0.13.3, 0.14.0, 0.14.1, 0.15.0, 0.15.1, 0.16.0, 0.16.1, 0.17.0, 0.17.1, 0.18.0, 0.18.1, 0.19.0, 0.19.1, 1.0.0b1, 1.0.0rc1, 1.0.0rc2, 1.0.0, 1.0.1, 1.1.0rc1, 1.1.0, 1.2.0rc1, 1.2.0rc2, 1.2.0, 1.2.1, 1.2.2, 1.2.3, 1.3.0rc1, 1.3.0rc2, 1.3.0, 1.3.1, 1.3.2, 1.3.3, 1.4.0rc1, 
1.4.0rc2, 1.4.0, 1.4.1, 1.5.0rc1, 1.5.0rc2, 1.5.0, 1.5.1, 1.5.2, 1.5.3, 1.5.4, 1.6.0rc1, 1.6.0rc2, 1.6.0, 1.6.1, 1.6.2, 1.6.3, 1.7.0rc1, 1.7.0rc2, 1.7.0, 1.7.1)
ERROR: No matching distribution found for scipy==1.4.1
