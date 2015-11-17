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

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1447321436.209204
__CHEETAH_genTimestamp__ = 'Thu Nov 12 18:43:56 2015'
__CHEETAH_src__ = '/home/knuth/openpli-oe-core/build/tmp/work/fusionhd-oe-linux/enigma2-plugin-extensions-openwebif/1+gitAUTOINC+5837c87afc-r0/git/plugin/controllers/views/web/getallservices.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Nov 12 18:43:41 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class getallservices(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(getallservices, self).__init__(*args, **KWs)
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
        
        _orig_filter_14349137 = _filter
        filterName = u'WebSafe'
        if self._CHEETAH__filters.has_key("WebSafe"):
            _filter = self._CHEETAH__currentFilter = self._CHEETAH__filters[filterName]
        else:
            _filter = self._CHEETAH__currentFilter = \
			self._CHEETAH__filters[filterName] = getattr(self._CHEETAH__filtersLib, filterName)(self).filter
        write(u'''<?xml version="1.0" encoding="UTF-8"?>
<e2servicelistrecursive>
''')
        for service in VFFSL(SL,"services",True): # generated from line 4, col 2
            if VFFSL(SL,"len",False)(VFFSL(SL,"service.subservices",True)) > 0: # generated from line 5, col 3
                write(u'''\t\t<e2bouquet>
\t\t\t<e2servicereference>''')
                _v = VFFSL(SL,"service.servicereference",True) # u'$service.servicereference' on line 7, col 24
                if _v is not None: write(_filter(_v, rawExpr=u'$service.servicereference')) # from line 7, col 24.
                write(u'''</e2servicereference>
\t\t\t<e2servicename>''')
                _v = VFFSL(SL,"service.servicename",True) # u'$service.servicename' on line 8, col 19
                if _v is not None: write(_filter(_v, rawExpr=u'$service.servicename')) # from line 8, col 19.
                write(u'''</e2servicename>
\t\t\t<e2servicelist>
''')
                for service2 in VFFSL(SL,"service.subservices",True): # generated from line 10, col 4
                    write(u'''\t\t\t<e2service>
\t\t\t\t<e2servicereference>''')
                    _v = VFFSL(SL,"service2.servicereference",True) # u'$service2.servicereference' on line 12, col 25
                    if _v is not None: write(_filter(_v, rawExpr=u'$service2.servicereference')) # from line 12, col 25.
                    write(u'''</e2servicereference>
\t\t\t\t<e2servicename>''')
                    _v = VFFSL(SL,"service2.servicename",True) # u'$service2.servicename' on line 13, col 20
                    if _v is not None: write(_filter(_v, rawExpr=u'$service2.servicename')) # from line 13, col 20.
                    write(u'''</e2servicename>
\t\t\t</e2service>
''')
                write(u'''\t\t\t</e2servicelist>
\t\t</e2bouquet>
''')
            else: # generated from line 18, col 3
                write(u'''\t\t<e2service>
\t\t\t<e2servicereference>''')
                _v = VFFSL(SL,"service.servicereference",True) # u'$service.servicereference' on line 20, col 24
                if _v is not None: write(_filter(_v, rawExpr=u'$service.servicereference')) # from line 20, col 24.
                write(u'''</e2servicereference>
\t\t\t<e2servicename>''')
                _v = VFFSL(SL,"service.servicename",True) # u'$service.servicename' on line 21, col 19
                if _v is not None: write(_filter(_v, rawExpr=u'$service.servicename')) # from line 21, col 19.
                write(u'''</e2servicename>
\t\t</e2service>
''')
        write(u'''</e2servicelistrecursive>
''')
        _filter = self._CHEETAH__currentFilter = _orig_filter_14349137
        
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

    _mainCheetahMethod_for_getallservices= 'respond'

## END CLASS DEFINITION

if not hasattr(getallservices, '_initCheetahAttributes'):
    templateAPIClass = getattr(getallservices, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(getallservices)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=getallservices()).run()


