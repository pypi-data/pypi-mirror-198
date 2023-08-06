import os
import re
import sys
from socket import gethostname
from argparse import ArgumentParser, Action, SUPPRESS
from clinterface import messages
from .readspec import readspec
from .fileutils import AbsPath, pathsplit, pathjoin, file_except_info
from .shared import names, nodes, paths, environ, iospec, config, options, remoteargs
from .utils import AttrDict, LogDict, GlobDict, ConfTemplate, natsorted as sorted, o, p, q, _
from .submit import initialize, submit 

class ArgList:
    def __init__(self, args):
        self.current = None
        if options.arguments.sort:
            self.args = sorted(args)
        elif options.arguments.sort_reverse:
            self.args = sorted(args, reverse=True)
        else:
            self.args = args
        if 'filter' in options.arguments:
            self.filter = re.compile(options.arguments.filter)
        else:
            self.filter = re.compile('.+')
    def __iter__(self):
        return self
    def __next__(self):
        try:
            self.current = self.args.pop(0)
        except IndexError:
            raise StopIteration
        if options.common.job:
            parentdir = AbsPath(options.common.cwd)
            for key in iospec.inputfiles:
                if AbsPath(pathjoin(parentdir, (self.current, key))).isfile():
                    inputname = self.current
                    break
            else:
                messages.failure('No hay archivos de entrada de', names.display, 'asociados al trabajo', self.current)
                return next(self)
        else:
            path = AbsPath(self.current, cwd=options.common.cwd)
            parentdir = path.parent
            try:
                path.assertfile()
            except Exception as e:
                file_except_info(e, path)
                return next(self)
            for key in iospec.inputfiles:
                if path.name.endswith('.' + key):
                    inputname = path.name[:-len('.' + key)]
                    break
            else:
                messages.failure(q(path.name), 'no es un archivo de entrada de', config.specname)
                return next(self)
        matched = self.filter.fullmatch(inputname)
        if matched:
            filtergroups = {str(i): x for i, x in enumerate(matched.groups())}
            return parentdir, inputname, filtergroups
        else:
            return next(self)

class ListOptions(Action):
    def __init__(self, **kwargs):
        super().__init__(nargs=0, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        if config.versions:
            print(_('Versiones disponibles:'))
            default = config.defaults.version if 'version' in config.defaults else None
            print_tree(tuple(config.versions.keys()), [default], level=1)
        for path in config.parameterpaths:
            dirtree = {}
            parts = pathsplit(ConfTemplate(path).safe_substitute(names))
            dirbranches(AbsPath(parts.pop(0)), parts, dirtree)
            if dirtree:
                defaultdict = LogDict()
                ConfTemplate(path).substitute(defaultdict)
                defaults = [config.defaults.parametervars.get(i, None) for i in defaultdict.logged_keys]
                print(_('Conjuntos de parámetros disponibles:'))
                print_tree(dirtree, defaults, level=1)
        sys.exit()

class StorePath(Action):
    def __init__(self, **kwargs):
        super().__init__(nargs=1, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, AbsPath(values[0], cwd=os.getcwd()))

#TODO How to append value to list?
class AppendPath(Action):
    def __init__(self, **kwargs):
        super().__init__(nargs=1, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, AbsPath(values[0], cwd=os.getcwd()))

def dirbranches(trunk, componentlist, dirtree):
    trunk.assertdir()
    if componentlist:
        defaultdict = LogDict()
        component = ConfTemplate(componentlist.pop(0)).substitute(defaultdict)
        if defaultdict.logged_keys:
            branches = trunk.glob(ConfTemplate(component).substitute(GlobDict()))
            for branch in branches:
                dirtree[branch] = {}
                dirbranches(trunk/branch, componentlist, dirtree[branch])
        else:
            dirbranches(trunk/component, componentlist, dirtree)

try:

    parser = ArgumentParser(add_help=False)
    parser.add_argument('confdir')
    parser.add_argument('filepath')
    parsedargs, remainingargs = parser.parse_known_args()

    paths.confdir = parsedargs.confdir
    names.command = os.path.basename(parsedargs.filepath)
    paths.moduledir = AbsPath(__file__).parent

    config.merge(readspec(pathjoin(paths.confdir, 'config.json')))
    config.merge(readspec(pathjoin(paths.moduledir, 'schedulers', config.scheduler, 'config.json')))
    config.merge(readspec(pathjoin(paths.confdir, 'packages', names.command, 'config.json')))
    iospec.merge(readspec(pathjoin(paths.moduledir, 'iospecs', config.specname, 'iospec.json')))

    userconfdir = pathjoin(paths.home, '.clusterq')
    userclusterconf = pathjoin(userconfdir, 'clusterconf.json')
    userpackageconf = pathjoin(userconfdir, names.command, 'packageconf.json')
    
    try:
        config.merge(readspec(userclusterconf))
    except FileNotFoundError:
        pass

    try:
        config.merge(readspec(userpackageconf))
    except FileNotFoundError:
        pass
    
    try:
        names.display = config.displayname
    except AttributeError:
        messages.error('No se definió el nombre del programa', key='displayname')

    try:
        names.cluster = config.clustername
    except AttributeError:
        messages.error('No se definió el nombre del clúster', key='clustername')

    try:
        nodes.head = config.headnode
    except AttributeError:
        nodes.head = names.host

    parser = ArgumentParser(prog=names.command, add_help=False, description='Envía trabajos de {} a la cola de ejecución.'.format(names.display))

    group1 = parser.add_argument_group('Argumentos')
    group1.add_argument('files', nargs='*', metavar='FILE', help='Rutas de los archivos de entrada.')
    group1.name = 'arguments'
    group1.remote = False

#    group1 = parser.add_argument_group('Ejecución remota')

    group2 = parser.add_argument_group('Opciones comunes')
    group2.name = 'common'
    group2.remote = True
    group2.add_argument('-h', '--help', action='help', help='Mostrar este mensaje de ayuda y salir.')
    group2.add_argument('-l', '--list', action=ListOptions, default=SUPPRESS, help='Mostrar las opciones disponibles y salir.')
    group2.add_argument('-v', '--version', metavar='VERSION', default=SUPPRESS, help='Usar la versión VERSION del ejecutable.')
    group2.add_argument('-p', '--prompt', action='store_true', help='Seleccionar interactivamente las opciones disponibles.')
    group2.add_argument('-n', '--nproc', type=int, metavar='#PROCS', default=1, help='Requerir #PROCS núcleos de procesamiento.')
    group2.add_argument('-q', '--queue', metavar='QUEUE', default=SUPPRESS, help='Requerir la cola QUEUE.')
    group2.add_argument('-j', '--job', action='store_true', help='Interpretar los argumentos como nombres de trabajo en vez de rutas de archivo.')
    group2.add_argument('-o', '--out', action=StorePath, metavar='PATH', default=SUPPRESS, help='Escribir los archivos de salida en el directorio PATH.')
    group2.add_argument('--cwd', action=StorePath, metavar='PATH', default=os.getcwd(), help='Usar PATH como directorio actual de trabajo.')
    group2.add_argument('--raw', action='store_true', help='No interpolar ni crear copias de los archivos de entrada.')
    group2.add_argument('--move', action='store_true', help='Mover los archivos de entrada al directorio de salida en vez de copiarlos.')
    group2.add_argument('--delay', type=int, metavar='#SECONDS', default=0, help='Demorar el envío del trabajo #SECONDS segundos.')
    group2.add_argument('--scratch', action=StorePath, metavar='PATH', default=SUPPRESS, help='Escribir los archivos temporales en el directorio PATH.')
    hostgroup = group2.add_mutually_exclusive_group()
    hostgroup.add_argument('-N', '--nhost', type=int, metavar='#NODES', default=1, help='Requerir #NODES nodos de ejecución.')
    hostgroup.add_argument('--hosts', metavar='NODE', default=SUPPRESS, help='Solicitar nodos específicos de ejecución.')
    yngroup = group2.add_mutually_exclusive_group()
    yngroup.add_argument('--yes', action='store_true', help='Responder "si" a todas las preguntas.')
    yngroup.add_argument('--no', action='store_true', help='Responder "no" a todas las preguntas.')
#    group2.add_argument('-X', '--xdialog', action='store_true', help='Habilitar el modo gráfico para los mensajes y diálogos.')

    group3 = parser.add_argument_group('Opciones remotas')
    group3.name = 'remote'
    group3.remote = False 
    group3.add_argument('-H', '--host', metavar='HOSTNAME', help='Procesar el trabajo en el host HOSTNAME.')

    group4 = parser.add_argument_group('Conjuntos de parámetros')
    group4.name = 'parametervars'
    group4.remote = True
    for key in iospec.parametervars:
        group4.add_argument(o(key), metavar='SETNAME', default=SUPPRESS, help='Seleccionar el conjunto SETNAME de parámetros.')

    group5 = parser.add_argument_group('Opciones de interpolación')
    group5.name = 'interpolation'
    group5.remote = False
    group5.add_argument('-x', '--var', dest='posvars', metavar='VALUE', action='append', default=[], help='Variables posicionales de interpolación.')
    molgroup = group5.add_mutually_exclusive_group()
    molgroup.add_argument('-m', '--mol', metavar='MOLFILE', action='append', default=[], help='Incluir el último paso del archivo MOLFILE en las variables de interpolación.')
    molgroup.add_argument('-M', '--trjmol', metavar='MOLFILE', default=None, help='Incluir todos los pasos del archivo MOLFILE en las variables de interpolación.')
    group5.add_argument('--prefix', metavar='PREFIX', default=None, help='Agregar el prefijo PREFIX al nombre del trabajo.')
    group5.add_argument('-a', '--anchor', metavar='CHARACTER', default='$', help='Usar el caracter CHARACTER como delimitador de las variables de interpolación en los archivos de entrada.')
    for key in iospec.interpolationvars:
        group5.add_argument(o(key), metavar='VARNAME', default=SUPPRESS, help='Variables de interpolación.')

    group6 = parser.add_argument_group('Archivos reutilizables')
    group6.name = 'targetfiles'
    group6.remote = False
    for key, value in iospec.fileoptions.items():
        group6.add_argument(o(key), action=StorePath, metavar='FILEPATH', default=SUPPRESS, help='Ruta al archivo {}.'.format(value))

    group7 = parser.add_argument_group('Opciones de depuración')
    group7.name = 'debug'
    group7.remote = False
    group7.add_argument('--dry-run', action='store_true', help='Procesar los archivos de entrada sin enviar el trabajo.')

    group8 = parser.add_argument_group('Manipulación de argumentos')
    group8.name = 'arguments'
    group8.remote = False 
    sortgroup = group8.add_mutually_exclusive_group()
    sortgroup.add_argument('-s', '--sort', action='store_true', help='Ordenar los argumentos en orden ascendente.')
    sortgroup.add_argument('-S', '--sort-reverse', action='store_true', help='Ordenar los argumentos en orden descendente.')
    group8.add_argument('-f', '--filter', metavar='REGEX', default=SUPPRESS, help='Enviar únicamente los trabajos que coinciden con la expresión regular.')

    parsedargs = parser.parse_args(remainingargs)
#    print(parsedargs)

    for group in parser._action_groups:
        group_dict = {a.dest:getattr(parsedargs, a.dest) for a in group._group_actions if a.dest in parsedargs}
        if hasattr(group, 'name'):
            options[group.name] = AttrDict(**group_dict)
        if hasattr(group, 'remote') and group.remote:
            remoteargs.gather(AttrDict(**group_dict))

    if not parsedargs.files:
        messages.error('Debe especificar al menos un archivo de entrada')

    arguments = ArgList(parsedargs.files)

    try:
        environ.TELEGRAM_BOT_URL = os.environ['TELEGRAM_BOT_URL']
        environ.TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
    except KeyError:
        pass

#    print(options)
#    print(remoteargs)

#    #TODO Add suport for dialog boxes
#    if options.common.xdialog:
#        try:
#            from tkdialog import TkDialog
#        except ImportError:
#            raise SystemExit()
#        else:
#            dialogs.yesno = join_args(TkDialog().yesno)
#            messages.failure = join_args(TkDialog().message)
#            messages.success = join_args(TkDialog().message)

    initialize()

    for parentdir, inputname, filtergroups in arguments:
        submit(parentdir, inputname, filtergroups)
    
except KeyboardInterrupt:

    messages.error('Interrumpido por el usuario')
