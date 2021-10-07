from jnius import autoclass
from kivy.logger import Logger

PythonActivity = autoclass("org.kivy.android.PythonActivity").mActivity
Context = autoclass('android.content.Context')
ContextCompat = autoclass('android.support.v4.content.ContextCompat')

def check_permission(permission, activity=PythonActivity):
    permission_status = ContextCompat.checkSelfPermission(activity,
                                                          permission)

    Logger.info(permission_status)
    permission_granted = 0 == permission_status
    Logger.info("Permission Status: {}".format(permission_granted))
    return permission_granted

def ask_permission(permission, activity=PythonActivity):
    PythonActivity.requestPermissions(['android.permission.WRITE_EXTERNAL_STORAGE',
                                       'android.permission.ACCESS_NETWORK_STATE',
                                       'android.permission.CAMERA',
                                       'android.permission.INTERNET',
                                       'android.permission.MANAGE_DOCUMENTS',
                                       'android.permission.MANAGE_EXTERNAL_STORAGE',
                                       'android.permission.READ_EXTERNAL_STORAGE',
                                       'android.permission.WRITE_EXTERNAL_STORAGE',
                                       ])