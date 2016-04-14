import xbmc
import xbmcgui
import xbmcaddon
import httplib
import urllib

from settings import Settings

__addon__      = xbmcaddon.Addon()

ADDON_ID = __addon__.getAddonInfo('id')

def log(msg):
    xbmc.log("%s: %s" %(ADDON_ID, msg))

class DenonControlPlayer(xbmc.Player):
    STATE_VIDEO = 1
    STATE_MUSIC = 2

    def __init__(self, settings, *args, **kwargs):
        assert isinstance(settings, Settings)
        
        self.settings = settings
        self.last_state = 0
        super(DenonControlPlayer, self).__init__(*args, **kwargs)
        

    def onPlayBackStarted(self):
        if self.isPlayingVideo():
            if self.last_state != self.STATE_VIDEO:
                self.apply_video_settings()
                self.last_state = self.STATE_VIDEO
        elif self.isPlayingAudio():
            if self.last_state != self.STATE_MUSIC:
                self.apply_music_settings()
                self.last_state = self.STATE_MUSIC

    def apply_music_settings(self):
        """
        djusts the receiver sound settings for playing music
        """
        log("apply music settings")
        connection = httplib.HTTPConnection(self.settings.avr_ip)
        if self.settings.music_audyssey_enable:
            target="/SETUP/AUDIO/AUDYSSEY/s_audio.asp"
            data = {
                'setPureDirectOn': 'OFF',
                'setSetupLock': 'OFF',
                'listRoomEq': self.settings.music_audyssey_mode,
                'listRoomEqValue': 'Set',       
                'radioDynamicEq': self.settings.music_audyssey_dyneq,
                'radioDynamicVol': self.settings.music_audyssey_dynvol,
            }
            log(data)
            connection.request("POST", target, urllib.urlencode(data))
        

    def apply_video_settings(self):
        """
        Adjusts the receiver sound settings for playing videos
        """
        log("apply video settings")
        connection = httplib.HTTPConnection(self.settings.avr_ip)
        if self.settings.video_audyssey_enable:
            target="/SETUP/AUDIO/AUDYSSEY/s_audio.asp"
            data = {
                'setPureDirectOn': 'OFF',
                'setSetupLock': 'OFF',
                'listRoomEq': self.settings.video_audyssey_mode,
                'listRoomEqValue': 'Set',       
                'radioDynamicEq': self.settings.video_audyssey_dyneq,
                'radioDynamicVol': self.settings.video_audyssey_dynvol,
            }
            log(data)
            connection.request("POST", target, urllib.urlencode(data))

def main():
    s = Settings()
    player = None

    while not xbmc.abortRequested:
        if player is None:
            # Initialization only works with kwargs
            player = DenonControlPlayer(settings=s)
        else:
            xbmc.sleep(100)

if __name__ == '__main__':
    main()
