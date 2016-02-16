
from auxlib.entity import Entity, StringField, IntField, EnumField, ListField
from enum import Enum





# If you update this please update the example in
# conda-docs/docs/source/build.rst
FIELDS = {
    'package': ['name', 'version'],
    'source': ['fn', 'url', 'md5', 'sha1', 'sha256', 'path',
               'git_url', 'git_tag', 'git_branch', 'git_rev', 'git_depth',
               'hg_url', 'hg_tag',
               'svn_url', 'svn_rev', 'svn_ignore_externals',
               'patches'],
    'build': ['number', 'string', 'entry_points', 'osx_is_app',
              'features', 'track_features', 'preserve_egg_dir',
              'no_link', 'binary_relocation', 'script', 'noarch_python',
              'has_prefix_files', 'binary_has_prefix_files', 'script_env',
              'detect_binary_files_with_prefix', 'rpaths',
              'always_include_files', 'skip', 'msvc_compiler'],
    'requirements': ['build', 'run', 'conflicts'],  # needs test
    'app': ['entry', 'icon', 'summary', 'type', 'cli_opts',
            'own_environment'],
    'test': ['requires', 'commands', 'files', 'imports'],
    'about': ['home', 'license', 'license_family',
              'summary', 'readme', 'license_file'],
}

# package: name, version, runtime, build_number, features


# from conda/config.py
########################

_sys_map = {'linux2': 'linux', 'linux': 'linux',
            'darwin': 'osx', 'win32': 'win', 'openbsd5': 'openbsd'}
non_x86_linux_machines = {'armv6l', 'armv7l', 'ppc64le'}
platform = _sys_map.get(sys.platform, 'unknown')
bits = 8 * tuple.__itemsize__
if force_32bit:
    if bits == 32:
        sys.exit("Error: you cannot set CONDA_FORCE_32BIT using "
                 "32-bit already.")
    bits = 32

if platform == 'linux' and machine() in non_x86_linux_machines:
    arch_name = machine()
    subdir = 'linux-%s' % arch_name
else:
    arch_name = {64: 'x86_64', 32: 'x86'}[bits]
    subdir = '%s-%d' % (platform, bits)

rc_list_keys = [
    'channels',
    'disallow',
    'create_default_packages',
    'track_features',
    'envs_dirs',
    'default_channels',
]

DEFAULT_CHANNEL_ALIAS = 'https://conda.anaconda.org/'

ADD_BINSTAR_TOKEN = True

rc_bool_keys = [
    'add_binstar_token',
    'add_anaconda_token',
    'add_pip_as_python_dependency',
    'always_yes',
    'always_copy',
    'allow_softlinks',
    'changeps1',
    'use_pip',
    'offline',
    'binstar_upload',
    'anaconda_upload',
    'show_channel_urls',
    'allow_other_channels',
    'update_dependencies',
]

rc_string_keys = [
    'ssl_verify',
    'channel_alias',
    'root_dir',
]

# Not supported by conda config yet
rc_other = [
    'proxy_servers',
]

user_rc_path = abspath(expanduser('~/.condarc'))
sys_rc_path = join(sys.prefix, '.condarc')



# from conda_build/metatadata.py
#####################################
allowed_license_families = set("""
AGPL
Apache
BSD
GPL2
GPL3
LGPL
MIT
Other
PSF
Proprietary
Public-Domain
""".split())










# from conda_build/main_build.py
###########################################


all_versions = {
    'python': [26, 27, 33, 34, 35],
    'numpy': [16, 17, 18, 19, 110],
    'perl': None,
    'R': None,
}



# These don't represent all supported versions. It's just for tab completion.

class PythonVersionCompleter(Completer):
    def _get_items(self):
        return ['all'] + [str(i/10) for i in all_versions['python']]

class NumPyVersionCompleter(Completer):
    def _get_items(self):
        return ['all'] + [str(i/10) for i in all_versions['numpy']]

class RVersionsCompleter(Completer):
    def _get_items(self):
        return ['3.1.2', '3.1.3', '3.2.0', '3.2.1', '3.2.2']







class Arch(Enum):
    x86 = 'x86'
    x86_64 = 'x86_64'


class Platform(Enum):
    osx = 'osx'






class Channel(Entity):
    name = StringField()
    url = StringField()


class Patch(Entity):
    filename = StringField()
    url = StringField()
    patch_level = IntField(default=0)


class Package(Entity):
    requirements = ListField(basestring)


class PackageSpec(Entity):
    """
    pyside-1.1.2-py27_1
    zlib-1.2.7-1
    """
    channel = StringField()
    name = StringField()
    version = StringField()
    build = StringField()
    build_number = IntField()
    platform = EnumField(Platform)
    arch = EnumField(Arch)





class CondaConfig(Entity):
    package = ''
    source = ''
    build = ''
    requirements = ''
    app = ''
    test = ''
    about = ''

