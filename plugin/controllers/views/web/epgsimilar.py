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
__CHEETAH_genTime__ = 1447321436.176619
__CHEETAH_genTimestamp__ = 'Thu Nov 12 18:43:56 2015'
__CHEETAH_src__ = '/home/knuth/openpli-oe-core/build/tmp/work/fusionhd-oe-linux/enigma2-plugin-extensions-openwebif/1+gitAUTOINC+5837c87afc-r0/git/plugin/controllers/views/web/epgsimilar.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Nov 12 18:43:41 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class epgsimilar(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(epgsimilar, self).__init__(*args, **KWs)
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
        
        _orig_filter_53525962 = _filter
        filterName = u'WebSafe'
        if self._CHEETAH__filters.has_key("WebSafe"):
            _filter = self._CHEETAH__currentFilter = self._CHEETAH__filters[filterName]
        else:
            _filter = self._CHEETAH__currentFilter = \
			self._CHEETAH__filters[filterName] = getattr(self._CHEETAH__filtersLib, filterName)(self).filter
        write(u'''<?xml version="1.0" encoding="UTF-8"?>
<e2eventlist>
''')
        for event in VFFSL(SL,"events",True): # generated from line 4, col 2
            write(u'''\t<e2event>
\t\t<e2eventid>''')
            _v = VFFSL(SL,"str",False)(VFFSL(SL,"event.id",True)) # u'$str($event.id)' on line 6, col 14
            if _v is not None: write(_filter(_v, rawExpr=u'$str($event.id)')) # from line 6, col 14.
            write(u'''</e2eventid>
\t\t<e2eventstart>''')
            _v = VFFSL(SL,"str",False)(VFFSL(SL,"event.begin_timestamp",True)) # u'$str($event.begin_timestamp)' on line 7, col 17
            if _v is not None: write(_filter(_v, rawExpr=u'$str($event.begin_timestamp)')) # from line 7, col 17.
            write(u'''</e2eventstart>
\t\t<e2eventduration>''')
            _v = VFFSL(SL,"str",False)(VFFSL(SL,"event.duration_sec",True)) # u'$str($event.duration_sec)' on line 8, col 20
            if _v is not None: write(_filter(_v, rawExpr=u'$str($event.duration_sec)')) # from line 8, col 20.
            write(u'''</e2eventduration>
\t\t<e2eventcurrenttime>''')
            _v = VFFSL(SL,"str",False)(VFFSL(SL,"event.now_timestamp",True)) # u'$str($event.now_timestamp)' on line 9, col 23
            if _v is not None: write(_filter(_v, rawExpr=u'$str($event.now_timestamp)')) # from line 9, col 23.
            write(u'''</e2eventcurrenttime>
\t\t<e2eventtitle>''')
            _v = VFFSL(SL,"str",False)(VFFSL(SL,"event.title",True)) # u'$str($event.title)' on line 10, col 17
            if _v is not None: write(_filter(_v, rawExpr=u'$str($event.title)')) # from line 10, col 17.
            write(u'''</e2eventtitle>
\t\t<e2eventdescription>''')
            _v = VFFSL(SL,"str",False)(VFFSL(SL,"event.shortdesc",True)) # u'$str($event.shortdesc)' on line 11, col 23
            if _v is not None: write(_filter(_v, rawExpr=u'$str($event.shortdesc)')) # from line 11, col 23.
            write(u'''</e2eventdescription>
\t\t<e2eventdescriptionextended>''')
            _v = VFFSL(SL,"str",False)(VFFSL(SL,"event.longdesc",True)) # u'$str($event.longdesc)' on line 12, col 31
            if _v is not None: write(_filter(_v, rawExpr=u'$str($event.longdesc)')) # from line 12, col 31.
            write(u'''</e2eventdescriptionextended>
\t\t<e2eventservicereference>''')
            _v = VFFSL(SL,"event.sref",True) # u'$event.sref' on line 13, col 28
            if _v is not None: write(_filter(_v, rawExpr=u'$event.sref')) # from line 13, col 28.
            write(u'''</e2eventservicereference>
\t\t<e2eventservicename>''')
            _v = VFFSL(SL,"event.sname",True) # u'$event.sname' on line 14, col 23
            if _v is not None: write(_filter(_v, rawExpr=u'$event.sname')) # from line 14, col 23.
            write(u'''</e2eventservicename>
\t</e2event>
''')
        write(u'''</e2eventlist>
''')
        _filter = self._CHEETAH__currentFilter = _orig_filter_53525962
        
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

    _mainCheetahMethod_for_epgsimilar= 'respond'

## END CLASS DEFINITION

if not hasattr(epgsimilar, '_initCheetahAttributes'):
    templateAPIClass = getattr(epgsimilar, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(epgsimilar)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=epgsimilar()).run()


