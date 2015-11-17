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
__CHEETAH_genTime__ = 1447321436.618305
__CHEETAH_genTimestamp__ = 'Thu Nov 12 18:43:56 2015'
__CHEETAH_src__ = '/home/knuth/openpli-oe-core/build/tmp/work/fusionhd-oe-linux/enigma2-plugin-extensions-openwebif/1+gitAUTOINC+5837c87afc-r0/git/plugin/controllers/views/ajax/epgr.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Nov 12 18:43:41 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class epgr(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(epgr, self).__init__(*args, **KWs)
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
        
        _orig_filter_29369579 = _filter
        filterName = u'WebSafe'
        if self._CHEETAH__filters.has_key("WebSafe"):
            _filter = self._CHEETAH__currentFilter = self._CHEETAH__filters[filterName]
        else:
            _filter = self._CHEETAH__currentFilter = \
			self._CHEETAH__filters[filterName] = getattr(self._CHEETAH__filtersLib, filterName)(self).filter
        write(u'''<style>
optgroup {font-weight: bolder;}
label
{
\t-webkit-margin-top-collapse: separate;
\tmargin-top: 1.5em;
\tdisplay: inline-block;
}
</style>
<div id="content_main" style="min-height: 500px;">
<div id="info">
<div style="background-color: #00000">
<div style="display: inline-block; width: 100%; zoom: 1;">
<h3>EPG Refresh</h3>
<div id="epgrefreshcontent">
\t<form>
\t<fieldset>
\t\t<label for="enabled">''')
        _v = VFFSL(SL,"tstrings",True)['er_enabled'] # u"$tstrings['er_enabled']" on line 20, col 24
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_enabled']")) # from line 20, col 24.
        write(u''':</label>
\t\t<input type="checkbox" name="er_enabled" id="er_enabled" value="" class="checkbox ui-widget-content ui-corner-all">
\t\t<br><label for="er_enablemessage">''')
        _v = VFFSL(SL,"tstrings",True)['er_enable_messages'] # u"$tstrings['er_enable_messages']" on line 22, col 37
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_enable_messages']")) # from line 22, col 37.
        write(u''':</label>
\t\t<input type="checkbox" name="er_enablemessage" id="er_enablemessage" value="" class="checkbox ui-widget-content ui-corner-all">
\t\t<br><label for="er_begin">''')
        _v = VFFSL(SL,"tstrings",True)['er_begin'] # u"$tstrings['er_begin']" on line 24, col 29
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_begin']")) # from line 24, col 29.
        write(u''':</label>
\t\t<input type="text" name="er_begin" id="er_begin" value="" class="text date ui-widget-content ui-corner-all">
\t\t<br><label for="er_end">''')
        _v = VFFSL(SL,"tstrings",True)['er_end'] # u"$tstrings['er_end']" on line 26, col 27
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_end']")) # from line 26, col 27.
        write(u''':</label>
\t\t<input type="text" name="er_end" id="er_end" value="" class="text date ui-widget-content ui-corner-all">
\t\t<br><label for="er_delay_standby">''')
        _v = VFFSL(SL,"tstrings",True)['er_delay_standby'] # u"$tstrings['er_delay_standby']" on line 28, col 37
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_delay_standby']")) # from line 28, col 37.
        write(u''':</label>
\t\t<input type="text" name="er_delay_standby" id="er_delay_standby" class="text ui-widget-content ui-corner-all">
\t\t<br><label id="lblm" for="er_interval">''')
        _v = VFFSL(SL,"tstrings",True)['er_interval_min'] # u"$tstrings['er_interval_min']" on line 30, col 42
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_interval_min']")) # from line 30, col 42.
        write(u''':</label><label id="lbls" for="er_interval">''')
        _v = VFFSL(SL,"tstrings",True)['er_interval_sec'] # u"$tstrings['er_interval_sec']" on line 30, col 114
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_interval_sec']")) # from line 30, col 114.
        write(u''':</label>
\t\t<input type="text" name="er_interval" id="er_interval" class="text ui-widget-content ui-corner-all">
\t\t<br><label for="er_afterevent">''')
        _v = VFFSL(SL,"tstrings",True)['er_afterevent'] # u"$tstrings['er_afterevent']" on line 32, col 34
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_afterevent']")) # from line 32, col 34.
        write(u''':</label>
\t\t<input type="checkbox" name="er_afterevent" id="er_afterevent" value="" class="checkbox ui-widget-content ui-corner-all">
\t\t<br><label for="er_force">''')
        _v = VFFSL(SL,"tstrings",True)['er_force'] # u"$tstrings['er_force']" on line 34, col 29
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_force']")) # from line 34, col 29.
        write(u''':</label>
\t\t<input type="checkbox" name="er_force" id="er_force" value="" class="checkbox ui-widget-content ui-corner-all">
\t\t<br><label for="er_wakeup">''')
        _v = VFFSL(SL,"tstrings",True)['er_wakeup'] # u"$tstrings['er_wakeup']" on line 36, col 30
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_wakeup']")) # from line 36, col 30.
        write(u''':</label>
\t\t<input type="checkbox" name="er_wakeup" id="er_wakeup" value="" class="checkbox ui-widget-content ui-corner-all">
\t\t<span id="er_hasAT"><br><label for="er_inherit_autotimer">''')
        _v = VFFSL(SL,"tstrings",True)['er_inherit_autotimer'] # u"$tstrings['er_inherit_autotimer']" on line 38, col 61
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_inherit_autotimer']")) # from line 38, col 61.
        write(u''':</label>
\t\t<input type="checkbox" name="er_inherit_autotimer" id="er_inherit_autotimer" value="" class="checkbox ui-widget-content ui-corner-all">
\t\t<br><label for="er_parse_autotimer">''')
        _v = VFFSL(SL,"tstrings",True)['er_parse_autotimer'] # u"$tstrings['er_parse_autotimer']" on line 40, col 39
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_parse_autotimer']")) # from line 40, col 39.
        write(u''':</label>
\t\t<select name="er_parse_autotimer" id="er_parse_autotimer">
\t\t<option value="always">''')
        _v = VFFSL(SL,"tstrings",True)['er_always'] # u"$tstrings['er_always']" on line 42, col 26
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_always']")) # from line 42, col 26.
        write(u'''</option>
\t\t<option value="never" selected="selected">''')
        _v = VFFSL(SL,"tstrings",True)['er_never'] # u"$tstrings['er_never']" on line 43, col 45
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_never']")) # from line 43, col 45.
        write(u'''</option>
\t\t<option value="bg_only">''')
        _v = VFFSL(SL,"tstrings",True)['er_bg_only'] # u"$tstrings['er_bg_only']" on line 44, col 27
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_bg_only']")) # from line 44, col 27.
        write(u'''</option>
\t\t<option value="ask_yes">''')
        _v = VFFSL(SL,"tstrings",True)['er_ask_yes'] # u"$tstrings['er_ask_yes']" on line 45, col 27
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_ask_yes']")) # from line 45, col 27.
        write(u'''</option>
\t\t<option value="ask_no">''')
        _v = VFFSL(SL,"tstrings",True)['er_ask_no'] # u"$tstrings['er_ask_no']" on line 46, col 26
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_ask_no']")) # from line 46, col 26.
        write(u'''</option>
\t\t</select>
\t\t</span><br><label for="er_adapter">''')
        _v = VFFSL(SL,"tstrings",True)['er_adapter'] # u"$tstrings['er_adapter']" on line 48, col 38
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_adapter']")) # from line 48, col 38.
        write(u''':</label>
\t\t<select name="er_adapter" id="er_adapter">
\t\t<option value="main" selected="selected">''')
        _v = VFFSL(SL,"tstrings",True)['er_main'] # u"$tstrings['er_main']" on line 50, col 44
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_main']")) # from line 50, col 44.
        write(u'''</option>
\t\t<option value="pip">''')
        _v = VFFSL(SL,"tstrings",True)['er_pip'] # u"$tstrings['er_pip']" on line 51, col 23
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_pip']")) # from line 51, col 23.
        write(u'''</option>
\t\t<option value="pip_hidden">''')
        _v = VFFSL(SL,"tstrings",True)['er_pip_hidden'] # u"$tstrings['er_pip_hidden']" on line 52, col 30
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_pip_hidden']")) # from line 52, col 30.
        write(u'''</option>
\t\t<option value="record">''')
        _v = VFFSL(SL,"tstrings",True)['er_fake_recording'] # u"$tstrings['er_fake_recording']" on line 53, col 26
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_fake_recording']")) # from line 53, col 26.
        write(u'''</option>
\t\t</select>
\t\t<br><label for="bouquets">''')
        _v = VFFSL(SL,"tstrings",True)['at_bouquets'] # u"$tstrings['at_bouquets']" on line 55, col 29
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['at_bouquets']")) # from line 55, col 29.
        write(u''':</label>
\t\t<select data-placeholder="''')
        _v = VFFSL(SL,"tstrings",True)['at_select_bouquets'] # u"$tstrings['at_select_bouquets']" on line 56, col 29
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['at_select_bouquets']")) # from line 56, col 29.
        write(u'''" name="bouquets" id="bouquets" class="bq_select_box" multiple tabindex="16">
\t\t</select>
\t\t<br><label for="channels">''')
        _v = VFFSL(SL,"tstrings",True)['at_channels'] # u"$tstrings['at_channels']" on line 58, col 29
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['at_channels']")) # from line 58, col 29.
        write(u''':</label>
\t\t<select data-placeholder="''')
        _v = VFFSL(SL,"tstrings",True)['at_select_channels'] # u"$tstrings['at_select_channels']" on line 59, col 29
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['at_select_channels']")) # from line 59, col 29.
        write(u'''" name="channels" id="channels" class="ch_select_box" multiple tabindex="16">
\t\t</select>
\t</fieldset>
\t</form>
\t<div class="ui-dialog-buttonpane ui-widget-content ui-helper-clearfix">
\t<div id="actions">
\t<button id="epgrbutton0">''')
        _v = VFFSL(SL,"tstrings",True)['er_reload'] # u"$tstrings['er_reload']" on line 65, col 27
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_reload']")) # from line 65, col 27.
        write(u'''</button>
\t<button id="epgrbutton1">''')
        _v = VFFSL(SL,"tstrings",True)['er_save'] # u"$tstrings['er_save']" on line 66, col 27
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_save']")) # from line 66, col 27.
        write(u'''</button>
\t<button id="epgrbutton2">''')
        _v = VFFSL(SL,"tstrings",True)['er_refresh'] # u"$tstrings['er_refresh']" on line 67, col 27
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['er_refresh']")) # from line 67, col 27.
        write(u'''</button>
\t</div></div>
\t<div id="errorbox" class="timerlist_row" style="color: red;">
\t<div class="ui-state-error ui-corner-all" style="padding: 0 .7em;"> 
\t<p><span class="ui-icon ui-icon-alert" style="float: left; margin-right: .3em;"></span> 
\t<span id="error"></span>
\t<span id="success" style="color: green;"></span>
\t</div>
</div>
</div>
</div>
</div>
</div>

<script type="text/javascript" src="js/jquery-ui-timepicker-addon.min.js"></script>
<script type="text/javascript" src="js/chosen.jquery.min.js"></script>
<script type="text/javascript" src="js/epgr.js"></script>
<script type="text/javascript">
$(function() { InitPage();});
</script>
<link rel="stylesheet" type="text/css" href="css/chosen.min.css" />
''')
        _filter = self._CHEETAH__currentFilter = _orig_filter_29369579
        
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

    _mainCheetahMethod_for_epgr= 'respond'

## END CLASS DEFINITION

if not hasattr(epgr, '_initCheetahAttributes'):
    templateAPIClass = getattr(epgr, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(epgr)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=epgr()).run()


