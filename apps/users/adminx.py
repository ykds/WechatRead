from users.models import UserProfile

from xadmin import views
import xadmin


class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class GlobalSetting:
    site_title = '微信阅读'
    site_footer = 'WechatReader'
    menu_style = 'accordion'


class UserProfileAdmin:
    list_display = ['nickname', 'email', 'gender', 'motto', 'province', 'city', 'read_time', 'likes']
    list_filter = ['gender', 'province', 'city']
    readonly_fields = ['read_time', 'likes']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
