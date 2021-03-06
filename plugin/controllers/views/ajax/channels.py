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
__CHEETAH_genTime__ = 1447321436.733869
__CHEETAH_genTimestamp__ = 'Thu Nov 12 18:43:56 2015'
__CHEETAH_src__ = '/home/knuth/openpli-oe-core/build/tmp/work/fusionhd-oe-linux/enigma2-plugin-extensions-openwebif/1+gitAUTOINC+5837c87afc-r0/git/plugin/controllers/views/ajax/channels.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Nov 12 18:43:41 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class channels(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(channels, self).__init__(*args, **KWs)
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
        
        for channel in VFFSL(SL,"channels",True): # generated from line 1, col 1
            write(u'''<table width="100%"><tbody><tr class="channel_tr">
<div>
<div>
<div class="channel_left">
''')
            name = VFN(VFFSL(SL,"channel.name",True),"replace",False)("'", r"\'")
            if VFFSL(SL,"channel.protection",True) == "0": # generated from line 8, col 1
                write(u'''<a href="#" onclick="zapChannel(\'''')
                _v = VFFSL(SL,"channel.ref",True) # u'$channel.ref' on line 9, col 34
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.ref')) # from line 9, col 34.
                write(u"""', '""")
                _v = VFFSL(SL,"name",True) # u'$name' on line 9, col 50
                if _v is not None: write(_filter(_v, rawExpr=u'$name')) # from line 9, col 50.
                write(u'''\'); return false" title="''')
                _v = VFFSL(SL,"tstrings",True)['zap_to'] # u"$tstrings['zap_to']" on line 9, col 80
                if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['zap_to']")) # from line 9, col 80.
                write(u''' ''')
                _v = VFFSL(SL,"channel.name",True) # u'$channel.name' on line 9, col 100
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.name')) # from line 9, col 100.
                write(u'''">''')
                _v = VFFSL(SL,"channel.name",True) # u'$channel.name' on line 9, col 115
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.name')) # from line 9, col 115.
                write(u'''</a><br />
''')
            else: # generated from line 10, col 1
                write(u'''<a href="#" onclick="return false" title="''')
                _v = VFFSL(SL,"tstrings",True)['locked'] # u"$tstrings['locked']" on line 11, col 43
                if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['locked']")) # from line 11, col 43.
                write(u'''">''')
                _v = VFFSL(SL,"channel.name",True) # u'$channel.name' on line 11, col 64
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.name')) # from line 11, col 64.
                write(u'''</a><br />
''')
            write(u'''</div>
<div class="channel_right">
''')
            if VFFSL(SL,"channel.protection",True) == "0": # generated from line 15, col 1
                if VFFSL(SL,"type",True) == "radio": # generated from line 16, col 1
                    write(u'''<a href="#" onclick="addTimer(\'\',\'''')
                    _v = VFFSL(SL,"channel.ref",True) # u'$channel.ref' on line 17, col 35
                    if _v is not None: write(_filter(_v, rawExpr=u'$channel.ref')) # from line 17, col 35.
                    write(u"""','""")
                    _v = VFFSL(SL,"channel.name",True) # u'$channel.name' on line 17, col 50
                    if _v is not None: write(_filter(_v, rawExpr=u'$channel.name')) # from line 17, col 50.
                    write(u'''\')" title="''')
                    _v = VFFSL(SL,"tstrings",True)['add_timer'] # u"$tstrings['add_timer']" on line 17, col 74
                    if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['add_timer']")) # from line 17, col 74.
                    write(u'''"><div class="ow_i ow_i_timer"></div></a>
''')
                write(u'''<a href="#" onclick="open_epg_dialog(\'''')
                _v = VFFSL(SL,"channel.ref",True) # u'$channel.ref' on line 19, col 39
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.ref')) # from line 19, col 39.
                write(u"""','""")
                _v = VFFSL(SL,"channel.name",True) # u'$channel.name' on line 19, col 54
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.name')) # from line 19, col 54.
                write(u'''\')" title="''')
                _v = VFFSL(SL,"tstrings",True)['show_epg_for'] # u"$tstrings['show_epg_for']" on line 19, col 78
                if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['show_epg_for']")) # from line 19, col 78.
                write(u''' ''')
                _v = VFFSL(SL,"channel.name",True) # u'$channel.name' on line 19, col 104
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.name')) # from line 19, col 104.
                write(u'''"><div class="ow_i ow_i_epg"></div></a>
''')
                if VFFSL(SL,"transcoding",True): # generated from line 20, col 1
                    write(u'''<a href="#" onclick="jumper8001(\'''')
                    _v = VFFSL(SL,"channel.ref",True) # u'$channel.ref' on line 21, col 34
                    if _v is not None: write(_filter(_v, rawExpr=u'$channel.ref')) # from line 21, col 34.
                    write(u"""', '""")
                    _v = VFFSL(SL,"channel.name",True) # u'$channel.name' on line 21, col 50
                    if _v is not None: write(_filter(_v, rawExpr=u'$channel.name')) # from line 21, col 50.
                    write(u'''\');" title="''')
                    _v = VFFSL(SL,"tstrings",True)['stream'] # u"$tstrings['stream']" on line 21, col 75
                    if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['stream']")) # from line 21, col 75.
                    write(u''': ''')
                    _v = VFFSL(SL,"channel.name",True) # u'$channel.name' on line 21, col 96
                    if _v is not None: write(_filter(_v, rawExpr=u'$channel.name')) # from line 21, col 96.
                    write(u'''"><div class="ow_i ow_i_stream1"></div></a>
<a href="#" onclick="jumper8002(\'''')
                    _v = VFFSL(SL,"channel.ref",True) # u'$channel.ref' on line 22, col 34
                    if _v is not None: write(_filter(_v, rawExpr=u'$channel.ref')) # from line 22, col 34.
                    write(u"""', '""")
                    _v = VFFSL(SL,"channel.name",True) # u'$channel.name' on line 22, col 50
                    if _v is not None: write(_filter(_v, rawExpr=u'$channel.name')) # from line 22, col 50.
                    write(u'''\');" title="''')
                    _v = VFFSL(SL,"tstrings",True)['stream'] # u"$tstrings['stream']" on line 22, col 75
                    if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['stream']")) # from line 22, col 75.
                    write(u''' (''')
                    _v = VFFSL(SL,"tstrings",True)['transcoded'] # u"$tstrings['transcoded']" on line 22, col 96
                    if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['transcoded']")) # from line 22, col 96.
                    write(u'''): ''')
                    _v = VFFSL(SL,"channel.name",True) # u'$channel.name' on line 22, col 122
                    if _v is not None: write(_filter(_v, rawExpr=u'$channel.name')) # from line 22, col 122.
                    write(u'''"><div class="ow_i ow_i_stream2"></div></a>
''')
                else: # generated from line 23, col 1
                    write(u'''<a target="_blank" href=\'web/stream.m3u?ref=''')
                    _v = VFFSL(SL,"channel.ref",True) # u'$channel.ref' on line 24, col 45
                    if _v is not None: write(_filter(_v, rawExpr=u'$channel.ref')) # from line 24, col 45.
                    write(u'''&name=''')
                    _v = VFFSL(SL,"channel.name",True) # u'$channel.name' on line 24, col 63
                    if _v is not None: write(_filter(_v, rawExpr=u'$channel.name')) # from line 24, col 63.
                    write(u'''\' title="''')
                    _v = VFFSL(SL,"tstrings",True)['stream'] # u"$tstrings['stream']" on line 24, col 85
                    if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['stream']")) # from line 24, col 85.
                    write(u''' ''')
                    _v = VFFSL(SL,"channel.name",True) # u'$channel.name' on line 24, col 105
                    if _v is not None: write(_filter(_v, rawExpr=u'$channel.name')) # from line 24, col 105.
                    write(u'''"><div class="ow_i ow_i_stream1"></div></a>
''')
            else: # generated from line 26, col 1
                write(u'''<a target="_blank" href=\'#\' title="''')
                _v = VFFSL(SL,"tstrings",True)['locked'] # u"$tstrings['locked']" on line 27, col 36
                if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['locked']")) # from line 27, col 36.
                write(u'''"><div class="ow_i ow_i_lock"></div></a>
''')
            write(u'''</div>

''')
            if VFN(VFFSL(SL,"channel",True),"has_key",False)('now_title') and VFFSL(SL,"channel.protection",True) == "0": # generated from line 31, col 1
                write(u'''<div class="channel_leftE">
<div>
''')
                _v = VFFSL(SL,"channel.now_begin",True) # u'$channel.now_begin' on line 34, col 1
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.now_begin')) # from line 34, col 1.
                write(u''' - ''')
                _v = VFFSL(SL,"channel.now_end",True) # u'$channel.now_end' on line 34, col 22
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.now_end')) # from line 34, col 22.
                write(u''' &nbsp;&nbsp;&nbsp;
<a href=\'#\' onClick="toggle_chan_des(\'''')
                _v = VFFSL(SL,"channel.now_ev_id",True) # u'$channel.now_ev_id' on line 35, col 39
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.now_ev_id')) # from line 35, col 39.
                write(u"""', '""")
                _v = VFFSL(SL,"channel.ref",True) # u'$channel.ref' on line 35, col 61
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.ref')) # from line 35, col 61.
                write(u"""', '""")
                _v = VFFSL(SL,"channel.now_idp",True) # u'$channel.now_idp' on line 35, col 77
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.now_idp')) # from line 35, col 77.
                write(u'''\'); return false" title="''')
                _v = VFFSL(SL,"channel.now_title",True) # u'$channel.now_title' on line 35, col 118
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.now_title')) # from line 35, col 118.
                write(u'''">''')
                _v = VFFSL(SL,"channel.now_title",True) # u'$channel.now_title' on line 35, col 138
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.now_title')) # from line 35, col 138.
                write(u'''</a>
</div>
</div>
<div class="channel_rightE">
+''')
                _v = VFFSL(SL,"channel.now_left",True) # u'$channel.now_left' on line 39, col 2
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.now_left')) # from line 39, col 2.
                write(u''' min
</div>
<div class="channel_desc" id="''')
                _v = VFFSL(SL,"channel.now_idp",True) # u'$channel.now_idp' on line 41, col 31
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.now_idp')) # from line 41, col 31.
                write(u'''">''')
                _v = VFFSL(SL,"tstrings",True)['no_description_available'] # u"$tstrings['no_description_available']" on line 41, col 49
                if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['no_description_available']")) # from line 41, col 49.
                write(u'''</div>
<div class="channel_content">
<div class="meter-wrap">
<div class="meter-value" style="width: ''')
                _v = VFFSL(SL,"channel.progress",True) # u'${channel.progress}' on line 44, col 40
                if _v is not None: write(_filter(_v, rawExpr=u'${channel.progress}')) # from line 44, col 40.
                write(u'''px;"></div></div>
</div>
<div class="channel_leftE">
''')
                _v = VFFSL(SL,"channel.next_begin",True) # u'$channel.next_begin' on line 47, col 1
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.next_begin')) # from line 47, col 1.
                write(u''' - ''')
                _v = VFFSL(SL,"channel.next_end",True) # u'$channel.next_end' on line 47, col 23
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.next_end')) # from line 47, col 23.
                write(u''' &nbsp;&nbsp;&nbsp;
<a href=\'#\' onClick="toggle_chan_des(\'''')
                _v = VFFSL(SL,"channel.next_ev_id",True) # u'$channel.next_ev_id' on line 48, col 39
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.next_ev_id')) # from line 48, col 39.
                write(u"""', '""")
                _v = VFFSL(SL,"channel.ref",True) # u'$channel.ref' on line 48, col 62
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.ref')) # from line 48, col 62.
                write(u"""', '""")
                _v = VFFSL(SL,"channel.next_idp",True) # u'$channel.next_idp' on line 48, col 78
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.next_idp')) # from line 48, col 78.
                write(u'''\'); return false" title="''')
                _v = VFFSL(SL,"channel.next_title",True) # u'$channel.next_title' on line 48, col 120
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.next_title')) # from line 48, col 120.
                write(u'''">''')
                _v = VFFSL(SL,"channel.next_title",True) # u'$channel.next_title' on line 48, col 141
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.next_title')) # from line 48, col 141.
                write(u'''</a>
</div>
<div class="channel_rightE">
''')
                _v = VFFSL(SL,"channel.next_duration",True) # u'$channel.next_duration' on line 51, col 1
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.next_duration')) # from line 51, col 1.
                write(u''' min
</div>
<div class="channel_desc" id="''')
                _v = VFFSL(SL,"channel.next_idp",True) # u'$channel.next_idp' on line 53, col 31
                if _v is not None: write(_filter(_v, rawExpr=u'$channel.next_idp')) # from line 53, col 31.
                write(u'''">''')
                _v = VFFSL(SL,"tstrings",True)['no_description_available'] # u"$tstrings['no_description_available']" on line 53, col 50
                if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['no_description_available']")) # from line 53, col 50.
                write(u'''</div>
</div>
''')
            write(u'''</tr></tbody></table>
''')
        write(u'''
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

    _mainCheetahMethod_for_channels= 'respond'

## END CLASS DEFINITION

if not hasattr(channels, '_initCheetahAttributes'):
    templateAPIClass = getattr(channels, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(channels)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=channels()).run()


