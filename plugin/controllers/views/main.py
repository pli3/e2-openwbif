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
from json import dumps

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1447321436.104418
__CHEETAH_genTimestamp__ = 'Thu Nov 12 18:43:56 2015'
__CHEETAH_src__ = '/home/knuth/openpli-oe-core/build/tmp/work/fusionhd-oe-linux/enigma2-plugin-extensions-openwebif/1+gitAUTOINC+5837c87afc-r0/git/plugin/controllers/views/main.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Nov 12 18:43:41 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class main(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(main, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def menu(self, title, name, content, **KWS):



        ## CHEETAH: generated from #def menu($title, $name, $content) at line 36, col 4.
        trans = KWS.get("trans")
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
        
        write(u'''\t\t\t<div id="leftmenu_main">\r
\t\t\t\t<div id="leftmenu_top">\r
\t\t\t\t\t''')
        _v = VFFSL(SL,"title",True) # u'$title' on line 39, col 6
        if _v is not None: write(_filter(_v, rawExpr=u'$title')) # from line 39, col 6.
        write(u'''\r
''')
        if VFFSL(SL,"name",True) in VFFSL(SL,"collapsed",True): # generated from line 40, col 6
            write(u'''\t\t\t\t\t<div id="leftmenu_expander_''')
            _v = VFFSL(SL,"name",True) # u'$name' on line 41, col 33
            if _v is not None: write(_filter(_v, rawExpr=u'$name')) # from line 41, col 33.
            write(u'''" class="leftmenu_icon leftmenu_icon_collapse" onclick="toggleMenu(\'''')
            _v = VFFSL(SL,"name",True) # u'$name' on line 41, col 106
            if _v is not None: write(_filter(_v, rawExpr=u'$name')) # from line 41, col 106.
            write(u'''\');"></div>\r
''')
        else: # generated from line 42, col 6
            write(u'''\t\t\t\t\t<div id="leftmenu_expander_''')
            _v = VFFSL(SL,"name",True) # u'$name' on line 43, col 33
            if _v is not None: write(_filter(_v, rawExpr=u'$name')) # from line 43, col 33.
            write(u'''" class="leftmenu_icon" onclick="toggleMenu(\'''')
            _v = VFFSL(SL,"name",True) # u'$name' on line 43, col 83
            if _v is not None: write(_filter(_v, rawExpr=u'$name')) # from line 43, col 83.
            write(u'''\');"></div>\r
''')
        write(u'''\t\t\t\t</div>\r
''')
        if VFFSL(SL,"name",True) in VFFSL(SL,"collapsed",True): # generated from line 46, col 5
            write(u'''\t\t\t\t<div id="leftmenu_container_''')
            _v = VFFSL(SL,"name",True) # u'$name' on line 47, col 33
            if _v is not None: write(_filter(_v, rawExpr=u'$name')) # from line 47, col 33.
            write(u'''" style="display: none;">\r
''')
        else: # generated from line 48, col 5
            write(u'''\t\t\t\t<div id="leftmenu_container_''')
            _v = VFFSL(SL,"name",True) # u'$name' on line 49, col 33
            if _v is not None: write(_filter(_v, rawExpr=u'$name')) # from line 49, col 33.
            write(u'''">\r
''')
        write(u'''\t\t\t\t''')
        _v = VFFSL(SL,"content",True) # u'$content' on line 51, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$content')) # from line 51, col 5.
        write(u'''\r
\t\t\t\t</div>\r
\t\t\t</div>\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def mainMenu(self, **KWS):



        ## CHEETAH: generated from #def mainMenu at line 56, col 4.
        trans = KWS.get("trans")
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
        
        write(u'''\t\t\t<ul>\r
\t\t\t\t<li><a href=\'#\' onclick="load_maincontent(\'ajax/tv\'); return false;">''')
        _v = VFFSL(SL,"tstrings",True)['television'] # u"$tstrings['television']" on line 58, col 74
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['television']")) # from line 58, col 74.
        write(u'''</a></li>\r
\t\t\t\t<li><a href=\'#\' onclick="load_maincontent(\'ajax/radio\'); return false;">''')
        _v = VFFSL(SL,"tstrings",True)['radio'] # u"$tstrings['radio']" on line 59, col 77
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['radio']")) # from line 59, col 77.
        write(u"""</a></li>\r
\t\t\t\t<li><a href='ajax/multiepg2' target=_blank>""")
        _v = VFFSL(SL,"tstrings",True)['tv_multi_epg'] # u"$tstrings['tv_multi_epg']" on line 60, col 48
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['tv_multi_epg']")) # from line 60, col 48.
        write(u'''</a></li>\r
\t\t\t</ul>\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def volumeMenu(self, **KWS):



        ## CHEETAH: generated from #def volumeMenu at line 64, col 4.
        trans = KWS.get("trans")
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
        
        write(u'''\t\t\t<div class="volslider">\r
\t\t\t\t\t<p style="text-align:center; padding-bottom:8px;"> \r
\t\t\t\t\t\t<label for="amount">''')
        _v = VFFSL(SL,"tstrings",True)['volume'] # u"$tstrings['volume']" on line 67, col 27
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['volume']")) # from line 67, col 27.
        write(u''':</label>\r
\t\t\t\t\t\t<input type="text" id="amount" style="border:0; color:#f6931f; font-weight:bold; width:40px;" />\r
\t\t\t\t\t</p>\r
\t\t\t\t<div id="slider" style="width:130px;"></div>\r
\t\t\t</div>\r
\t\t\t<div style="width:100%; text-align:center; padding-top:5px; padding-bottom:10px;"><img id="volimage" src="images/volume.png" title="" border="0" width="48" height="48"></div>\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def controlMenu(self, **KWS):



        ## CHEETAH: generated from #def controlMenu at line 75, col 4.
        trans = KWS.get("trans")
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
        
        write(u'''\t\t\t<ul>\r
\t\t\t\t<li><a href=\'#\' onclick="load_dm(\'ajax/powerstate\',\'''')
        _v = VFFSL(SL,"tstrings",True)["powercontrol"] # u'$tstrings["powercontrol"]' on line 77, col 57
        if _v is not None: write(_filter(_v, rawExpr=u'$tstrings["powercontrol"]')) # from line 77, col 57.
        write(u'''\'); return false;">''')
        _v = VFFSL(SL,"tstrings",True)['powercontrol'] # u"$tstrings['powercontrol']" on line 77, col 101
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['powercontrol']")) # from line 77, col 101.
        write(u'''</a></li>\r
\t\t\t\t<li><a href=\'#\' onclick="load_maincontent(\'ajax/screenshot\'); return false;">''')
        _v = VFFSL(SL,"tstrings",True)['grabscreenshot'] # u"$tstrings['grabscreenshot']" on line 78, col 82
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['grabscreenshot']")) # from line 78, col 82.
        write(u'''</a></li>\r
\t\t\t\t<li><a href=\'#\' onclick="load_message_dm(\'ajax/message\',\'''')
        _v = VFFSL(SL,"tstrings",True)["sendamessage"] # u'$tstrings["sendamessage"]' on line 79, col 62
        if _v is not None: write(_filter(_v, rawExpr=u'$tstrings["sendamessage"]')) # from line 79, col 62.
        write(u'''\'); return false;">''')
        _v = VFFSL(SL,"tstrings",True)['sendamessage'] # u"$tstrings['sendamessage']" on line 79, col 106
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['sendamessage']")) # from line 79, col 106.
        write(u'''</a></li>\r
\t\t\t\t<li><a href=\'#\' onclick="load_maincontent(\'ajax/timers\'); return false;">''')
        _v = VFFSL(SL,"tstrings",True)['timers'] # u"$tstrings['timers']" on line 80, col 78
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['timers']")) # from line 80, col 78.
        write(u'''</a></li>\r
\t\t\t</ul>\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def infoMenu(self, **KWS):



        ## CHEETAH: generated from #def infoMenu at line 84, col 4.
        trans = KWS.get("trans")
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
        
        write(u'''\t\t\t<ul>\r
\t\t\t\t<li><a href="#" onclick="load_maincontent(\'ajax/boxinfo\'); return false">''')
        _v = VFFSL(SL,"tstrings",True)['box_info'] # u"$tstrings['box_info']" on line 86, col 78
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['box_info']")) # from line 86, col 78.
        write(u'''</a></li>\r
\t\t\t\t<li><a href="#" onclick="load_maincontent(\'ajax/about\'); return false">''')
        _v = VFFSL(SL,"tstrings",True)['about'] # u"$tstrings['about']" on line 87, col 76
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['about']")) # from line 87, col 76.
        write(u'''</a></li>\r
\t\t\t</ul>\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def streamMenu(self, **KWS):



        ## CHEETAH: generated from #def streamMenu at line 91, col 4.
        trans = KWS.get("trans")
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
        
        write(u'''\t\t\t<ul>\r
\t\t\t\t<li><a href=\'#\' onclick="load_maincontent_spin(\'ajax/movies\'); return false;">''')
        _v = VFFSL(SL,"tstrings",True)['movies'] # u"$tstrings['movies']" on line 93, col 83
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['movies']")) # from line 93, col 83.
        write(u'''</a></li>\r
 <!--\t\t\t\t<li><a href=\'#\' onclick="load_maincontent(\'ajax/workinprogress\'); return false;">Web Tv</a></li> -->\r
''')
        if VFFSL(SL,"zapstream",True): # generated from line 95, col 5
            write(u'''\t\t\t\t<li><input type="checkbox" name="zapstream" checked="checked" />''')
            _v = VFFSL(SL,"tstrings",True)['zapbeforestream'] # u"$tstrings['zapbeforestream']" on line 96, col 69
            if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['zapbeforestream']")) # from line 96, col 69.
            write(u'''</li>\r
''')
        else: # generated from line 97, col 5
            write(u'''\t\t\t\t<li><input type="checkbox" name="zapstream" />''')
            _v = VFFSL(SL,"tstrings",True)['zapbeforestream'] # u"$tstrings['zapbeforestream']" on line 98, col 51
            if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['zapbeforestream']")) # from line 98, col 51.
            write(u'''</li>\r
''')
        write(u'''\t\t\t</ul>\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def searchMenu(self, **KWS):



        ## CHEETAH: generated from #def searchMenu at line 103, col 4.
        trans = KWS.get("trans")
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
        
        if VFFSL(SL,"epgsearchcaps",True): # generated from line 104, col 4
            write(u'''\t\t\t<ul>\r
''')
            if VFFSL(SL,"epgsearchtype",True): # generated from line 106, col 5
                write(u'''\t\t\t\t<li><input type="checkbox" name="epgsearchtype" checked="checked" />''')
                _v = VFFSL(SL,"tstrings",True)['epgsearchextended'] # u"$tstrings['epgsearchextended']" on line 107, col 73
                if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['epgsearchextended']")) # from line 107, col 73.
                write(u'''</li>\r
''')
            else: # generated from line 108, col 5
                write(u'''\t\t\t\t<li><input type="checkbox" name="epgsearchtype" />''')
                _v = VFFSL(SL,"tstrings",True)['epgsearchextended'] # u"$tstrings['epgsearchextended']" on line 109, col 55
                if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['epgsearchextended']")) # from line 109, col 55.
                write(u'''</li>\r
''')
            write(u'''\t\t\t</ul>\r
''')
        write(u'''\t\t\t<form action="" onSubmit="open_epg_search_dialog(); return false;">\r
\t\t\t\t<div style="width:100%; text-align:center; padding-top:5px;"><input type="text" id="epgSearch" size="14" /></div>\r
\t\t\t\t<div style="width:100%; text-align:center;padding-top:5px; padding-bottom:7px;" class="epgsearch"><button>''')
        _v = VFFSL(SL,"tstrings",True)['search'] # u"$tstrings['search']" on line 115, col 111
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['search']")) # from line 115, col 111.
        write(u'''</button></div>\r
\t\t\t</form>\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def remoteMenu(self, **KWS):



        ## CHEETAH: generated from #def remoteMenu at line 119, col 4.
        trans = KWS.get("trans")
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
        
        write(u'''\t\t\t<div style="width:100%; text-align:center;">\r
\t\t\t\t<img src="images/remotes/ow_remote.png" width="135" height="183" usemap="#menuremote" border="0">\r
\t\t\t\t<map name="menuremote" >\r
\t\t\t\t\t<area shape="circle" coords="67,148,13" alt="ok" onclick="pressMenuRemote(\'352\');">\r
\t\t\t\t\t<area shape="circle" coords="68,173,9" alt="down" onclick="pressMenuRemote(\'108\');">\r
\t\t\t\t\t<area shape="circle" coords="44,148,9" alt="left" onclick="pressMenuRemote(\'105\');">\r
\t\t\t\t\t<area shape="circle" coords="92,147,9" alt="right" onclick="pressMenuRemote(\'106\');">\r
\t\t\t\t\t<area shape="circle" coords="68,126,8" alt="up" onclick="pressMenuRemote(\'103\');">\r
\t\t\t\t\t<area shape="circle" coords="117,163,10" alt="blue" onclick="pressMenuRemote(\'401\');">\r
\t\t\t\t\t<area shape="circle" coords="118,132,11" alt="yellow" onclick="pressMenuRemote(\'400\');">\r
\t\t\t\t\t<area shape="circle" coords="18,163,11" alt="green" onclick="pressMenuRemote(\'399\');">\r
\t\t\t\t\t<area shape="circle" coords="19,133,10" alt="red" onclick="pressMenuRemote(\'398\');">\r
\t\t\t\t\t<area shape="rect" coords="5,89,44,117" alt="menu" onclick="pressMenuRemote(\'139\');">\r
\t\t\t\t\t<area shape="rect" coords="90,89,128,117" alt="exit" onclick="pressMenuRemote(\'174\');">\r
\t\t\t\t\t<area shape="rect" coords="47,89,87,117" alt="0" onclick="pressMenuRemote(\'11\');">\r
\t\t\t\t\t<area shape="rect" coords="90,60,128,86" alt="9" onclick="pressMenuRemote(\'10\');">\r
\t\t\t\t\t<area shape="rect" coords="47,60,87,86" alt="8" onclick="pressMenuRemote(\'9\');">\r
\t\t\t\t\t<area shape="rect" coords="4,60,44,86" alt="7" onclick="pressMenuRemote(\'8\');">\r
\t\t\t\t\t<area shape="rect" coords="90,30,129,57" alt="6" onclick="pressMenuRemote(\'7\');">\r
\t\t\t\t\t<area shape="rect" coords="47,30,87,57" alt="5" onclick="pressMenuRemote(\'6\');">\r
\t\t\t\t\t<area shape="rect" coords="4,30,44,57" alt="4" onclick="pressMenuRemote(\'5\');">\r
\t\t\t\t\t<area shape="rect" coords="90,0,129,27" alt="3" onclick="pressMenuRemote(\'4\');">\r
\t\t\t\t\t<area shape="rect" coords="46,0,88,28" alt="2" onclick="pressMenuRemote(\'3\');">\r
\t\t\t\t\t<area shape="rect" coords="5,0,45,28" alt="1" onclick="pressMenuRemote(\'2\');">\r
\t\t\t\t</map>\r
\t\t\t\t<div id="help">\r
\t\t\t\t\t''')
        _v = VFFSL(SL,"tstrings",True)['shiftforlong'] # u"$tstrings['shiftforlong']" on line 146, col 6
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['shiftforlong']")) # from line 146, col 6.
        write(u'''\r
\t\t\t\t</div>\r
\t\t\t\t<ul>\r
''')
        if VFFSL(SL,"remotegrabscreenshot",True): # generated from line 149, col 6
            write(u'''\t\t\t\t\t<li><input type="checkbox" name="remotegrabscreen" checked="checked" />''')
            _v = VFFSL(SL,"tstrings",True)['grabscreenshot'] # u"$tstrings['grabscreenshot']" on line 150, col 77
            if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['grabscreenshot']")) # from line 150, col 77.
            write(u'''</li>\r
''')
        else: # generated from line 151, col 6
            write(u'''\t\t\t\t\t<li><input type="checkbox" name="remotegrabscreen" />''')
            _v = VFFSL(SL,"tstrings",True)['grabscreenshot'] # u"$tstrings['grabscreenshot']" on line 152, col 59
            if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['grabscreenshot']")) # from line 152, col 59.
            write(u'''</li>\r
''')
        write(u'''\t\t\t\t\t<li><a href="#" onclick="toggleFullRemote(); return false;">''')
        _v = VFFSL(SL,"tstrings",True)['showfullremote'] # u"$tstrings['showfullremote']" on line 154, col 66
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['showfullremote']")) # from line 154, col 66.
        write(u'''</a></li>\r
\t\t\t\t</ul>\r
\t\t\t</div>\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def extrasMenu(self, **KWS):



        ## CHEETAH: generated from #def extrasMenu at line 159, col 4.
        trans = KWS.get("trans")
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
        
        write(u'''\t\t\t<ul>\r
''')
        for extra in VFFSL(SL,"extras",True): # generated from line 161, col 5
            if VFN(VFFSL(SL,"extra",True)["key"],"endswith",False)('lcd4linux/config'): # generated from line 162, col 6
                write(u"""\t\t\t\t\t\t<li><a href='""")
                _v = VFFSL(SL,"extra",True)["key"] # u'$extra["key"]' on line 163, col 20
                if _v is not None: write(_filter(_v, rawExpr=u'$extra["key"]')) # from line 163, col 20.
                write(u"""' target='_blank'>""")
                _v = VFFSL(SL,"extra",True)["description"] # u'$extra["description"]' on line 163, col 51
                if _v is not None: write(_filter(_v, rawExpr=u'$extra["description"]')) # from line 163, col 51.
                write(u'''</a></li>\r
''')
            else: # generated from line 164, col 6
                write(u'''\t\t\t\t\t\t<li><a href=\'#\' onclick="load_maincontent(\'''')
                _v = VFFSL(SL,"extra",True)["key"] # u'$extra["key"]' on line 165, col 50
                if _v is not None: write(_filter(_v, rawExpr=u'$extra["key"]')) # from line 165, col 50.
                write(u'''\'); return false;">''')
                _v = VFFSL(SL,"extra",True)["description"] # u'$extra["description"]' on line 165, col 82
                if _v is not None: write(_filter(_v, rawExpr=u'$extra["description"]')) # from line 165, col 82.
                write(u'''</a></li>\r
''')
        write(u'''\t\t\t</ul>\r
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

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
        
        write(u'''\r
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r
<html xmlns="http://www.w3.org/1999/xhtml">\r
<head>\r
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\r
<link rel="shortcut icon" href="images/favicon.png">\r
<link rel="stylesheet" type="text/css" href="css/style.css" />\r
<link type="text/css" href="css/jquery-ui-1.8.18.custom.css" rel="stylesheet" />\t\r
<script type="text/javascript" src="js/jquery-1.6.2.min.js"></script>\r
<script type="text/javascript" src="js/jquery-ui-1.8.18.custom.min.js"></script>\r
<script type="text/javascript" src="js/openwebif.js"></script>\r
<script type="text/javascript">initJsTranslation(''')
        _v = VFFSL(SL,"dumps",False)(VFFSL(SL,"tstrings",True)) # u'$dumps($tstrings)' on line 14, col 50
        if _v is not None: write(_filter(_v, rawExpr=u'$dumps($tstrings)')) # from line 14, col 50.
        write(u''')</script>\r
<title>Open Webif</title>\r
</head>\r
\r
<body>\r
\t<div id="container">\r
\t\t<div id="header">\r
\t\t\t<h1><a href="/">Open<span class="off">Webif</span></a></h1>\r
''')
        if VFFSL(SL,"showname",True): # generated from line 22, col 4
            write(u'''\t\t\t<h2>''')
            _v = VFFSL(SL,"tstrings",True)['openwebif_header'] # u"$tstrings['openwebif_header']" on line 23, col 8
            if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['openwebif_header']")) # from line 23, col 8.
            write(u'''<br /><span class="off">''')
            _v = VFFSL(SL,"boxname",True) # u'$boxname' on line 23, col 61
            if _v is not None: write(_filter(_v, rawExpr=u'$boxname')) # from line 23, col 61.
            write(u'''</span></h2>\r
''')
        else: # generated from line 24, col 4
            write(u'''\t\t\t<h2>''')
            _v = VFFSL(SL,"tstrings",True)['openwebif_header'] # u"$tstrings['openwebif_header']" on line 25, col 8
            if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['openwebif_header']")) # from line 25, col 8.
            write(u'''</h2>\r
''')
        write(u'''\t\t</div>\r
\t\t\r
\t\t<div id="statusheader">\r
\t\t\t<div id="osd">''')
        _v = VFFSL(SL,"tstrings",True)['nothing_play'] # u"$tstrings['nothing_play']" on line 30, col 18
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['nothing_play']")) # from line 30, col 18.
        write(u'''</div>\r
\t\t\t<div id="osd_status"></div>\r
\t\t\t<div id="osd_bottom"></div>\r
\t\t</div>\r
\t\t\r
\t\t<div id="leftmenu">\r
\t\t\r
\t\t\r
\r
\t\t\r
\t\t\r
\t\t\r
\t\t\t\r
\t\t\t\r
\t\t\r
\t\t\t<div id="menucontainer">\r
\t\t\t\t''')
        _v = VFFSL(SL,"menu",False)(VFFSL(SL,"tstrings",True)['main'], "main", VFFSL(SL,"mainMenu",True)) # u'$menu($tstrings[\'main\'], "main", $mainMenu)' on line 172, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$menu($tstrings[\'main\'], "main", $mainMenu)')) # from line 172, col 5.
        write(u'''\r
\t\t\t\t''')
        _v = VFFSL(SL,"menu",False)(VFFSL(SL,"tstrings",True)['volumecontrol'], "volume", VFFSL(SL,"volumeMenu",True)) # u'$menu($tstrings[\'volumecontrol\'], "volume", $volumeMenu)' on line 173, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$menu($tstrings[\'volumecontrol\'], "volume", $volumeMenu)')) # from line 173, col 5.
        write(u'''\r
\t\t\t\t''')
        _v = VFFSL(SL,"menu",False)(VFFSL(SL,"tstrings",True)['boxcontrol'], "control", VFFSL(SL,"controlMenu",True)) # u'$menu($tstrings[\'boxcontrol\'], "control", $controlMenu)' on line 174, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$menu($tstrings[\'boxcontrol\'], "control", $controlMenu)')) # from line 174, col 5.
        write(u'''\r
\t\t\t\t''')
        _v = VFFSL(SL,"menu",False)(VFFSL(SL,"tstrings",True)['remote'], "remote", VFFSL(SL,"remoteMenu",True)) # u'$menu($tstrings[\'remote\'], "remote", $remoteMenu)' on line 175, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$menu($tstrings[\'remote\'], "remote", $remoteMenu)')) # from line 175, col 5.
        write(u'''\r
\t\t\t\t''')
        _v = VFFSL(SL,"menu",False)(VFFSL(SL,"tstrings",True)['info'], "info", VFFSL(SL,"infoMenu",True)) # u'$menu($tstrings[\'info\'], "info", $infoMenu)' on line 176, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$menu($tstrings[\'info\'], "info", $infoMenu)')) # from line 176, col 5.
        write(u'''\r
\t\t\t\t''')
        _v = VFFSL(SL,"menu",False)(VFFSL(SL,"tstrings",True)['stream'], "stream", VFFSL(SL,"streamMenu",True)) # u'$menu($tstrings[\'stream\'], "stream", $streamMenu)' on line 177, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$menu($tstrings[\'stream\'], "stream", $streamMenu)')) # from line 177, col 5.
        write(u'''\r
\t\t\t\t''')
        _v = VFFSL(SL,"menu",False)(VFFSL(SL,"tstrings",True)['extras'], "extras", VFFSL(SL,"extrasMenu",True)) # u'$menu($tstrings[\'extras\'], "extras", $extrasMenu)' on line 178, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$menu($tstrings[\'extras\'], "extras", $extrasMenu)')) # from line 178, col 5.
        write(u'''\r
\t\t\t\t''')
        _v = VFFSL(SL,"menu",False)(VFFSL(SL,"tstrings",True)['epgsearch'], "search", VFFSL(SL,"searchMenu",True)) # u'$menu($tstrings[\'epgsearch\'], "search", $searchMenu)' on line 179, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$menu($tstrings[\'epgsearch\'], "search", $searchMenu)')) # from line 179, col 5.
        write(u'''\r
\t\t\t</div>\r
\t\t\t<div id="remotecontainer" style="display: none;">\r
\t\t\t\t<div id="leftmenu_main">\r
\t\t\t\t\t<div id="leftmenu_top">''')
        _v = VFFSL(SL,"tstrings",True)['remote'] # u"$tstrings['remote']" on line 183, col 29
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['remote']")) # from line 183, col 29.
        write(u'''</div>\r
\t\t\t\t\t<div style="width:100%; text-align:center;">\r
\t\t\t\t\t\t<div id="remote_container" style="width:100%; text-align:center;"></div>\r
\t\t\t\t\t\t<script type="text/javascript">\r
\t\t\t\t\t\t\t$(document).ready(function() {\r
\t\t\t\t\t\t\t\t$("#remote_container").load("static/remotes/''')
        _v = VFFSL(SL,"remote",True) # u'${remote}' on line 188, col 54
        if _v is not None: write(_filter(_v, rawExpr=u'${remote}')) # from line 188, col 54.
        write(u'''.html");\r
\t\t\t\t\t\t\t});\r
\t\t\t\t\t\t</script>\r
\t\t\t\t\t\t<div id="help">\r
\t\t\t\t\t\t\t''')
        _v = VFFSL(SL,"tstrings",True)['shiftforlong'] # u"$tstrings['shiftforlong']" on line 192, col 8
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['shiftforlong']")) # from line 192, col 8.
        write(u'''\r
\t\t\t\t\t\t</div>\r
\t\t\t\t\t\t<ul>\r
''')
        if VFFSL(SL,"remotegrabscreenshot",True): # generated from line 195, col 8
            write(u'''\t\t\t\t\t\t\t<li><input type="checkbox" name="remotegrabscreen" checked="checked" />''')
            _v = VFFSL(SL,"tstrings",True)['grabscreenshot'] # u"$tstrings['grabscreenshot']" on line 196, col 79
            if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['grabscreenshot']")) # from line 196, col 79.
            write(u'''</li>\r
''')
        else: # generated from line 197, col 8
            write(u'''\t\t\t\t\t\t\t<li><input type="checkbox" name="remotegrabscreen" />''')
            _v = VFFSL(SL,"tstrings",True)['grabscreenshot'] # u"$tstrings['grabscreenshot']" on line 198, col 61
            if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['grabscreenshot']")) # from line 198, col 61.
            write(u'''</li>\r
''')
        write(u'''\t\t\t\t\t\t\t<li><a href="#" onclick="toggleFullRemote(); return false;" class="leftmenu_remotelink">''')
        _v = VFFSL(SL,"tstrings",True)['hidefullremote'] # u"$tstrings['hidefullremote']" on line 200, col 96
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['hidefullremote']")) # from line 200, col 96.
        write(u'''</a></li>\r
\t\t\t\t\t\t</ul>\r
\t\t\t\t\t</div>\r
\t\t\t\t</div>\r
\t\t\t</div>\r
\t\t</div>\r
\t\t\r
\t\t<div id="content">\r
\t\t\t<div id="content_container">\r
\t\t\t''')
        _v = VFFSL(SL,"content",True) # u'$content' on line 209, col 4
        if _v is not None: write(_filter(_v, rawExpr=u'$content')) # from line 209, col 4.
        write(u'''\r
\t\t\t</div>\r
\t\t\t<div id="footer"><h3>&nbsp;&nbsp;<a href="https://github.com/E2OpenPlugins">E2OpenPlugins</a> | <a href="http://www.opena.tv">openATV</a> | <a href="http://www.vuplus-community.net">Black Hole</a> | <a href="http://www.egami-image.com">EGAMI</a> | <a href="http://www.hdfreaks.cc">OpenHDF</a> | <a href="http://www.hdmedia-universe.com">HDMU</a> | <a href="http://openpli.org">OpenPli</a> | <a href="http://forum.sifteam.eu">Sif</a> | <a href="http://openspa.info">OpenSpa</a> | <a href="http://www.world-of-satellite.com">OpenViX</a> | <a href="http://www.droidsat.org">OpenDroid</a> | <a href="http://www.vuplus-support.org">VTi</a></h3></div>\r
\t\t</div>\r
\t</div>\r
\t<form name="portForm" action="web/stream.m3u" method="GET" target="_blank">\r
\t\t<input type="hidden" name="ref">\r
\t\t<input type="hidden" name="name">\r
\t\t<input type="hidden" name="device">\r
\t</form>\r
\t<form name="portFormTs" action="web/ts.m3u" method="GET" target="_blank">\r
\t\t<input type="hidden" name="file">\r
\t\t<input type="hidden" name="device">\r
\t</form>\r
\t<div id="modaldialog"></div>\r
\t<div id="dialog" title="Work in progress" style="display:none">\r
\t\t<p>Sorry, this function is not yet implemented.</p>\r
\t</div>\r
\t<div id="editTimerForm" title="''')
        _v = VFFSL(SL,"tstrings",True)['edit_timer'] # u"$tstrings['edit_timer']" on line 227, col 33
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['edit_timer']")) # from line 227, col 33.
        write(u'''"></div>\r
\t\r
</body>\r
\r
</html>\r
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

    _mainCheetahMethod_for_main= 'respond'

## END CLASS DEFINITION

if not hasattr(main, '_initCheetahAttributes'):
    templateAPIClass = getattr(main, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(main)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=main()).run()


