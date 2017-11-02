from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin('python.pydev')


name = "hello-app"
default_task = "publish"


@init
def set_properties(project):
    
    project.depends_on('flask')
    project.build_depends_on('coverage')
    project.set_property('coverage_break_build', True)
    project.set_property('flake8_break_build', True)
    project.set_property('flake8_verbose_output', True)
    
    
