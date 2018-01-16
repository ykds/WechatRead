from users.models import UserProfile, Follow, Account, DealLog, Purchased, EmailVerifyCode

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


class FollowAdmin:
    list_display = ['followed', 'following', 'follow_time']


class AccountAdmin:
    list_display = ['user', 'balance', 'present', 'recharge']


class PurchasedAdmin:
    list_display = ['user', 'book', 'chapter', 'buy_time']
    list_filter = ['user', 'book', 'chapter']


class DealLogAdmin:
    list_display = ['user', 'book', 'chapter', 'buy_type', 'use_currency', 'money']
    list_filter = ['user', 'book', 'chapter']

class EmailVerifyAdmin:
    list_display = ['code', 'email', 'send_type', 'add_time']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(Follow, FollowAdmin)
xadmin.site.register(Account, AccountAdmin)
xadmin.site.register(EmailVerifyCode, EmailVerifyAdmin)
xadmin.site.register(Purchased, PurchasedAdmin)
xadmin.site.register(DealLog, DealLogAdmin)