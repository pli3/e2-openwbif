#!/usr/bin/env python




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from Plugins.Extensions.OpenWebif.local import tstrings

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1447321436.736963
__CHEETAH_genTimestamp__ = 'Thu Nov 12 18:43:56 2015'
__CHEETAH_src__ = '/home/knuth/openpli-oe-core/build/tmp/work/fusionhd-oe-linux/enigma2-plugin-extensions-openwebif/1+gitAUTOINC+5837c87afc-r0/git/plugin/controllers/views/ajax/powerstate.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Nov 12 18:43:41 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class powerstate(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(powerstate, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''<div style="height: 300px; width:500px">
\t<div class="powerStateButtons">
\t\t<ul>
\t\t\t<li onclick="handle_power_state_dialog(new_power_state = 0); return false">''')
        _v = VFFSL(SL,"tstrings",True)['standby_toggle'] # u"$tstrings['standby_toggle']" on line 5, col 79
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['standby_toggle']")) # from line 5, col 79.
        write(u'''</li>
\t\t\t<li onclick="handle_power_state_dialog(new_power_state = 1); return false">''')
        _v = VFFSL(SL,"tstrings",True)['deep_standby'] # u"$tstrings['deep_standby']" on line 6, col 79
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['deep_standby']")) # from line 6, col 79.
        write(u'''</li>
\t\t\t<li onclick="handle_power_state_dialog(new_power_state = 2); return false">''')
        _v = VFFSL(SL,"tstrings",True)['reboot_box'] # u"$tstrings['reboot_box']" on line 7, col 79
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['reboot_box']")) # from line 7, col 79.
        write(u'''</li> 
\t\t\t<li onclick="handle_power_state_dialog(new_power_state = 3); return false">''')
        _v = VFFSL(SL,"tstrings",True)['restart_gui'] # u"$tstrings['restart_gui']" on line 8, col 79
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['restart_gui']")) # from line 8, col 79.
        write(u'''</li>
\t\t</ul>
\t</div>
</div>
<!-- cache the spinner for the restart gui or reboot stb dialog -->
<div id="screenshotspinnerl">
\t<img id="screenshotspinner" src="images/spinner.gif" width="64" height="64" border="0" alt="''')
        _v = VFFSL(SL,"tstrings",True)['loading'] # u"$tstrings['loading']" on line 14, col 94
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['loading']")) # from line 14, col 94.
        write(u''' ..." style="display: none;">
</div>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_powerstate= 'respond'

## END CLASS DEFINITION

if not hasattr(powerstate, '_initCheetahAttributes'):
    templateAPIClass = getattr(powerstate, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(powerstate)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=powerstate()).run()


