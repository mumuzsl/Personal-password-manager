# Personal-password-manager
个人密码管理器

## 开发历程

自己的各种账号越来越多，必须把它们记下来，最开始是用的记事本，但我觉得不够，就打算开发这样一个密码管理应用。

html + css + js 开发更快，界面能够快速设计，并且能够快速实现交互功能。这种模式能使应用体积更小，应用的更快，毕竟现在大家一般都有浏览器。

eel 可以调用Python代码，这样就可以操作sqlite数据库，js在数据库方面的支持并不友好，我最开始就想用js来操作sqlite数据库，但是遇到了阻碍，转而利用Django
框架开发小型web项目，但Django框架对我来说比较复杂，最后选择了eel + Python的简单模式，该模式还是有不足之处，但已经能够实现当初设想的功能。