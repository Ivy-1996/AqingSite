from django.db import models


class CompanyInfo(models.Model):
    logo = models.ImageField(upload_to='upload/', verbose_name='公司logo')

    name = models.CharField(max_length=255, verbose_name='公司名称')
    desc = models.TextField(verbose_name='公司简介')
    short_desc = models.CharField(max_length=526, verbose_name='公司简介')
    image = models.ImageField(upload_to='upload/', verbose_name='公司照片')

    location = models.CharField(max_length=256, default='', verbose_name='公司地址')
    phone_num = models.CharField(max_length=50, default='', verbose_name='手机电话')
    mobile = models.CharField(max_length=11, default='', verbose_name='座机号码')
    email = models.EmailField(default='', verbose_name='邮件')
    wechat = models.CharField(max_length=255, default='', verbose_name='微信')

    display = models.BooleanField(default=False, verbose_name='是否为默认选项')

    class Meta:
        verbose_name = verbose_name_plural = '公司信息'

    def __str__(self):
        return self.name


class Banner(models.Model):
    desc = models.CharField(max_length=50, null=True, blank=True, verbose_name='轮播图描述')
    image = models.ImageField(upload_to='upload/', verbose_name='轮播图片')
    display = models.BooleanField(default=True, verbose_name='是否展示')
    index = models.SmallIntegerField(default=0, verbose_name='优先级')

    class Meta:
        verbose_name = verbose_name_plural = '轮播图'

    def __str__(self):
        return self.desc


class News(models.Model):
    TYPE_CHOICES = (
        (0, '公司新闻'),
        (1, '行业新闻'),
    )

    title = models.CharField(max_length=30, verbose_name='标题')
    content = models.CharField(max_length=255, verbose_name='内容')
    image = models.ImageField(upload_to='upload/', verbose_name='图片')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    type = models.SmallIntegerField(choices=TYPE_CHOICES, default=0, verbose_name='类型')
    display = models.BooleanField(default=True, verbose_name='是否展示')

    class Meta:
        verbose_name = verbose_name_plural = '新闻'

    def __str__(self):
        return self.title


class Cases(models.Model):
    TYPE_CHOICES = (
        (0, '家装案例'),
        (1, '工装案例'),
        (2, '其他案例'),
    )

    title = models.CharField('标题', max_length=30)
    content = models.CharField('内容', max_length=255)
    image = models.ImageField('图片', upload_to='upload/')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    type = models.SmallIntegerField('类型', choices=TYPE_CHOICES, default=0)
    display = models.BooleanField('是否展示', default=True)

    class Meta:
        verbose_name = verbose_name_plural = '装修案例'

    def __str__(self):
        return self.title


class Recruitment(models.Model):
    title = models.CharField('标题', max_length=56)
    content = models.CharField('内容', max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    desc = models.CharField(max_length=256)
    display = models.BooleanField(default=True)

    class Meta:
        verbose_name = verbose_name_plural = '招聘信息'

    def __str__(self):
        return self.title


class Staff(models.Model):
    name = models.CharField(max_length=10)
    desc = models.CharField(max_length=526)
    avatar = models.ImageField(upload_to='upload/')
    create_time = models.DateTimeField(auto_now_add=True)
    display = models.BooleanField(default=True)

    class Meta:
        verbose_name = verbose_name_plural = '员工信息'

    def __str__(self):
        return self.name
