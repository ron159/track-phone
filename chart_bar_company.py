import pandas as pd
import numpy as np

from pyecharts import options as opts
from pyecharts.charts import Geo, Page, Map, Pie, Bar, WordCloud
from pyecharts.globals import ChartType, SymbolType


class Collector:
    charts = []

    @staticmethod
    def funcs(fn):
        Collector.charts.append((fn, fn.__name__))


C = Collector()

data = [('google.com', 4496),
 ('sinaimg.cn', 2287),
 ('qq.com', 1719),
 ('ithome.com', 916),
 ('miui.com', 535),
 ('ggpht.com', 533),
 ('bilivideo.com', 492),
 ('weibo.cn', 443),
 ('ks-live.com', 405),
 ('googleapis.com', 374),
 ('biliapi.net', 358),
 ('coolapk.com', 339),
 ('ruanmei.com', 297),
 ('xiaomi.com', 247),
 ('mi-img.com', 230),
 ('other', 3521)]

data.reverse()

data_night = [('ithome.com', 40),
 ('ks-live.com', 30),
 ('googleapis.com', 21),
 ('jd.com', 20),
 ('miui.com', 16),
 ('githubusercontent.com', 15),
 ('google.com', 14),
 ('ruanmei.com', 13),
 ('github.com', 12),
 ('360buyimg.com', 9),
 ('biliapi.net', 8),
 ('xiaomi.com', 8),
 ('gstatic.com', 8),
 ('bilibili.com', 5),
 ('googleusercontent.com', 4),
 ('pstatp.com', 3),
 ('xiaomi.net', 3),
 ('microsoft.com', 3),
 ('mi-img.com', 3),
 ('xn--ngstr-lra8j.com', 3),
 ('ksyun.com', 3),
 ('aliyuncs.com', 3),
 ('telegram.org', 2),
 ('appcenter.ms', 2),
 ('baidu.com', 2),
 ('windows.com', 2),
 ('net.in', 2),
 ('facebook.com', 2),
 ('bingapis.com', 2),
 ('lapin365.com', 2)]
data_night.reverse()

data_cloud = [
 ('google', 4496),
 ('sinaimg', 2287),
 ('qq', 1719),
 ('ithome', 916),
 ('miui', 535),
 ('ggpht', 533),
 ('bilivideo', 492),
 ('weibo', 443),
 ('ks-live', 405),
 ('googleapis', 374),
 ('biliapi.net', 358),
 ('coolapk', 339),
 ('ruanmei', 297),
 ('xiaomi', 247),
 ('mi-img', 230),
 ('jd', 179),
 ('bilibili', 166),
 ('hdslb', 146),
 ('weibo', 123),
 ('facebook', 117),
 ('alicdn', 106),
 ('twitter', 104),
 ('googlevideo', 97),
 ('googleusercontent', 88),
 ('gstatic', 83),
 ('smzdm', 81),
 ('qpic', 81),
 ('xiaomi.net', 77),
 ('qlogo', 73),
 ('coding.net', 71),
 ('office365', 70),
 ('amap', 70),
 ('doubanio', 66),
 ('douban', 65),
 ('gtimg', 63),
 ('alipay', 62),
 ('microsoft', 60),
 ('aliyuncs', 55),
 ('appcenter.ms', 53),
 ('ksyun', 43),
 ('githubusercontent', 42),
 ('twimg', 39),
 ('live', 39),
 ('pstatp', 39),
 ('gvt2', 35),
 ('youtube', 34),
 ('qingmang.me', 33),
 ('tanx', 31),
 ('v2ex', 31),
 ('qingmang.mobi', 29),
 ('360buyimg', 28),
 ('akamaized.net', 28),
 ('taobao', 27),
 ('zuihuimai', 26),
 ('weibocdn', 25),
 ('windows', 23),
 ('bing', 23),
 ('baidu', 23),
 ('ytimg', 23),
 ('xn--ngstr-lra8j', 22),
 ('alipayobjects', 22),
 ('lapin365', 22),
 ('xiaoheihe', 20),
 ('bingapis', 20),
 ('yandex', 19),
 ('net.in', 19),
 ('githubassets', 16),
 ('msn', 15),
 ('google', 15),
 ('github', 15),
 ('podcastrepublic.net', 15),
 ('pangolin-sdk-toutiao-b', 14),
 ('msedge.net', 13),
 ('com', 12),
 ('co.uk', 12),
 ('mi', 12),
 ('163', 11),
 ('bigfun', 11),
 ('bigfunapp', 11),
 ('biligame', 11),
 ('mozilla', 10),
 ('cdninstagram', 10),
 ('max-c', 10),
 ('tradplus', 10),
 ('t.co', 10),
 ('mozilla.org', 9),
 ('idqqimg', 9),
 ('office', 9),
 ('instagram', 9),
 ('sspai', 9),
 ('url', 7),
 ('mit.edu', 7),
 ('servicewechat', 7),
 ('learnsolid', 7),
 ('quoracdn.net', 7),
 ('126.net', 7),
 ('blogspot', 7),
 ('bmob', 7),
 ('2dogz', 7),
 ('intercom', 7),
 ('edu', 6),
 ('techkoala.top', 6),
 ('intercom.io', 6),
 ('firefox', 6),
 ('zdmimg', 6),
 ('cloudorz', 5),
 ('winudf', 5),
 ('fbcdn.net', 5),
 ('digicert', 5),
 ('wikimedia.org', 5),
 ('sandai.net', 5),
 ('googleapis', 5),
 ('applovefrom', 5),
 ('wikipedia.org', 5),
 ('hihonor', 5),
 ('akamaihd.net', 5),
 ('xtracloud.net', 5),
 ('jsdelivr.net', 4),
 ('alipay', 4),
 ('facebook.net', 4),
 ('lizhi.fm', 4),
 ('xmcdn', 4),
 ('pureapk', 4),
 ('fontawesome', 4),
 ('onedrive', 4),
 ('outlookmobile', 4),
 ('quora', 3),
 ('maxjia', 3),
 ('speedtest.net', 3),
 ('steampowered', 3),
 ('storyfm', 3),
 ('amazonaws', 3),
 ('gvt1', 3),
 ('miaopai', 3),
 ('ximalaya', 3),
 ('myapp', 3),
 ('gtimg', 3),
 ('helpshift', 3),
 ('loli.net', 3),
 ('t.me', 2),
 ('telegram.org', 2),
 ('tencentcloudapi', 2),
 ('cl2009', 2),
 ('bootstrapcdn', 2),
 ('statuspage.io', 2),
 ('solidproject.org', 2),
 ('adblockplus.org', 2),
 ('sfx.ms', 2),
 ('frdic', 2),
 ('mmstat', 2),
 ('everviz', 2),
 ('netease', 2),
 ('jquery', 2),
 ('redditstatic', 2),
 ('netease.im', 2),
 ('fxltsbl', 2),
 ('geetest', 2),
 ('myqcloud', 2),
 ('windows.net', 1),
 ('gubo.org', 1),
 ('esdict', 1),
 ('myhuaweicloud', 1),
 ('mozilla.net', 1),
 ('mzstatic', 1),
 ('getpodcast.xyz', 1),
 ('blogger', 1),
 ('wlvpn', 1),
 ('castbox.fm', 1),
 ('modpim', 1),
 ('xiaoka.tv', 1),
 ('highcharts', 1),
 ('mirrormedia.mg', 1),
 ('imgur', 1),
 ('adobedtm', 1),
 ('jjldbk', 1),
 ('live.net', 1),
 ('youke.co', 1),
 ('300hu', 1),
 ('licdn', 1),
 ('v2ex.co', 1),
 ('cdnpure', 1),
 ('umeng', 1),
 ('typlog.io', 1),
 ('justpodmedia', 1),
 ('duckduckgo', 1),
 ('sinastorage', 1),
 ('skype', 1),
 ('quickapp', 1),
 ('qiyukf', 1),
 ('soundon.fm', 1),
 ('fireside.fm', 1),
 ('crazy.capital', 1),
 ('fmit', 1),
 ('pythonhunter.org', 1),
 ('polyfill.io', 1),
 ('swift.gg', 1),
 ('coolapkmarket', 1),
 ('tangsuanradio', 1),
 ('pglstatp-toutiao', 1),
 ('cloudflare', 1),
 ('fyre.co', 1),
 ('telesco.pe', 1),
 ('tencentcs', 1),
 ('tinypass', 1),
 ('trafficmanager.net', 1),
 ('cdn-go', 1),
 ('kaolafm', 1)]


@C.funcs
def pie_base() -> Pie:
    c = (
        Pie()
            .add("", data)
            .set_global_opts(title_opts=opts.TitleOpts(title=""))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}", font_size=18))
    )
    return c


@C.funcs
def bar_base() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(width="100%", height="800%"))
            .add_xaxis(xaxis_data=[x[0] for x in data])
            .add_yaxis(series_name="所有公司排行",
                       color='#59a2a7',
                       y_axis=[x[1] for x in data])
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))

    )
    return c


@C.funcs
def bar_base() -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(width="100%", height="800%"))
            .add_xaxis(xaxis_data=[x[0] for x in data_night])
            .add_yaxis(series_name="夜间活动排行",
                       color='black',
                       y_axis=[x[1] for x in data_night])
            .reversal_axis()
            .set_series_opts(label_opts=opts.LabelOpts(position="right"))

    )
    return c


@C.funcs
def wordcloud_base() -> WordCloud:
    c = (
        WordCloud()
            .add("", data_cloud[0:], word_size_range=[12, 100], shape=SymbolType.DIAMOND)
            .set_global_opts(title_opts=opts.TitleOpts(title="词云"))
    )
    return c

Page().add(*[fn() for fn, _ in C.charts]).render('./output/map_bar_company.html')
