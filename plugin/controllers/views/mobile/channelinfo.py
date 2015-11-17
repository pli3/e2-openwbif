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
from urllib import quote
from Plugins.Extensions.OpenWebif.local import tstrings

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.4'
__CHEETAH_versionTuple__ = (2, 4, 4, 'development', 0)
__CHEETAH_genTime__ = 1447321436.325169
__CHEETAH_genTimestamp__ = 'Thu Nov 12 18:43:56 2015'
__CHEETAH_src__ = '/home/knuth/openpli-oe-core/build/tmp/work/fusionhd-oe-linux/enigma2-plugin-extensions-openwebif/1+gitAUTOINC+5837c87afc-r0/git/plugin/controllers/views/mobile/channelinfo.tmpl'
__CHEETAH_srcLastModified__ = 'Thu Nov 12 18:43:41 2015'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class channelinfo(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(channelinfo, self).__init__(*args, **KWs)
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
        
        write(u'''<html>\r
 <head>\r
\t<title>OpenWebif</title>\r
\t<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\r
\t<meta name="viewport" content="user-scalable=no, width=device-width"/>\r
\t<meta name="apple-mobile-web-app-capable" content="yes" />\r
\t<link rel="stylesheet" type="text/css" href="/css/jquery.mobile-1.0.min.css" media="screen"/>\r
\t<link rel="stylesheet" type="text/css" href="/css/iphone.css" media="screen"/>\r
\t<script src="/js/jquery-1.6.2.min.js"></script>\r
\t<script src="/js/jquery.mobile-1.0.min.js"></script>\r
 </head>\r
 <body> \r
\t<div data-role="page">\r
\r
\t\t<div id="header">\r
\t\t\t<div class="button" onClick="history.back()">''')
        _v = VFFSL(SL,"tstrings",True)['back'] # u"$tstrings['back']" on line 18, col 49
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['back']")) # from line 18, col 49.
        write(u'''</div>\r
\t\t\t<h1><a style="color:#FFF;text-decoration:none;" href=\'/mobile\'>OpenWebif</a></h1>
''')
        link = quote('/mobile/channelzap?sref=' + VFFSL(SL,"channelinfo.sref",True), safe=' ~@#$&()*!+=:;,.?/\'')
        write(u'''\t\t\t<div class="button" style="right:5px;left:auto;" onClick="window.open(\'''')
        _v = VFFSL(SL,"link",True) # u'$link' on line 21, col 75
        if _v is not None: write(_filter(_v, rawExpr=u'$link')) # from line 21, col 75.
        write(u'''\');return false;">''')
        _v = VFFSL(SL,"tstrings",True)['zap'] # u"$tstrings['zap']" on line 21, col 98
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['zap']")) # from line 21, col 98.
        write(u'''</div>\r
\t\t</div>\r
\t\t<div id="mainContent" class="ui-corner-all">\r
\t\t\t<table width="100%" border="0" cellspacing="1" cellpadding="5">\r
\t\t\t\t\t\t<tr>\r
\t\t\t\t\t\t\t<th colspan="3" class="ui-btn-up-b" style="text-align: left;">''')
        _v = VFFSL(SL,"tstrings",True)['service'] # u"$tstrings['service']" on line 26, col 70
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['service']")) # from line 26, col 70.
        write(u'''</th>\r
\t\t\t\t\t\t</tr>\r
\t\t\t\t\t\t<tr style="background-color:  #f0f7fc;">\r
\t\t\t\t\t\t\t<td width="200"><img src="''')
        _v = VFFSL(SL,"channelinfo.picon",True) # u'$channelinfo.picon' on line 29, col 34
        if _v is not None: write(_filter(_v, rawExpr=u'$channelinfo.picon')) # from line 29, col 34.
        write(u'''" border="0" alt=""></td>\r
\t\t\t\t\t\t\t<td width="100%" valign="top">\r
\t\t\t\t\t\t\t<strong>''')
        _v = VFFSL(SL,"channelinfo.sname",True) # u'$channelinfo.sname' on line 31, col 16
        if _v is not None: write(_filter(_v, rawExpr=u'$channelinfo.sname')) # from line 31, col 16.
        write(u'''</strong><br />\r
''')
        if VFFSL(SL,"channelinfo.title",True): # generated from line 32, col 8
            write(u'''\t\t\t\t\t\t\t\t''')
            _v = VFFSL(SL,"channelinfo.title",True) # u'$channelinfo.title' on line 33, col 9
            if _v is not None: write(_filter(_v, rawExpr=u'$channelinfo.title')) # from line 33, col 9.
            write(u'''<br />\r
\t\t\t\t\t\t\t\t''')
            _v = VFFSL(SL,"channelinfo.begin",True) # u'$channelinfo.begin' on line 34, col 9
            if _v is not None: write(_filter(_v, rawExpr=u'$channelinfo.begin')) # from line 34, col 9.
            write(u'''-''')
            _v = VFFSL(SL,"channelinfo.end",True) # u'$channelinfo.end' on line 34, col 28
            if _v is not None: write(_filter(_v, rawExpr=u'$channelinfo.end')) # from line 34, col 28.
            write(u''' (''')
            _v = VFFSL(SL,"channelinfo.duration",True) # u'$channelinfo.duration' on line 34, col 46
            if _v is not None: write(_filter(_v, rawExpr=u'$channelinfo.duration')) # from line 34, col 46.
            write(u''' min)<br />\r
''')
        write(u'''\t\t\t\t\t\t\t</td>\r
\t\t\t\t\t\t</tr>\r
\t\t\t\t\t\t<tr>\r
\t\t\t\t\t\t\t<th colspan="2" class="ui-btn-up-b" style="text-align: left;">''')
        _v = VFFSL(SL,"tstrings",True)['current_event'] # u"$tstrings['current_event']" on line 39, col 70
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['current_event']")) # from line 39, col 70.
        write(u'''</th>\r
\t\t\t\t\t\t</tr>\r
''')
        if VFN(VFFSL(SL,"channelinfo",True),"has_key",False)('shortdesc'): # generated from line 41, col 7
            write(u'''\t\t\t\t\t\t<tr style="background-color:  #f0f7fc;">\r
\t\t\t\t\t\t\t<td colspan="2">''')
            _v = VFFSL(SL,"channelinfo.shortdesc",True) # u'$channelinfo.shortdesc' on line 43, col 24
            if _v is not None: write(_filter(_v, rawExpr=u'$channelinfo.shortdesc')) # from line 43, col 24.
            write(u'''</td>\r
\t\t\t\t\t\t</tr>\r
''')
        if VFN(VFFSL(SL,"channelinfo",True),"has_key",False)('longdesc'): # generated from line 46, col 7
            write(u'''\t\t\t\t\t\t<tr style="background-color:  #f0f7fc;">\r
\t\t\t\t\t\t\t<td colspan="2">''')
            _v = VFFSL(SL,"channelinfo.longdesc",True) # u'$channelinfo.longdesc' on line 48, col 24
            if _v is not None: write(_filter(_v, rawExpr=u'$channelinfo.longdesc')) # from line 48, col 24.
            write(u'''</td>\r
\t\t\t\t\t\t</tr>\r
''')
        write(u'''\t\t\t</table>\r
\t\t</div>\r
\t\t\r
''')
        if VFFSL(SL,"channelepg",True): # generated from line 54, col 3
            write(u'''\t\t<div id="contentContainer">\r
\t\t\t<ul data-role="listview" data-inset="true" data-theme="d">\r
\t\t\t\t<li data-role="list-divider" role="heading" data-theme="b">''')
            _v = VFFSL(SL,"tstrings",True)['upcoming_events'] # u"$tstrings['upcoming_events']" on line 57, col 64
            if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['upcoming_events']")) # from line 57, col 64.
            write(u'''</li>\r
''')
            for event in VFFSL(SL,"channelepg",True): # generated from line 58, col 5
                write(u'''\t\t\t\t<li style="padding: 3px;">\r
\t\t\t\t\t<a href="/mobile/eventview?eventid=''')
                _v = VFFSL(SL,"event.id",True) # u'$event.id' on line 60, col 41
                if _v is not None: write(_filter(_v, rawExpr=u'$event.id')) # from line 60, col 41.
                write(u'''&eventref=''')
                _v = VFFSL(SL,"event.sref",True) # u'$event.sref' on line 60, col 60
                if _v is not None: write(_filter(_v, rawExpr=u'$event.sref')) # from line 60, col 60.
                write(u'''" style="padding: 3px;">\r
\t\t\t\t\t\t<span class="ui-li-heading" style="margin-top: 0px; margin-bottom: 3px;">''')
                _v = VFFSL(SL,"event.title",True) # u'$event.title' on line 61, col 80
                if _v is not None: write(_filter(_v, rawExpr=u'$event.title')) # from line 61, col 80.
                write(u'''</span>\r
\t\t\t\t\t\t<span class="ui-li-desc" style="margin-bottom: 0px;">''')
                _v = VFFSL(SL,"event.begin",True) # u'$event.begin' on line 62, col 60
                if _v is not None: write(_filter(_v, rawExpr=u'$event.begin')) # from line 62, col 60.
                write(u''' - ''')
                _v = VFFSL(SL,"event.end",True) # u'$event.end' on line 62, col 75
                if _v is not None: write(_filter(_v, rawExpr=u'$event.end')) # from line 62, col 75.
                write(u'''</span>\r
\t\t\t\t\t</a>\t\r
\t\t\t\t</li>\r
''')
            write(u'''\t\t\t</ul>\r
\t\t</div>\r
''')
        write(u'''\r
\t\t<div id="footer">\r
\t\t\t<p>OpenWebif Mobile</p>\r
\t\t\t<a onclick="document.location.href=\'/index?mode=fullpage\';return false;" href="#">''')
        _v = VFFSL(SL,"tstrings",True)['show_full_openwebif'] # u"$tstrings['show_full_openwebif']" on line 72, col 86
        if _v is not None: write(_filter(_v, rawExpr=u"$tstrings['show_full_openwebif']")) # from line 72, col 86.
        write(u'''</a>\r
\t\t</div>\r
\t\t\r
\t</div>\r
 </body>\r
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

    _mainCheetahMethod_for_channelinfo= 'respond'

## END CLASS DEFINITION

if not hasattr(channelinfo, '_initCheetahAttributes'):
    templateAPIClass = getattr(channelinfo, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(channelinfo)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=channelinfo()).run()


