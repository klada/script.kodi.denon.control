import xbmcaddon

class Settings(object):
    """
    Loads the addon settings and makes them easily accessible.
    """
    AUDYSSEY_MODES = [
        'OFF',
        'AUDYSSEY',
        'BYP.LR',
        'FLAT'
    ]
    AUDYSSEY_DYNVOL = [
        'OFF',
        'LIT',
        'MED',
        'HEV'
    ]

    def __init__( self, *args, **kwargs ):
        self.addon = xbmcaddon.Addon()
        self.read_settings()
    
    def get_audyssey_mode(self, setting_id):
        return self.AUDYSSEY_MODES[int(self.addon.getSetting(setting_id))]
    
    def get_audyssey_dynvol(self, setting_id):
        return self.AUDYSSEY_DYNVOL[int(self.addon.getSetting(setting_id))]
    
    def get_audyssey_dyneq(self, setting_id):
        if self.get_bool(setting_id):
            return 'ON'
        else:
            return 'OFF'
        
    def get_bool(self, setting_id):
        return self.addon.getSetting(setting_id) == 'true'

    def read_settings(self):
        self.avr_ip             = self.addon.getSetting("avr_ip")

        self.music_audyssey_enable = self.get_bool("music_audyssey_enable")
        self.music_audyssey_mode = self.get_audyssey_mode("music_audyssey_mode")
        self.music_audyssey_dyneq = self.get_audyssey_dyneq("music_audyssey_dyneq")
        self.music_audyssey_dynvol = self.get_audyssey_dynvol("music_audyssey_dynvol")
        
        self.video_audyssey_enable = self.get_bool("video_audyssey_enable")
        self.video_audyssey_mode = self.get_audyssey_mode("video_audyssey_mode")
        self.video_audyssey_dyneq = self.get_audyssey_dyneq("video_audyssey_dyneq")
        self.video_audyssey_dynvol = self.get_audyssey_dynvol("video_audyssey_dynvol")
