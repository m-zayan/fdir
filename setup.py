from distutils.core import setup, Extension

module = Extension('fdir',
                    define_macros = [('MAJOR_VERSION', '1'),
                                     ('MINOR_VERSION', '0')],
                    sources = ['_fdir_.c'])

setup (name = 'fdir',
       version = '0.1',
       description = 'Alpha Version Module',
       author = 'Mohamed Zayan',
       ext_modules = [module])
