# QuickUp-Linux(Ubuntu)

QuickUp的实验性质的Linux版本，基于Ubuntu 24.04 LTS。

需要提前安装微软雅黑和Segoe Fluent Icons字体。

在`\usr\share\fonts`新建`windows`目录，存放msyh.ttc、msyhbd.ttc、msyhl.ttc、Segoe Fluent lcons.ttf。

> 可能需要如下操作：
>
> 为windows目录设置权限`sudo chmod 755 windows`。
>
> 安装`sudo apt-get -y install fontconfig xfonts-utils`。
>
> 在/windows安装字体、建立索引并更新缓存`mkfontscale && mkfontdir && fc-cache -fv`。

查看新安装的字体fc-list :lang=zh